# News Sentiment Stock Analysis

A comprehensive project for analyzing correlations between financial news sentiment and stock price movements, developed for the 10 Academy AI Mastery Week 1 Challenge.

## Project Overview

This project focuses on detailed analysis of financial news data to discover correlations between news sentiment and stock market movements. The analysis covers:

1. **Exploratory Data Analysis (EDA)** - Understanding the financial news dataset
2. **Technical Indicators** - Calculating financial metrics using TA-Lib and PyNance
3. **Sentiment Analysis** - Analyzing news headline sentiment using NLP
4. **Correlation Analysis** - Measuring relationships between sentiment and stock returns

## Business Objective

Nova Financial Solutions aims to enhance predictive analytics capabilities by:
- Performing sentiment analysis on financial news headlines
- Establishing statistical correlations between news sentiment and stock price movements
- Providing actionable investment strategies based on sentiment analysis

## Project Structure

```
├── .vscode/
│   └── settings.json          # VS Code settings
├── .github/
│   └── workflows
│       └── unittests.yml      # CI/CD pipeline
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── src/
│   └── __init__.py           # Source package
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   ├── 01_eda.ipynb          # EDA analysis
│   ├── 02_technical_indicators.ipynb  # Technical indicators
│   ├── 03_sentiment_analysis.ipynb    # Sentiment analysis
│   └── 04_correlation_analysis.ipynb  # Correlation analysis
├── reports/
│   ├── interim_report.md      # Interim submission (3 pages)
│   ├── final_report.md        # Final submission (10 pages)
│   ├── figures/              # Visualization images
│   └── README.md             # Report guidelines
├── tests/
│   └── __init__.py           # Test package
└── scripts/
    ├── __init__.py
    ├── README.md
    ├── download_data.py       # Data download utilities
    ├── preprocess_data.py     # Data cleaning
    ├── calculate_indicators.py # Technical indicators
    ├── sentiment_analysis.py  # Sentiment analysis
    └── correlation_analysis.py # Correlation analysis
```

## Dataset

The project uses the **Financial News and Stock Price Integration Dataset (FNSPID)** with the following structure:

- **headline**: Article release headline
- **url**: Direct link to the full news article
- **publisher**: Author/creator of article
- **date**: Publication date and time (UTC-4 timezone)
- **stock**: Stock ticker symbol (e.g., AAPL for Apple)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd news-sentiment-stock-analysis
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: TA-Lib installation may require additional steps:
- Windows: Download wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib)
- Linux/Mac: `brew install ta-lib` then `pip install TA-Lib`

### 4. Download NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('brown')
```

## Usage

### Task 1: Exploratory Data Analysis

1. Place your news data file in a `data/` directory
2. Open `notebooks/01_eda.ipynb`
3. Update the data path and run all cells

The EDA covers:
- Descriptive statistics (headline lengths, article counts)
- Publisher analysis
- Time series analysis (publication frequency, time patterns)
- Text analysis (keyword extraction, topic modeling)
- Stock symbol analysis

### Task 2: Technical Indicators

1. Use `scripts/download_data.py` to download stock price data
2. Open `notebooks/02_technical_indicators.ipynb`
3. Calculate indicators using `scripts/calculate_indicators.py`

Indicators calculated:
- Moving Averages (SMA, EMA)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Stochastic Oscillator
- ATR (Average True Range)
- OBV (On Balance Volume)

### Task 3: Sentiment Analysis & Correlation

1. Run sentiment analysis using `scripts/sentiment_analysis.py`
2. Open `notebooks/03_sentiment_analysis.ipynb` for detailed analysis
3. Use `scripts/correlation_analysis.py` to calculate correlations
4. Open `notebooks/04_correlation_analysis.ipynb` for visualization

## Key Features

### Data Processing
- Automated data cleaning and preprocessing
- Date alignment between news and stock data
- Handling missing values and outliers

### Sentiment Analysis
- Polarity scoring (-1 to 1)
- Subjectivity measurement
- Sentiment classification (positive/negative/neutral)

### Technical Analysis
- Multiple technical indicators
- Visualization of indicators
- Integration with stock price data

### Correlation Analysis
- Pearson and Spearman correlations
- Statistical significance testing
- Time series alignment
- Daily aggregation of sentiment scores

## Development Workflow

### Git Branches

- `main`: Production-ready code
- `task-1`: EDA and data understanding
- `task-2`: Technical indicators implementation
- `task-3`: Sentiment and correlation analysis

### Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Adding tests

### Running Tests

```bash
pytest tests/ -v --cov=src
```

## Dependencies

### Core Libraries
- `pandas`: Data manipulation
- `numpy`: Numerical computing
- `matplotlib`, `seaborn`: Visualization

### Financial Analysis
- `yfinance`: Stock price data
- `pynance`: Financial metrics
- `TA-Lib`: Technical indicators

### NLP
- `nltk`: Natural language processing
- `textblob`: Sentiment analysis

### Statistical Analysis
- `scipy`: Statistical functions
- `scikit-learn`: Machine learning utilities

## Deliverables

### Interim Submission (Sunday, 23 Nov 2025)
- GitHub link to main branch
- Interim report (max 3 pages) - See `reports/interim_report.md`
- Task 1 completion + partial Task 2

### Final Submission (Tuesday, 25 Nov 2025)
- GitHub link to main branch
- Final report (up to 10 pages, max 10 plots) - See `reports/final_report.md`
- All tasks completed
- Publication-style Medium blog format

**Note:** Both report templates are provided in the `reports/` directory. Fill in placeholders with your actual analysis results. See `reports/REPORT_TEMPLATE_GUIDE.md` for detailed instructions.

## Learning Objectives

By completing this project, you will:

- ✅ Configure a reproducible Python data-science environment with GitHub
- ✅ Perform EDA on text and time series data
- ✅ Compute technical indicators using TA-Lib and PyNance
- ✅ Run sentiment analysis on news headlines with NLP tools
- ✅ Measure correlation between news sentiment and daily stock returns
- ✅ Document findings and write publication-style reports

## References

- [Stock Market Basics](https://www.investopedia.com/terms/s/stockmarket.asp)
- [TA-Lib Python](https://github.com/ta-lib/ta-lib-python)
- [PyNance](https://github.com/mqandil/pynance)
- [TextBlob Documentation](https://textblob.readthedocs.io/)

## Contributors

Developed for 10 Academy AI Mastery Week 1 Challenge.

## License

This project is for educational purposes as part of the 10 Academy program.

