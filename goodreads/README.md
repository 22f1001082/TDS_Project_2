# Goodreads Dataset Analysis 
## Data Description
The dataset appears to be a collection of information about books, likely sourced from a platform like Goodreads. Each entry is identified by a unique `book_id` and is associated with other identifiers such as `goodreads_book_id`, `best_book_id`, and `work_id`. It includes metadata about the books, such as the `authors`, `original_title`, and `title`. The dataset also captures publication details, specifically the `original_publication_year` and `language_code`. 

Several columns provide insights into the book's reception and popularity, including `average_rating`, `ratings_count`, and `work_ratings_count`, alongside specific ratings across different categories (1 to 5 stars). There are also columns related to the book's ISBN numbers (`isbn`, `isbn13`) for identification purposes. Visual representation is supported through `image_url` and `small_image_url`, offering links to book cover images. The dataset seems to be structured for analysis or exploration of book popularity and reader feedback.
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
To gain insights from the dataset described, the analyst can perform a variety of analyses. Here are ten recommended analyses:

1. **Descriptive Statistics**:
   - Calculate descriptive statistics (mean, median, mode, standard deviation, and range) for numerical variables such as `average_rating`, `ratings_count`, and `work_ratings_count` to understand their distribution.

2. **Rating Distribution Analysis**:
   - Analyze the distribution of the ratings (from `ratings_1` to `ratings_5`) to identify common rating patterns and find out if there are any biases in the ratings.

3. **Authors' Performance Analysis**:
   - Aggregate `average_rating` and `ratings_count` by `authors` to identify which authors have the highest rated books and the most engagement based on ratings.

4. **Impact of Publication Year**:
   - Investigate the trend of `average_rating` over the years (using `original_publication_year`) to see if newer books are receiving higher ratings compared to older titles.

5. **Language Analysis**:
   - Analyze `average_rating` and `ratings_count` based on `language_code` to see if there are differences in engagement or satisfaction based on the language of the books.

6. **Top Rated Books**:
   - Identify the top-rated books based on `average_rating` and `ratings_count`, providing insight into which books are popular and well-received.

7. **Book Count Analysis**:
   - Examine the distribution of `books_count` for each author to understand how the number of books published by an author correlates with average ratings and reader engagement.

8. **Correlations**:
   - Perform correlation analysis between `average_rating`, `ratings_count`, and other numerical variables to identify relationships and potential patterns.

9. **Content Analysis**:
   - Analyze the `original_title` and `title` fields to identify common keywords or phrases in high-rated books, which can provide insights into popular themes or topics.

10. **Image URL Analysis**:
    - Investigate if having high-quality book covers (as indicated by the presence of an image URL) correlates with higher ratings or ratings counts, assessing the impact of marketing on reader engagement.

These analyses will help the analyst glean valuable insights, uncover trends, and understand factors affecting book ratings and engagement.
## Data Story
In the world of literature, our dataset reveals intriguing insights into a collection of 10,000 books, each contributing to a vibrant and diverse reading experience. The average book in this dataset boasts a Goodreads rating of 4.00, underlining the high level of reader satisfaction, with ratings mostly clustering around four stars. Yet, the range of ratings is telling—across the dataset, books have received as few as 2.47 stars to a maximum of 4.82, indicating some titles spark substantial admiration while others may leave readers wanting.

The ratings distribution highlights an interesting pattern, with 23,789 average five-star ratings across the dataset—the highest among all ratings categories—which suggests that a notable portion of books has achieved critical acclaim. The lowest rated books, in comparison, have only garnered around 1,345 one-star ratings, signaling a significant divide in reader opinions.

Diving deeper, we find that these books come from varied publication years, with the average publication dating back to 1982. This means our collection spans an impressive historical range, capturing literary voices from multiple generations. The oldest book in the dataset appears to date as far back as 1750, while newer titles continue to captivate modern readers, with some published as recently as 2017.

The dataset also reveals the depth of engagement readers have with these works. On average, 75.7 books are recorded per reader, a testament to the book-loving habits of this community. Some readers exhibit voracious appetites, with the maximum noted at 3,455 books, indicating an exceptional enthusiasm for exploring literature.

Analyzing the Goodreads book IDs, we see that many titles possess a high visibility, with an average Goodreads ID reaching over 5 million, showcasing their presence in a broader reading community. The ratings count further reveals a bustling interaction between books and readers, with average ratings counts around 54,001, illustrating robust reader engagement.

In summary, the dataset paints a rich portrait of literary preferences, reader engagement, and the appreciation of books that span decades. With high average ratings, a diverse range of titles, and active reader interaction, this dataset exemplifies the enduring love for books and their profound impact on reading communities.
