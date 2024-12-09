# Happiness Dataset Analysis 
## Data Description
The dataset appears to contain information related to various aspects of well-being and quality of life across different countries and years. Each row represents a specific country's data for a particular year, capturing factors that contribute to happiness and life satisfaction. The "Life Ladder" column likely reflects subjective well-being or happiness levels, while "Log GDP per capita" provides an economic perspective, indicating wealth distribution. Other columns, such as "Social support" and "Healthy life expectancy at birth," measure social and health-related factors that affect overall quality of life. Additionally, the dataset includes metrics for individual freedoms, generosity, and perceptions of corruption, offering a comprehensive view of societal conditions. Data points on positive and negative affect also suggest an emphasis on emotional well-being. Overall, this dataset can be useful for analyzing the interplay of economic, social, and psychological factors influencing happiness across different global contexts.
## Data Overview
### Summary Statistics
| Stat | year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 2363.000 | 2363.000 | 2335.000 | 2350.000 | 2300.000 | 2327.000 | 2282.000 | 2238.000 | 2339.000 | 2347.000 |
| mean | 2014.764 | 5.484 | 9.400 | 0.809 | 63.402 | 0.750 | 0.000 | 0.744 | 0.652 | 0.273 |
| std | 5.059 | 1.126 | 1.152 | 0.121 | 6.843 | 0.139 | 0.161 | 0.185 | 0.106 | 0.087 |
| min | 2005.000 | 1.281 | 5.527 | 0.228 | 6.720 | 0.228 | -0.340 | 0.035 | 0.179 | 0.083 |
| 25% | 2011.000 | 4.647 | 8.506 | 0.744 | 59.195 | 0.661 | -0.112 | 0.687 | 0.572 | 0.209 |
| 50% | 2015.000 | 5.449 | 9.503 | 0.835 | 65.100 | 0.771 | -0.022 | 0.798 | 0.663 | 0.262 |
| 75% | 2019.000 | 6.324 | 10.393 | 0.904 | 68.552 | 0.862 | 0.094 | 0.868 | 0.737 | 0.326 |
| max | 2023.000 | 8.019 | 11.676 | 0.987 | 74.600 | 0.985 | 0.700 | 0.983 | 0.884 | 0.705 |

### Missing Values
| Column | Missing Count | Missing Percentage (%) |
|--------|------------|----------------------|
| Country name | 0.0 | 0.00 |
| year | 0.0 | 0.00 |
| Life Ladder | 0.0 | 0.00 |
| Log GDP per capita | 28.0 | 1.18 |
| Social support | 13.0 | 0.55 |
| Healthy life expectancy at birth | 63.0 | 2.67 |
| Freedom to make life choices | 36.0 | 1.52 |
| Generosity | 81.0 | 3.43 |
| Perceptions of corruption | 125.0 | 5.29 |
| Positive affect | 24.0 | 1.02 |
| Negative affect | 16.0 | 0.68 |

Duplicate Rows: 0
## Outliers
|Column|Outlier Count|
|-------|-------|
|year|0|
|Life Ladder|2|
|Log GDP per capita|1|
|Social support|48|
|Healthy life expectancy at birth|20|
|Freedom to make life choices|16|
|Generosity|39|
|Perceptions of corruption|194|
|Positive affect|9|
|Negative affect|31|
<div style="display: flex; flex-wrap: wrap; width: 120%;">
<img src="outliers_1.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
<img src="outliers_2.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
<img src="outliers_3.png" width="80%" style="margin-right: 10px; margin-bottom: 10px"/>
</div>
 
## Correlation Heatmap

![alt_text](correlation_heatmap.png)
## Data Story
In examining the dataset from the years 2005 to 2023, we uncover interesting insights into the factors that contribute to the overall well-being and happiness of individuals across various nations. The average Life Ladder score, indicative of individuals' self-reported life satisfaction, hovers around 5.48 on a scale that ranges from 1 to 10. This suggests that while a majority of people report a moderate level of happiness, there's substantial room for improvement, particularly as we observe the maximum score reaching 8.02.

We see a steady increase in the Life Ladder scores over the years, with the median year being 2015. This upward trend may correlate with economic factors, as reflected in the Log GDP per capita statistic, which has an average value of 9.4. However, the variability in GDP, indicated by a standard deviation of approximately 1.15, demonstrates that some nations experience significantly higher levels of economic prosperity than others.

Social support emerges as another critical factor, boasting an average of 0.81 on a scale from 0 to 1, showing that many individuals feel a strong connection and support from their communities. This is pivotal, considering that social connections are known to enhance life satisfaction. The maximum reported level of social support is close to 1, highlighting areas where communities excel in providing support.

Additionally, the dataset reveals that freedom to make life choices averages around 0.75. Most individuals feel a degree of autonomy in making choices that affect their lives, although a significant minority may still struggle with constraints in their decision-making.

While positive affect, averaging 0.65, suggests that individuals generally experience happiness and positivity, the presence of negative affect scores, averaging 0.27, implies that a notable portion of the population also faces anxiety and stress. The perception of corruption, averaging 0.74, reflects how citizens view transparency and integrity within their governments, which can significantly impact overall trust and satisfaction.

Interesting to note is the factor of generosity, which shows a mean close to zero, indicating that while some individuals are extremely generous, others may feel constrained in their means to give. 

As we explore the relationship between these various factors, the data sheds light on the complex tapestry of human well-being. While economic and social factors play crucial roles, enhancing social support systems and reducing perceptions of corruption could lead us toward a brighter, more fulfilling future for individuals around the world.
