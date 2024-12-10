# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "chardet",
#     "matplotlib",
#     "pandas",
#     "python-dotenv",
#     "requests",
#     "seaborn",
# ]
# ///


import os
import sys
import seaborn as sns
import requests
import shutil
import chardet
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()


def llm(message):
    AI_TOKEN = os.environ("AIPROXY_TOKEN")
    headers = {"Authorization": f"Bearer {AI_TOKEN}", "Content-Type": "application/json"}  
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": message}]
    }
    try:
        response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def configure_folder(filename):
    folder_name = os.path.splitext(filename)[0]
    source_path = os.path.join(os.getcwd(), filename)
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        shutil.copy2(source_path, folder_path)
        print(f"Folder '{folder_name}' created and file '{filename}' copied.")
    else:
        if os.path.exists(file_path):
            print(f"File '{filename}' already exists in the folder.")
        else:
            shutil.copy2(source_path, folder_path)
            print(f"File '{filename}' copied to the folder.")
        print(f"Folder '{folder_name}' already exists.")
    return folder_name, folder_path, file_path


def get_encoding(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encoding = chardet.detect(data)["encoding"]
    return encoding


def read_file(file_path):
    encoding = get_encoding(file_path)
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def data_description(df):
    cols = df.columns
    try:
        ai_summary = llm(f"There is a pandas dataframe with the following columns: {cols}. Briefly describe the dataset? Do not give any headings in the response.")  
        summary_stats = df.describe()
        summary_stats = summary_stats.to_dict()

        # Format summary stats as a table for markdown
        stats = next(iter(summary_stats.values())).keys()
        metrics = summary_stats.keys()  # Metric names
        headers = ["Stat"] + list(metrics)
        rows = []
        for stat in stats:
            row = [stat] + [
                f"{summary_stats[metric].get(stat, ''):.3f}" if isinstance(summary_stats[metric].get(stat), (int, float)) else summary_stats[metric].get(stat, '')
                for metric in metrics
            ]
            rows.append(row)
        # Create the Markdown table
        ss_table = f"| {' | '.join(headers)} |\n"
        ss_table += f"| {' | '.join(['---'] * len(headers))} |\n"
        for row in rows:
            ss_table += f"| {' | '.join(map(str, row))} |\n"
        return ai_summary, ss_table
    except Exception as e:
        print(f"Error generating summary: {e}")
        sys.exit(1)


def count_outliers(df):
    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]).columns.tolist()

    if not isinstance(numeric_cols, list) or not numeric_cols:
        return {}

    outlier_counts = {}
    for col in numeric_cols:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            outlier_counts[col] = len(outliers)
        else:
            # Or handle the case where the column is not numeric or does not exist
            outlier_counts[col] = 0
    return outlier_counts


def plot_outliers(df, output_dir, col_per_plot=4):
    columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    num_plots = len(columns)
    cols_per_plot = 4  # Number of columns per plot
    files = []
    for i in range(0, num_plots, cols_per_plot):
        fig, axes = plt.subplots(
            1, min(cols_per_plot, num_plots - i), figsize=(15, 5))
        for j, col in enumerate(columns[i:min(i + cols_per_plot, num_plots)]):
            if num_plots <= cols_per_plot:
                sns.boxplot(y=df[col], ax=axes[j])
                axes[j].set_title(f"Outlier plot for {col}")
            else:
                sns.boxplot(y=df[col], ax=axes[j])
                axes[j].set_title(f"Outlier plot for {col}")
            plt.suptitle("Outliers for Columns")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/outliers_{i//cols_per_plot + 1}.png")
        files.append(f"outliers_{i//cols_per_plot + 1}.png")
        plt.close(fig)
    return files


def generic_analysis(df):
    missing_values = df.isnull().sum()
    missing_percentage = df.isnull().mean() * 100

    # Create a DataFrame to store the null summary
    null_summary = pd.DataFrame({
        'Missing Count': missing_values,
        'Missing Percentage (%)': missing_percentage
    })
    # Convert the DataFrame to a Markdown table
    missing_table = "| Column | Missing Count | Missing Percentage (%) |\n"
    missing_table += "|--------|------------|----------------------|\n"
    # Iterate over rows in the null_summary DataFrame and add to the table
    for column, row in null_summary.iterrows():
        missing_table += f"| {column} | {row['Missing Count']} | {row['Missing Percentage (%)']:.2f} |\n"  

    duplicate_rows = df.duplicated().sum()
    outlier_counts = count_outliers(df)
    ai_summary, summary_stats = data_description(df)
    return ai_summary, summary_stats, missing_table, duplicate_rows, outlier_counts


def generate_correlation_heatmap(df, output_dir, output_file='correlation_heatmap.png'):
    # Filter out non-numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Ensure there are numeric columns
    if numeric_df.shape[1] < 2:
        raise ValueError("DataFrame must contain at least two numeric columns for correlation analysis.")

    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr()

    # Determine the size of the heatmap dynamically
    num_columns = corr_matrix.shape[1]
    max_size = 16  # Maximum figure size in inches to prevent rendering issues
    figsize = (min(max_size, num_columns * 1.2),min(max_size, num_columns * 1.2))

    # Create the heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title("Correlation Heatmap")
    # Save the heatmap
    output_location = os.path.join(output_dir, output_file)
    plt.savefig(output_location, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Correlation heatmap saved as {output_file}")
    return output_file


def data_story(df):
    summary_stats = df.describe().to_dict()
    try:
        data_story = llm(f"Suppose you are a data analyst trying to generate a compelling story about a dataset. Use the following summary statistics to generate a short data story: {summary_stats}. Do not format the output.")  
        return data_story
    except Exception as e:
        print(e)
        return None
    
def recommended_analysis(df):
    columns = df.columns
    try:
        analysis_recommendation = llm(f"Suppose a data analyst is trying to analyze a dataset with the following summary statistics: {columns}. What analysis should the analyst perform to gain insights from the data? Return a list of 10 analysis recommendations.")
        return analysis_recommendation
    except Exception as e:
        print(f"Error: {e}")
        return None


def create_md(filename):
    file_name, folder_path, file_path = configure_folder(filename)
    df = read_file(file_path)
    ai_summary, summary_stats, missing_table, duplicate_rows, outlier_counts = generic_analysis(df)  
    outlier_files = plot_outliers(df, folder_path)
    heatmap_file = generate_correlation_heatmap(df, folder_path)
    analysis_recommendation = recommended_analysis(df)
    story = data_story(df)
    with open(f"{os.path.join(folder_path, "README.md")}", "w") as f:
        f.write(f"# {file_name.title()} Dataset Analysis \n")
        f.write("## Data Description\n")
        f.write(f"{ai_summary}\n")
        f.write("## Data Overview\n")
        f.write("### Summary Statistics\n")
        f.write(f"{summary_stats}\n")
        f.write("### Missing Values\n")
        f.write(f"{missing_table}\n")
        f.write(f"Duplicate Rows: {duplicate_rows}\n")
        f.write("## Outliers\n")
        f.write("|Column|Outlier Count|\n|-------|-------|\n")
        for item in outlier_counts:
            f.write(f"|{item}|{outlier_counts[item]}|\n")
        f.write('<div style="display: flex; flex-wrap: wrap; width: 120%;">\n')
        for image in outlier_files:
            f.write(f'<img src="{image.replace(" ", "_").lower()}" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>\n')
        f.write('</div>\n')
        f.write(' \n')
        f.write("## Correlation Heatmap\n")
        f.write(f"\n![alt_text]({heatmap_file})\n")
        f.write("## Analysis Recommendations\n")
        f.write(f"{analysis_recommendation}\n")
        f.write("## Data Story\n")
        f.write(f"{story}\n")
    os.remove(file_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python autolysis.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    create_md(filename)
