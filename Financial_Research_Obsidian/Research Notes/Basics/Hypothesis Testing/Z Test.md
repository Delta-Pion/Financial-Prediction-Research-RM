A z test is a way of hypothesis testing that is used for a large sample size (n ≥ 30). It is used to determine whether there is a difference between the population mean and the sample mean when the population standard deviation is known. It can also be used to compare the mean of two samples. It is used to compute the z test statistic. The formulas are given as follows:

$$
\text{z} = \frac{\bar{x} - \mu }{\frac{\sigma}{\sqrt{ n }}}
$$
where $\bar{x}$ is the sample mean and $\mu$ is the population mean $\sigma$ is the population standard deviation and n is the size of sample

## For two samples : 
$$
\text{z} = \frac{(\bar{x_{1}}- \bar{x_{2}}) - (\mu_{1} - \mu_{2})}{\sqrt{ \frac{\sigma _{1}^2}{n_{1}} +  \frac{\sigma_{2}^2}{n_{2}}}}
$$
# Example
###### Worked Example - One Sample _z_-test

Research for a campaign to increase mental health awareness is being carried out. Using data from all GP practices across the U.K., the number of patients suffering from depression as a percentage of all patients over the past 15

years was recorded. The mean was found to be 21.9% and the standard deviation was found to be 7.5%. In the Liverpool area, data from 35 GP practices was collected, and the proportion of patients diagnosed with depression was recorded for the past fifteen years. The mean was found to be 26.2%

**How would we decide if the proportion of people suffering from depression is different in the Liverpool area than the national average?**

###### Solution

This is an example of a [one sample z](https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/psychology/parametric-hypothesis-tests.html#z-tests_-_Population_variance_known)[-test](https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/psychology/parametric-hypothesis-tests.html#z-tests_-_Population_variance_known), since we know the population mean, μ=21.9, and the population standard deviation, σ=7.5. We also have a sample size of 35 > 30, so we could use the sample standard deviation in our calculations. However, we know the population standard deviation, so we shall use it in our calculations.

Our hypotheses are: H0:μ=21.9H1:μ≠21.9

So the null hypothesis is that the proportion of people suffering from depression in the Liverpool area is no different from the proportion in the U.K. Whereas the alternative hypothesis is that the proportion of people suffering from depression in the Liverpool area differs from the U.K. average. We have a [two tailed test](https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/psychology/introduction-to-hypothesis-testing.html#One_and_Two_Tailed_Tests) here.

Now we need to calculate our test statistic.

z= 26.2−21.9  √7.5235  =4.3 √1.6071 =3.39 (2 d.p.).

We compare this to our critical values at the α significance level (we use z1−α/2 values, since it is a two-tailed test).

Since our z-value of 3.39 is greater than 2.58, 'It has been found that the proportion of people suffering from depression in Liverpool (¯X=26.2%) is different to the national average (¯X=21.9%). (z=3.39,p<0.01).'