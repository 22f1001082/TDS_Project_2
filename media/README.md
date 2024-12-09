# Media Dataset Analysis 
## Data Description
The dataset appears to contain information related to content, possibly reviews or articles, organized into several columns. The 'date' column likely represents the publication or submission date of each entry. The 'language' column indicates the language in which the content is written. The 'type' column may categorize the content type, such as review, article, or essay. The 'title' column contains the titles of the respective entries, while the 'by' column likely identifies the author or contributor of the content. The 'overall' column could represent an overall rating or score given to the content, possibly reflecting its quality or relevance. The 'quality' column might provide a more detailed assessment of the content quality, while the 'repeatability' column could measure the consistency or reliability of the content or rating. Overall, the dataset seems to focus on evaluating and categorizing various pieces of content across different languages and types.
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
## Data Story
In examining a dataset of 2,652 items, a compelling narrative emerges around their overall performance and specific quality metrics, as well as repeatability measures. The average overall score stands at approximately 3.05, indicating a generally positive assessment but with room for improvement, as highlighted by a standard deviation of 0.76. This suggests that while many items hover around the mean, others diverge significantly, reflecting a landscape of varying performance levels.

When we delve deeper into the quality ratings, we observe a slightly higher mean of 3.21, which introduces the notion that quality is perceived marginally better than the overall experience. The distribution of quality scores reveals that 75% of the evaluated items score 4 or lower, with a minimum quality score of 1 and a maximum of 5. This indicates that while many items meet a standard of quality, there are still substantial gaps, particularly for a minority of items scoring at the lower end.

Another critical aspect of our analysis is the measure of repeatability, with a mean score of around 1.49. This score suggests that repeat engagements with these items yield inconsistent experiences, as indicated by a standard deviation of 0.60. Notably, a quarter of the items receive a repeatability score of just 1, suggesting that most users are unlikely to engage with them again.

In summary, this dataset paints a picture of products that are generally seen as satisfactory in quality yet exhibit variability in overall performance and repeatability. The analysis encourages stakeholders to focus on enhancing the quality and consistency of the lower-performing items to improve overall customer satisfaction and foster repeat interactions.
