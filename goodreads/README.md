# Goodreads Dataset Analysis 
## Data Description
The dataset appears to contain information about books, likely sourced from a platform like Goodreads. Each row represents a unique book entry, identified by a `book_id` and potentially linked to a Goodreads-specific identifier. The dataset includes various attributes that describe the book, such as `goodreads_book_id`, `best_book_id`, and `work_id`, which may relate to metadata about the book across different formats or editions.

Additional attributes provide insights into the book's details, including `isbn` and `isbn13` for international book identifiers, `authors` for the creators of the book, and `original_publication_year` revealing when the book was first published. Information such as `original_title` and `title` captures the book's name.

The dataset also includes several columns related to the book's reception, such as `average_rating`, `ratings_count`, and `work_ratings_count`, which indicate how well the book is perceived and the volume of ratings it has received. The ratings are further broken down into categories from 1 to 5 stars via `ratings_1` through `ratings_5`, providing a detailed view of reader sentiment.

Additionally, the dataset contains visual elements with `image_url` and `small_image_url` for book cover images and supports multilingual aspects with the `language_code`. Overall, this dataset serves as a comprehensive resource for analyzing various aspects of books and their reception in a reading community.
## Data Overview
### Summary Statistics
| Stat | book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn13 | original_publication_year | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 9415.000 | 9979.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 | 10000.000 |
| mean | 5000.500 | 5264696.513 | 5471213.580 | 8646183.425 | 75.713 | 9755044298883.463 | 1981.988 | 4.002 | 54001.235 | 59687.322 | 2919.955 | 1345.041 | 3110.885 | 11475.894 | 19965.697 | 23789.806 |
| std | 2886.896 | 7575461.864 | 7827329.891 | 11751060.824 | 170.471 | 442861920665.573 | 152.577 | 0.254 | 157369.956 | 167803.785 | 6124.378 | 6635.626 | 9717.124 | 28546.449 | 51447.358 | 79768.886 |
| min | 1.000 | 1.000 | 1.000 | 87.000 | 1.000 | 195170342.000 | -1750.000 | 2.470 | 2716.000 | 5510.000 | 3.000 | 11.000 | 30.000 | 323.000 | 750.000 | 754.000 |
| 25% | 2500.750 | 46275.750 | 47911.750 | 1008841.000 | 23.000 | 9780316192995.000 | 1990.000 | 3.850 | 13568.750 | 15438.750 | 694.000 | 196.000 | 656.000 | 3112.000 | 5405.750 | 5334.000 |
| 50% | 5000.500 | 394965.500 | 425123.500 | 2719524.500 | 40.000 | 9780451528640.000 | 2004.000 | 4.020 | 21155.500 | 23832.500 | 1402.000 | 391.000 | 1163.000 | 4894.000 | 8269.500 | 8836.000 |
| 75% | 7500.250 | 9382225.250 | 9636112.500 | 14517748.250 | 67.000 | 9780830777175.000 | 2011.000 | 4.180 | 41053.500 | 45915.000 | 2744.250 | 885.000 | 2353.250 | 9287.000 | 16023.500 | 17304.500 |
| max | 10000.000 | 33288638.000 | 35534230.000 | 56399597.000 | 3455.000 | 9790007672390.000 | 2017.000 | 4.820 | 4780653.000 | 4942365.000 | 155254.000 | 456191.000 | 436802.000 | 793319.000 | 1481305.000 | 3011543.000 |

### Missing Values
| Column | Missing Count | Missing Percentage (%) |
|--------|------------|----------------------|
| book_id | 0.0 | 0.00 |
| goodreads_book_id | 0.0 | 0.00 |
| best_book_id | 0.0 | 0.00 |
| work_id | 0.0 | 0.00 |
| books_count | 0.0 | 0.00 |
| isbn | 700.0 | 7.00 |
| isbn13 | 585.0 | 5.85 |
| authors | 0.0 | 0.00 |
| original_publication_year | 21.0 | 0.21 |
| original_title | 585.0 | 5.85 |
| title | 0.0 | 0.00 |
| language_code | 1084.0 | 10.84 |
| average_rating | 0.0 | 0.00 |
| ratings_count | 0.0 | 0.00 |
| work_ratings_count | 0.0 | 0.00 |
| work_text_reviews_count | 0.0 | 0.00 |
| ratings_1 | 0.0 | 0.00 |
| ratings_2 | 0.0 | 0.00 |
| ratings_3 | 0.0 | 0.00 |
| ratings_4 | 0.0 | 0.00 |
| ratings_5 | 0.0 | 0.00 |
| image_url | 0.0 | 0.00 |
| small_image_url | 0.0 | 0.00 |

Duplicate Rows: 0
## Outliers
|Column|Outlier Count|
|-------|-------|
|book_id|0|
|goodreads_book_id|345|
|best_book_id|357|
|work_id|601|
|books_count|844|
|isbn13|556|
|original_publication_year|1031|
|average_rating|158|
|ratings_count|1163|
|work_ratings_count|1143|
|work_text_reviews_count|1005|
|ratings_1|1140|
|ratings_2|1156|
|ratings_3|1149|
|ratings_4|1131|
|ratings_5|1158|
<div style="display: flex; flex-wrap: wrap; width: 120%;">
<img src="outliers_1.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
<img src="outliers_2.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
<img src="outliers_3.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
<img src="outliers_4.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
</div>
 
## Correlation Heatmap

![alt_text](correlation_heatmap.png)
## Analysis Recommendations
Here are 10 analysis recommendations that a data analyst can perform on the given dataset's summary statistics:

1. **Descriptive Statistics**: Calculate descriptive statistics (mean, median, mode, standard deviation) for numerical columns, such as `average_rating`, `ratings_count`, and `work_text_reviews_count`, to get a sense of the distribution and the overall rating trends.

2. **Correlation Analysis**: Conduct a correlation analysis between different numerical variables (e.g., `average_rating`, `ratings_count`, and `work_ratings_count`) to identify relationships and potential predictors of book ratings.

3. **Rating Distribution Analysis**: Visualize the distribution of ratings (e.g., `ratings_1`, `ratings_2`, ..., `ratings_5`) through histograms or bar charts to understand how readers rate books and to identify any potential biases in the rating system.

4. **Author Analysis**: Analyze the `authors` variable to determine which authors have the highest average ratings and which authors have the most works in the dataset. Identify trends or patterns among popular authors.

5. **Publication Year Trend**: Analyze how the average book ratings have changed over time by grouping data by `original_publication_year` and calculating average ratings to spot any trends related to book quality over the years.

6. **Language Code Analysis**: Compare average ratings by `language_code` to see if books in certain languages tend to receive better ratings than others. This could provide insights into cultural or regional preferences in reading.

7. **Top Rated Books**: Identify and list the top 10 books with the highest `average_rating` and provide additional insights on the `authors`, `original_publication_year`, and `ratings_count` for context.

8. **Image URL Analysis**: Analyze the impact of book cover images (`image_url` and `small_image_url`) on average ratings by collecting qualitative feedback or performing sentiment analysis on user comments or reviews.

9. **Review Count Impact**: Investigate whether there is a correlation between the number of `work_text_reviews_count` and `average_rating`. Assess if higher engagement (more reviews) leads to higher average ratings.

10. **ISBN Analysis**: Check the uniqueness and completeness of the `isbn` and `isbn13` fields. Conduct analyses on how the presence of ISBN affects the availability and discoverability of books within the dataset.

These recommendations will help the analyst gain meaningful insights into the dataset and potentially uncover interesting patterns and trends in book ratings and readership.
## Data Story
In a comprehensive analysis of a dataset consisting of 10,000 books, intriguing insights emerge regarding readership, popularity, and ratings. The dataset spans an impressive range of book IDs from 1 to 10,000, showcasing an average book ID of 5000.5, indicating a comprehensive and diverse catalog.

Each book is linked to a Goodreads book ID, with a mean of approximately 5.26 million, reflecting a vast spectrum of titles and interests. Notably, the highest Goodreads book ID reaches over 33 million, highlighting the presence of extremely popular titles within this dataset.

Delving deeper, we find that these books have an average of about 75.7 books in each collection, with a maximum collection reaching an astounding 3,455 books. This suggests that a significant number of readers are avid collectors or have an extensive array of reading interests.

The original publication years of the books span a wide timeline, with an average year of 1981, but with some books dating back as far as 1750. This indicates a well-rounded collection that includes both contemporary works and historical classics. The average rating across the board sits at 4.00, showcasing a generally positive reception of the books. Ratings are distributed quite evenly, with nearly equal portions of the ratings spread across 1 to 5 stars, but with notably high averages for 4 and 5-star ratings, suggesting that readers predominantly enjoy these books.

When we look at the ratings count, the data reveals that the average book has received over 54,000 ratings, with the most-rated book amassing nearly 4.8 million ratings, a testament to its widespread acclaim. Surprisingly, while the average book garners approximately 2,920 text reviews, the maximum number of reviews is sky-high at 155,254, exemplifying the engagement certain titles receive from their readership.

This dataset tells a compelling story of a vibrant literary landscape filled with passionate readers, diverse genres, and significant engagement, inviting further exploration into the nuances of individual titles and their unique impacts on readers.
