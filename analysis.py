import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

august = pd.read_csv("aug_sales.csv")

september = pd.read_csv("sep_sales.csv")


august = august.rename(columns={
    "client_name": "customer",
    "county": "region",
    "qty": "quantity",
    "unit_price": "price"
})

september = september.rename(columns={
    "customer_name": "customer"
})

august["month"] = "August"

september["month"] = "September"

combined = pd.concat([august, september], ignore_index=True)
combined["total_revenue"] = combined["quantity"] * combined["price"]

# Transform - Revenue category

def tier(rev):
    if rev >= 300000: return "High"
    elif rev >=200000: return "Medium"
    else: return "Low"

monthly_revenue = combined.groupby(["month", "customer"])["total_revenue"].sum().reset_index()

monthly_revenue["tier"] = monthly_revenue["total_revenue"].apply(tier)
print("---======----")
print(monthly_revenue["tier"].value_counts())
print("-------------")

pivot = monthly_revenue.pivot(index="customer", columns="month", values="total_revenue").fillna(0)
pivot["growth"] = pivot["September"] - pivot["August"]
pivot["pct_change"] = ((pivot["September"] - pivot["August"]) / pivot["August"] * 100).round(1)
print(pivot.sort_values("pct_change", ascending=False).head(5))

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Chart 1: Revenue by region
region_rev = combined.groupby("region")["total_revenue"].sum().sort_values(ascending=False)
region_rev.plot(kind="bar", ax=axes[0], color="#1F4E79")
axes[0].set_title("Revenue by Region (Aug-Sep)")

# Chart 2: Month-over-month comparison
monthly = monthly_revenue.groupby("month")["total_revenue"].sum()
monthly.plot(kind="bar", ax=axes[1], color=["#1F4E79", "#4472C4"])
axes[1].set_title("Revenue: August vs September")

# Chart 3: Customer tier distribution
monthly_revenue["tier"].value_counts().plot(kind="pie", ax=axes[2], autopct="%.0f%%")
axes[2].set_title("Customer Revenue Tiers")

os.makedirs("charts", exist_ok=True)
plt.tight_layout()
plt.savefig("charts/project_analysis.png", dpi=150)
print("Charts saved.")