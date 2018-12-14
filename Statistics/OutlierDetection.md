# Basic outlier detection method: by looking at quantiles

## Outlier Detection by Box Plot
Suppose we're given the data samples of a variable X, the most common way of detecting outlier of X is to use a boxplot. 
More specifically, the boxplot is showing the quantiles of X and the definition of outlier is as follows:\
First quartile of X: Q1. \
Third quartile of X: Q3. \
Interquartile range (IQR): Q3-Q1, then IQR will cover the middle 50\% of the observations.\
Lower limit: Q1 - 1.5 * IQR. \
Upper limit: Q3 + 1.5 * IQR. \
Any point falling outside the range is defined as an outlier.

## Outlier Detection if X is Normal Distributed
If X is normally distributed, then it's symmetric about the mean.\
For the standard normal distribution the first quartile is -0.67 and the third quartile is 0.67. This means that for normally distributed data, one-half of the data is within 2/3 of a standard deviation unit of the mean.\
If we follow the above definition of outlier, since the quartiles for the standard normal distribution are +/-0.67, the IQR = 1.34.\
Lower limit: Q1 - 1.5*IQR = - 0.67 - 1.5 * 1.34 = -2.68.\
Similarly, upper limit: Q3 + 1.5 * IQR = 2.68.\
Then for any normally distributed data X,
any observations falling outside of [mean(x) - 2.68 * sd(x), mean(x) + 2.68 * sd(x)] are considered outliers.
