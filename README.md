# Macro-Sentiment Options Strategy Dashboard

An interactive financial analytics dashboard that synthesizes macroeconomic conditions, market sentiment, and central bank communication signals to simulate and visualize options trading strategies under realistic risk assumptions.

---

## Project Overview

This project brings together economic regimes, NLP-driven sentiment analysis, and options backtesting into a single interactive dashboard. It's designed for risk teams, quants, and portfolio managers who want to explore how market context influences strategy performance.

---

## Project Structure

```
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── exploration/
│   └── modeling/
├── src/
│   ├── data_pipeline/
│   ├── models/
│   └── dashboard/
├── tests/
├── README.md
```

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/options-dashboard.git
cd options-dashboard
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up API keys**

Create a `.env` file and include:

```
FRED_API_KEY=your_key
BEA_API_KEY=optional_key
```

---

## Features

- **Macro Regime Classification** (KMeans on FRED data)
- **Sentiment Engine** (X/Twitter & News NLP w/ FinBERT + influence scoring)
- **FOMC Decoder** (Custom Hawkish/Dovish classifier)
- **Strategy Simulator** (Backtrader engine w/ OCO orders & volatility sizing)
- **Interactive Dashboard** (Streamlit or Dash)

---

## Example Usage

```bash
streamlit run src/dashboard/app.py
```

Navigate tabs to view:
- Regime timelines
- FOMC tone classifier output
- Sentiment overlays
- Trade simulation with performance metrics

---

## Model Details

| Module | Model | Notes |
|--------|-------|-------|
| Macro Regime | KMeans or HDBSCAN | Point-in-time ALFRED data |
| Sentiment | FinBERT + weight index | Weighted by influence, smoothed |
| FOMC | DistilRoBERTa fine-tuned | Custom labels, 3-class |
| Strategy | Rule-based | Driven by macro × sentiment |

---

## Tests

```bash
pytest tests/
```

---

## License

MIT License. Educational and demonstration use.

---

## Creator

Built by Chris DeWitt as part of a professional portfolio to showcase quantitative modeling, data synthesis, and application in financial strategy.
