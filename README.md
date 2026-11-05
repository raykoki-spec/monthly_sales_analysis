# File: README.md

#   Sales Multi-Dataset Analysis

This Python script cleans and merges sales data frame two datasets(august_sales, september_sales) into one dataframe.
Then, it applies logic to analyze revenue across various region, comparing September to August sales.


## What It Does

- Loads and combines sales datasets of two months
- Cleans the dataset by standardizing column names
- Applies logic to transform sales data into three categories(High, Medium, Low)
- Plots three charts fir visual representation of sales data
- Saves the charts as PNG in one folder(charts)


## Findings Summary

Nairobi recorded highest revenue compared to other regions. 
There was reduction in sales in September, compared to August.
Majority of customers fall in the Low category


## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the program from the project's folder

```
python analysis.py
```

## How it Works

```python
combined = pd.concat([august, september], ignore_index=True)

combined["total_revenue"] = combined["quantity"] * combined["price"]

monthly_revenue = combined.groupby(["month", "customer"])["total_revenue"].sum().reset_index()

print(monthly_revenue["tier"].value_counts())
```

## Sample Output

```
month     August  September  growth  pct_change
customer                                       
Mark       92900     124500   31600        34.0
Felix     327950     329650    1700         0.5
Oliver    249000     239600   -9400        -3.8
Joel      271800     197500  -74300       -27.3
Mike      177900     107250  -70650       -39.7
Charts saved.
```

## Stack
Python, Pandas, Numpy, Matplotlib, OS

