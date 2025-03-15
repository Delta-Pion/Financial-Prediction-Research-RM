## **What is a Stock Split?**

A stock split is a corporate action where a company increases the number of outstanding shares of its stock by dividing each existing share into multiple shares.  Think of it like cutting a pie into more slices – the pie itself (the company's value) doesn't change, but you have more, smaller pieces.

* **N to 1 Split (Forward Split):**  This is the most common type.  "N to 1" means for every 1 share you previously owned, you now own N shares.  `N` is usually a whole number greater than 1 (like 2, 3, 4, etc.).
    * **Example: 2-for-1 Split (N=2):** If you owned 100 shares of a stock trading at $100 per share, after a 2-for-1 split, you would own 200 shares, and the price per share would ideally adjust to around $50. The total value of your holding should remain roughly the same (100 shares * $100 = $10,000  becomes 200 shares * $50 = $10,000).

* **Fractional Splits (N can be a decimal > 1 or < 1):** Sometimes, splits are expressed as fractions (e.g., 1.5 to 1, or 0.5 to 1 for reverse splits).

* **Reverse Split (N < 1):**  When N is smaller than 1 (like 0.5, 1/3, etc.), it's called a reverse stock split. This is the opposite of a forward split.  The company reduces the number of outstanding shares by combining multiple shares into fewer shares.
    * **Example: 1-for-2 Reverse Split (N=0.5, or better expressed as 1/2):** If you owned 200 shares at $50 per share, after a 1-for-2 reverse split, you would own 100 shares, and the price per share would ideally adjust to around $100. Again, the total value remains approximately the same. Reverse splits are often done by companies whose stock price has fallen too low, to increase the price per share, sometimes to avoid delisting from exchanges or to improve investor perception.

### **What is the Ex-Date (T)?**

The **ex-date (ex-dividend date)** is crucial for stock splits (and also for dividends). It's the date that determines who is entitled to the benefits of the stock split.

* **If you buy shares *before* the ex-date:** You *are entitled* to receive the shares from the stock split.
* **If you buy shares *on or after* the ex-date:** You will *not* receive the shares from the stock split. The seller of the shares (the previous owner before the ex-date) is entitled to the split shares.

**Why Adjust Historical Prices Before the Ex-Date?**

Without adjusting historical prices, stock charts would show a sudden, artificial drop (for forward splits) or jump (for reverse splits) on the ex-date. This is misleading because the fundamental value of the company hasn't actually changed in a dramatic way on that single day due to the split itself.

**The Adjustment: Multiply Prices Before T by 1/N**

To create a consistent and comparable historical price series, we need to adjust the older prices *before* the ex-date (T) to reflect the split's effect *as if it had happened in the past*.

The adjustment factor is **1/N**.

* **Forward Split (N > 1):**  We multiply historical prices by a fraction (less than 1), effectively *reducing* the historical prices.
    * For a 2-for-1 split (N=2), we multiply historical prices by 1/2 = 0.5.
    * For a 3-for-1 split (N=3), we multiply historical prices by 1/3 = 0.333…

* **Reverse Split (N < 1):**  We multiply historical prices by a number greater than 1, effectively *increasing* the historical prices.
    * For a 1-for-2 reverse split (N=0.5), we multiply historical prices by 1/0.5 = 2.
    * For a 1-for-3 reverse split (N=1/3 or approximately 0.333), we multiply historical prices by 1/(1/3) = 3.

**Example to illustrate:**

Let's say Company XYZ had a 2-for-1 stock split (N=2) with an ex-date of January 15th, 2024.

* **Raw, Unadjusted Stock Prices:**
    * January 14th, 2024 (before ex-date): Closing price = $100
    * January 15th, 2024 (ex-date):  Opening price might be around $50 (due to the split).

    If you plot these prices directly, you'd see a huge drop from $100 to $50 on Jan 15th.  This looks like a massive value loss, but it's just the split effect.

* **Adjusted Stock Prices (multiplying prices before Jan 15th by 1/N = 1/2 = 0.5):**
    * January 14th, 2024 (adjusted): $100 * 0.5 = $50
    * January 15th, 2024 (and onwards, no adjustment needed since these prices already reflect the split):  Opening price around $50

    Now, when you plot the adjusted prices, the chart will be continuous around the split date.  You can compare prices before and after the split meaningfully because they are on a like-for-like basis in terms of share count.

**In summary, this statement is telling you:**

To properly analyze historical stock price data and visualize price movements, you must adjust historical prices *before* a stock split's ex-date. The adjustment is done by multiplying those pre-split prices by the reciprocal of the split ratio (1/N). This ensures that historical charts accurately reflect the underlying value changes of the stock, undistorted by artificial price jumps or drops caused by stock splits.