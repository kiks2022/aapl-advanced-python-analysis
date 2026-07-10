# 🍎 Decoding AAPL: Five Years, One DataFrame, and a Lot of Volatility

> *What does it actually mean when a stock "goes up"? This project takes 1,254 trading days of Apple Inc. data and makes them confess everything — the trend, the tremors, and the days it just couldn't sit still.*

**AnalystLab Africa Internship · Batch B · Week 6 — Advanced Python Analysis**

---

## 📌 The 30-Second Version

Five years of AAPL's daily price action, put through a full data-science pipeline: cleaned, transformed, time-sliced, feature-engineered, and visualized. The goal wasn't just "make some charts" — it was to answer a real question: **does Apple's stock behave the way headlines say it does, or does the data tell a messier, more interesting story?**

Spoiler: it's messier. It's always messier.

| | |
|---|---|
| 📅 **Period covered** | Jul 12, 2021 → Jul 9, 2026 (1,254 trading days) |
| 💵 **Price range** | $125.02 → $316.22 |
| 📈 **Total return** | +118.8% |
| ⚡ **Wildest single day** | +15.33% |
| 😬 **Ugliest single day** | −9.25% |
| 🎲 **Odds a given day closes green** | 53% (basically a coin flip with a slight lean) |
| 📆 **Positive months** | 34 of 60 (56.7%) |

---

## 🧠 Why This Isn't Just "Line Goes Up"

Anyone can plot `Close` vs. `Date`. That's not analysis, that's tracing. This project goes further:

- **It cleans before it trusts.** Missing values get time-aware interpolation, not lazy mean-fills. Duplicate rows get evicted, not ignored.
- **It quantifies risk, not just price.** A 30-day rolling, annualized volatility feature reveals that AAPL doesn't drift calmly upward — it clusters into nervous stretches and quiet stretches, like most equities do.
- **It lets the moving averages argue with each other.** The 7-day MA reacts like caffeine. The 30-day MA responds like patience. Where they cross is where the story usually turns.
- **It doesn't average away the outliers.** A +15% day and a −9% day are two of the most important rows in this dataset — and they get treated that way, not diluted into a mean.

---

## 🔬 The Pipeline

```
Raw OHLCV data (yfinance)
        │
        ▼
🧹 Clean          → datetime parsing · duplicate removal · interpolation
        │
        ▼
🔧 Transform       → daily change · % change · range % · groupby/resample aggregation
        │
        ▼
⏱️ Time-Series     → 7/30/90-day rolling MAs · monthly/yearly resampling · cumulative return
        │
        ▼
🧬 Feature Engineer → annualized volatility · Bollinger-style bands · momentum · relative volume
        │
        ▼
📊 Visualize        → 6+ charts telling 6 different parts of the story
```

---

## 📊 What the Charts Actually Say

**Closing Price Trend** — the headline chart, but read alongside the others below, not alone.

**Moving Average Analysis (7/30-day)** — this is where the plot thickens. Watch how tightly the 7-day MA hugs the raw price versus how the 30-day MA smooths distinct multi-quarter regimes: the 2022 slide, the 2023–24 climb, a sharp 2025 air-pocket, and the 2026 push toward highs. Crossovers here roughly mark where sentiment actually flipped.

**Trading Volume Trend** — volume doesn't move randomly. The tallest spikes on this chart line up with the sharpest price moves elsewhere in the dataset — the market voting with size, not just sentiment.

**Monthly Returns** — the honest chart. Twelve-plus percent up months sit right next to double-digit down months. This is the chart that kills the "steady growth stock" myth — Apple's monthly returns look more like a heartbeat than a staircase.

**Rolling Volatility** — risk isn't constant, and this proves it. Calm plateaus get interrupted by sharp volatility spikes that don't always coincide with the biggest price moves — sometimes the *fear* of a move is louder than the move itself.

**Daily Returns Distribution** — the shape here is the tell: a tall peak near zero with long, thin tails reaching toward the +15% and −9% extremes. Most days are boring. A handful of days do all the work.

---

## 🧩 Repo Structure

```
├── AAPL_Advanced_Analysis.ipynb     # the full notebook — run top to bottom
├── AAPL.csv                          # raw 5-year OHLCV data
├── AAPL_Engineered.csv               # cleaned + feature-engineered dataset
├── AAPL_Insight_Summary.docx         # 2-page written findings & recommendations
├── images/
│   ├── Closing_Price_Trend.png
│   ├── Trading_Volume_Trend.png
│   ├── Moving_Average_Analysis.png
│   ├── Monthly_Returns.png
│   ├── Rolling_Volatility.png
│   └── Daily_Returns_Distribution.png
└── README.md
```

---

## ⚙️ Run It Yourself

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
pip install pandas numpy matplotlib yfinance
jupyter notebook AAPL_Advanced_Analysis.ipynb
```

Or open it straight in Colab and hit **Run All** — the notebook re-pulls fresh AAPL data via `yfinance` on execution, so your numbers will drift slightly from the ones above as new trading days roll in. That's not a bug. That's the market still talking.

---

## 🛠️ Built With

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `yfinance` · a healthy suspicion of any stock chart that looks *too* smooth.

---

## 🎯 Key Takeaway

Apple's 5-year chart looks like a growth story from a distance. Zoom in, and it's really a **volatility story with a growth trend riding on top of it** — regime shifts, volume-confirmed swings, and a small number of extreme days quietly doing most of the heavy lifting on total return. Trend-following without a volatility lens is reading half the book.

---

*Part of the AnalystLab Africa Internship Program — Batch B, Week 6: Advanced Python Analysis.*
`#Python` `#DataAnalysis` `#TimeSeriesAnalysis` `#Pandas` `#DataScience` `#Analytics` `#AnalystLabAfrica`
