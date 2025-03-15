# Are the Data Split and Dividend Adjusted?
## Definitions : 
- [[Stock Splitting]]
- [[Dividend Adjustment]]

>[!info]+ Historical Databases For Backtesting
>![[Screenshot 2025-03-15 222113.png]]

***I recommend getting historical data that are already split and***
***dividend adjusted, because otherwise you would have to find a***
***separate historical database (such as earnings.com) of splits and***
***dividends and apply the adjustments yourself, a somewhat tedious and error-prone task***

# Are the Data Survivorship Bias Free?
## same as given [[Identifying Strategies#Does the Data Suffer from Survivorship Bias?|here]]
# Does Your Strategy Use High and Low Data?
For almost all daily stock data, the high and low prices are far noisier than the open and close prices. 

What this means is that even when you had placed a buy limit order below the recorded high of a day, it might not have been filled, and vice versa for a sell limit order. (This
could be due to the fact that a very small order was transacted at the high, or the execution could have occurred on a market to which your order was not routed. 

Sometimes, the high or low is simply due to an incorrectly reported tick that was not filtered out.) Hence, a back test that relies on high and low data is less reliable than one
that relies on the open and close.

>[!note]+
>After retrieving the data from a database, it is often advisable to
do a quick error check. The simplest way to do this is to calculate
the daily returns based on the data. If you have open, high, low, and
close prices, you can calculate the various combinations of daily
returns such as from the previous high to today’s close as well. You
can then examine closely those days with returns that are, say, 4
standard deviations away from the average. <mark style="background: #FF5582A6;">Typically, an extreme return should be accompanied by a news announcement, or should occur on a day when the market index also experienced extreme returns. If not, then your data is suspect.</mark>

# PERFORMANCE MEASUREMENT
1. [[Basic Terms#Information ratio or Sharpe ratio|Sharpe Ratio]]
2. Annualized Sharpe Ratio :
	- $$
\text{Annualized Sharpe Ratio} = \sqrt{ N_{T} } \times \text{Sharpe Ratio based on T}
$$

## Example 
For example, if your strategy holds positions only during the NYSE
market hours (9:30–16:00 ET), and the average hourly returns is R,
and the standard deviation of the hourly returns is s, then the annualized Sharpe ratio is
√1638 × R/s. This is because NT = (252 trading days) × (6.5 trading hours per trading day) = 1,638. (A common mistake is to compute NT as 252 × 24 = 6,048.)

## Example
![[Screenshot 2025-03-15 233823.png]]
![[Screenshot 2025-03-15 233839.png]]
![[Screenshot 2025-03-15 233859.png]]
![[Screenshot 2025-03-15 233914.png]]
![[Screenshot 2025-03-15 234445.png]]
![[Screenshot 2025-03-15 234522.png]]