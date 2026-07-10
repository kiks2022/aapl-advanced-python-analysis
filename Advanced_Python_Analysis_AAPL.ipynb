# ============================================================
# WEEK 6 INTERNSHIP TASK
# Advanced Python Analysis using Apple (AAPL) Stock Data
# AnalystLab Africa - Batch B
# ============================================================

# ===============================
# 1. Mount Google Drive FIRST
# ===============================
from google.colab import drive
drive.mount('/content/drive')

# ===============================
# 2. Download Real AAPL Data
# ===============================
!pip install yfinance openpyxl --quiet
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

%matplotlib inline
plt.rcParams["figure.figsize"] = (14, 6)

# auto_adjust=False keeps the separate 'Adj Close' column
df = yf.download("AAPL", period="5y", auto_adjust=False)

# yfinance sometimes returns MultiIndex columns even for one ticker — flatten if so
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.reset_index()  # turns the Date index into a normal column before saving

output_folder = "/content/drive/MyDrive/Colab Notebooks/Advanced Python Analysis"
output_path = f"{output_folder}/AAPL.csv"
df.to_csv(output_path, index=False)
print("Dataset saved successfully!")
display(df.head())

# ===============================
# 3. Load Dataset (clean, single-header CSV)
# ===============================
df = pd.read_csv(output_path)

print("First Five Rows")
display(df.head())

# ===============================
# 4. Explore Dataset
# ===============================
print("Dataset Shape:", df.shape)
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
display(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# ===============================
# 5. Data Cleaning
# ===============================
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").drop_duplicates(subset="Date", keep="first")
df.set_index("Date", inplace=True)

df.ffill(inplace=True)
df.bfill(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ===============================
# 6. Data Transformation
# ===============================
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Month_Name"] = df.index.month_name()
df["Day"] = df.index.day_name()

high_price = df[df["Close"] > 150]
print("\nDays where Closing Price > 150")
display(high_price.head())

monthly_average = df.groupby(["Year", "Month"])["Close"].mean()
print("\nMonthly Average Closing Price")
display(monthly_average.head())

# ===============================
# 7. Feature Engineering
# ===============================
df["Daily Price Change"] = df["Close"] - df["Open"]
df["Daily % Change"] = df["Close"].pct_change() * 100
df["High-Low Spread"] = df["High"] - df["Low"]
df["MA_7"] = df["Close"].rolling(window=7).mean()
df["MA_30"] = df["Close"].rolling(window=30).mean()
df["Volatility"] = df["Daily % Change"].rolling(window=30).std()

monthly_returns = df["Close"].resample("ME").last().pct_change() * 100
monthly_close = df["Close"].resample("ME").mean()

# ===============================
# 8. Time Series Analysis
# ===============================
print("\nHighest Closing Price:", round(df["Close"].max(), 2))
print("Lowest Closing Price:", round(df["Close"].min(), 2))
print("Average Closing Price:", round(df["Close"].mean(), 2))
print("Highest Trading Volume:", int(df["Volume"].max()))
print("Average Trading Volume:", round(df["Volume"].mean(), 2))

# ===============================
# 9-15. Visualizations (inline, for review in the notebook)
# ===============================
plt.figure(figsize=(15,6))
plt.plot(df.index, df["Close"])
plt.title("Apple Closing Price Trend"); plt.xlabel("Date"); plt.ylabel("Closing Price ($)")
plt.grid(True); plt.show()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Volume"])
plt.title("Trading Volume Trend"); plt.xlabel("Date"); plt.ylabel("Trading Volume")
plt.grid(True); plt.show()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Close"], label="Closing Price")
plt.plot(df.index, df["MA_7"], label="7-Day MA")
plt.plot(df.index, df["MA_30"], label="30-Day MA")
plt.legend(); plt.title("Moving Average Analysis"); plt.xlabel("Date"); plt.ylabel("Price")
plt.grid(True); plt.show()

plt.figure(figsize=(15,6))
plt.plot(monthly_returns.index, monthly_returns.values)
plt.title("Monthly Returns"); plt.xlabel("Month"); plt.ylabel("Return (%)")
plt.grid(True); plt.show()

plt.figure(figsize=(10,6))
plt.hist(df["Daily % Change"].dropna(), bins=50)
plt.title("Distribution of Daily Percentage Returns"); plt.xlabel("Daily Return (%)"); plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Volatility"])
plt.title("30-Day Rolling Volatility"); plt.xlabel("Date"); plt.ylabel("Volatility")
plt.grid(True); plt.show()

plt.figure(figsize=(15,6))
plt.plot(monthly_close.index, monthly_close.values)
plt.title("Average Monthly Closing Price"); plt.xlabel("Month"); plt.ylabel("Average Closing Price")
plt.grid(True); plt.show()

# ===============================
# 16. Display Engineered Dataset
# ===============================
print("Engineered Dataset")
display(df.head())

# ===============================
# 17. Summary Statistics
# ===============================
print("="*60)
print("SUMMARY OF ANALYSIS")
print("="*60)
print(f"Highest Closing Price: {df['Close'].max():.2f}")
print(f"Lowest Closing Price: {df['Close'].min():.2f}")
print(f"Average Closing Price: {df['Close'].mean():.2f}")
print(f"Highest Trading Volume: {df['Volume'].max():,.0f}")
print(f"Average Trading Volume: {df['Volume'].mean():,.0f}")
print(f"Highest Daily Return: {df['Daily % Change'].max():.2f}%")
print(f"Lowest Daily Return: {df['Daily % Change'].min():.2f}%")

# ===============================
# 18. Key Findings
# ===============================
print(f"""
==============================
KEY FINDINGS
==============================

1. AAPL moved from ${df['Close'].iloc[0]:.2f} to ${df['Close'].iloc[-1]:.2f} over the period,
   a cumulative return of {(df['Close'].iloc[-1]/df['Close'].iloc[0]-1)*100:.1f}%.

2. Average daily volume was {df['Volume'].mean():,.0f} shares, peaking at
   {df['Volume'].max():,.0f} shares on the busiest trading day.

3. The 7-Day MA tracks short-term swings closely, while the 30-Day MA
   smooths those swings to reveal the underlying trend.

4. Daily returns ranged from {df['Daily % Change'].min():.2f}% to
   {df['Daily % Change'].max():.2f}%, showing the scale of single-day volatility.

5. Rolling 30-day volatility varied over time, spiking during clearly
   identifiable higher-uncertainty stretches rather than staying constant.

6. Monthly returns were positive in {(monthly_returns>0).sum()} of
   {monthly_returns.count()} months.

==============================
END OF ANALYSIS
==============================
""")

# ============================================================
# 19. SAVE ALL TABLES AND CHARTS (each with its own real name)
# ============================================================

# ----------------------------
# SAVE TABLES
# ----------------------------
df.to_csv(f"{output_folder}/AAPL_Engineered.csv")
df.to_excel(f"{output_folder}/AAPL_Engineered.xlsx")
monthly_average.to_csv(f"{output_folder}/Monthly_Average_Closing_Price.csv")
monthly_returns.to_csv(f"{output_folder}/Monthly_Returns.csv")
high_price.to_csv(f"{output_folder}/High_Closing_Prices.csv")

summary = pd.DataFrame({
    "Metric": [
        "Highest Closing Price", "Lowest Closing Price", "Average Closing Price",
        "Highest Trading Volume", "Average Trading Volume",
        "Highest Daily Return", "Lowest Daily Return"
    ],
    "Value": [
        df["Close"].max(), df["Close"].min(), df["Close"].mean(),
        df["Volume"].max(), df["Volume"].mean(),
        df["Daily % Change"].max(), df["Daily % Change"].min()
    ]
})
summary.to_csv(f"{output_folder}/Summary_Statistics.csv", index=False)

# ----------------------------
# SAVE CHARTS
# ----------------------------
plt.figure(figsize=(15,6))
plt.plot(df.index, df["Close"])
plt.title("Apple Closing Price Trend"); plt.xlabel("Date"); plt.ylabel("Closing Price ($)")
plt.grid(True)
plt.savefig(f"{output_folder}/Closing_Price_Trend.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Volume"])
plt.title("Trading Volume Trend"); plt.xlabel("Date"); plt.ylabel("Trading Volume")
plt.grid(True)
plt.savefig(f"{output_folder}/Trading_Volume_Trend.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["MA_7"], label="7-Day MA")
plt.plot(df.index, df["MA_30"], label="30-Day MA")
plt.legend(); plt.title("Moving Average Analysis"); plt.xlabel("Date"); plt.ylabel("Price")
plt.grid(True)
plt.savefig(f"{output_folder}/Moving_Average_Analysis.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(15,6))
plt.plot(monthly_returns.index, monthly_returns.values)
plt.title("Monthly Returns"); plt.xlabel("Month"); plt.ylabel("Return (%)")
plt.grid(True)
plt.savefig(f"{output_folder}/Monthly_Returns.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(10,6))
plt.hist(df["Daily % Change"].dropna(), bins=50)
plt.title("Distribution of Daily Percentage Returns"); plt.xlabel("Daily Return (%)"); plt.ylabel("Frequency")
plt.savefig(f"{output_folder}/Daily_Returns_Distribution.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(15,6))
plt.plot(df.index, df["Volatility"])
plt.title("30-Day Rolling Volatility"); plt.xlabel("Date"); plt.ylabel("Volatility")
plt.grid(True)
plt.savefig(f"{output_folder}/Rolling_Volatility.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(15,6))
plt.plot(monthly_close.index, monthly_close.values)
plt.title("Average Monthly Closing Price"); plt.xlabel("Month"); plt.ylabel("Average Closing Price")
plt.grid(True)
plt.savefig(f"{output_folder}/Average_Monthly_Closing_Price.png", dpi=300, bbox_inches="tight")
plt.close()

# ----------------------------
# SHOW SAVED FILES
# ----------------------------
print("="*60)
print("FILES SAVED SUCCESSFULLY")
print("="*60)
for file in sorted(os.listdir(output_folder)):
    print(file)

print("\nAll tables and charts have been saved successfully.")
