# Media Dataset Analysis 
## Data Description
The dataset contains information related to various entries characterized by their date of entry, language, and type. Each entry has a title and is attributed to an author (by). It includes numerical ratings such as overall score, quality assessment, and repeatability, which likely reflect the evaluations or metrics relevant to the entries. The combination of these columns suggests that the dataset could be focused on assessing content, possibly in a review or feedback context across different languages and types of media or documents.
## Data Overview
### Summary Statistics
| Stat | overall | quality | repeatability |
| --- | --- | --- | --- |
| count | 2652.000 | 2652.000 | 2652.000 |
| mean | 3.048 | 3.209 | 1.495 |
| std | 0.762 | 0.797 | 0.598 |
| min | 1.000 | 1.000 | 1.000 |
| 25% | 3.000 | 3.000 | 1.000 |
| 50% | 3.000 | 3.000 | 1.000 |
| 75% | 3.000 | 4.000 | 2.000 |
| max | 5.000 | 5.000 | 3.000 |

### Missing Values
| Column | Missing Count | Missing Percentage (%) |
|--------|------------|----------------------|
| date | 99.0 | 3.73 |
| language | 0.0 | 0.00 |
| type | 0.0 | 0.00 |
| title | 0.0 | 0.00 |
| by | 262.0 | 9.88 |
| overall | 0.0 | 0.00 |
| quality | 0.0 | 0.00 |
| repeatability | 0.0 | 0.00 |

Duplicate Rows: 1
## Outliers
|Column|Outlier Count|
|-------|-------|
|overall|1216|
|quality|24|
|repeatability|0|
<div style="display: flex; flex-wrap: wrap; width: 120%;">
<img src="outliers_1.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
</div>
 
## Correlation Heatmap

![alt_text](correlation_heatmap.png)
## Analysis Recommendations
Certainly! Given the dataset's summary statistics, the analyst can perform the following analyses to gain valuable insights:

1. **Trend Analysis over Time**: Analyze how 'overall' and 'quality' scores change over different dates. This can reveal trends in performance or preferences over time.

2. **Language Distribution**: Explore the distribution of data points by 'language' to understand which languages are most represented and if there are any patterns in 'overall' or 'quality' scores across languages.

3. **Type Analysis**: Examine the data stratified by 'type' (e.g., article, review, etc.) to identify how different types affect metrics like 'overall' and 'quality'.

4. **Author Performance**: Analyze the 'by' field to assess the performance of different authors based on their average 'overall' and 'quality' ratings, helping identify high or low performers.

5. **Correlation Analysis**: Calculate correlation coefficients between 'overall', 'quality', and 'repeatability' to assess whether repeatability influences quality and overall scores.

6. **Sentiment Analysis on Titles**: Perform sentiment analysis on the 'title' field to determine how sentiment correlates with 'overall' scores, which may provide insights on how positive or negative titles impact experiences.

7. **Categorical Distribution Analysis**: Create visualizations (like bar charts) to show the distribution of 'overall' scores across different categories of 'language', 'type', or 'by', identifying any significant disparities.

8. **Box Plots for Quality Assessment**: Use box plots to visualize the distribution of 'quality' ratings across different languages or types, highlighting any outliers and providing insights into quality variability.

9. **Repeatability Impact Assessment**: Investigate how 'repeatability' affects the 'overall' score by conducting a regression analysis, possibly indicating how often the same user returns and its impact on quality perception.

10. **Temporal Patterns**: Conduct a seasonal analysis to determine whether certain times of year tend to yield higher or lower 'overall' and 'quality' scores, looking into potential cyclic trends.

These analyses will help the data analyst extract meaningful insights and formulate data-driven recommendations or strategies based on the identified trends and patterns.
## Data Story
In analyzing a dataset comprising responses from 2,652 individuals, several intriguing insights emerged that provide a glimpse into the overall perceptions of quality and repeatability. 

When we look at the overall ratings, the average score stands at approximately 3.05, suggesting a moderate level of satisfaction among respondents. The standard deviation of 0.76 highlights a reasonable spread in the responses, with the ratings spanning from a minimum of 1 to a maximum of 5. Notably, a quarter of the respondents provided scores of 3 or lower, indicating that while many find the service satisfactory, a significant portion remains underwhelmed.

Diving deeper into quality, the average score rises to around 3.21. This slightly higher mean, coupled with a standard deviation of 0.80, reflects a trend where more respondents are leaning towards positive experiences. A majority (75%) rated the quality at 4 or below, suggesting that while quality is perceived positively, there’s still considerable room for improvement.

The repeatability metric, however, tells a different story. Scoring an average of just 1.49 presents a stark contrast. This low mean, alongside a standard deviation of 0.60, indicates that many respondents found their experiences less likely to be repeated. A significant number of respondents (over 75%) rated their likelihood to repeat at or below 1, highlighting a troubling sentiment regarding brand loyalty or satisfaction with repeat experiences.

Overall, this dataset paints a nuanced picture: while quality perceptions are somewhat positive, there remains a significant gap in customers' willingness to return. Addressing the factors behind this low repeatability could be critical for organizations looking to enhance customer satisfaction and foster loyalty.
