# Appendices

---

## Appendix A: Python Quick Reference

This appendix provides a quick reference for the Python libraries and patterns used most frequently in time‑series prediction systems. It is not a comprehensive tutorial but a reminder of essential syntax and common operations.

### A.1 pandas Essentials

pandas is the workhorse for time‑series data manipulation in Python.

**Creating a DataFrame**

```python
import pandas as pd

# From dictionary
df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02'],
    'close': [100.5, 102.3]
})

# From list of lists
data = [['2023-01-01', 100.5], ['2023-01-02', 102.3]]
df = pd.DataFrame(data, columns=['date', 'close'])

# From CSV
df = pd.read_csv('nepse_data.csv', parse_dates=['date'])
```

**Handling Dates**

```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Set as index
df = df.set_index('date')

# Resample to different frequency (e.g., weekly)
df_weekly = df.resample('W').mean()

# Extract components
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['dayofweek'] = df.index.dayofweek  # Monday=0
```

**Selecting Data**

```python
# By label
df.loc['2023-01-01']

# By integer position
df.iloc[0]

# Boolean indexing
df[df['close'] > 101]

# Query method
df.query('close > 101 and volume > 1000')
```

**Missing Values**

```python
# Check for missing
df.isnull().sum()

# Drop rows with any missing
df.dropna()

# Fill forward (carry last known value)
df.fillna(method='ffill')

# Fill with a specific value
df.fillna(0)
```

**Rolling Windows**

```python
# 7-day rolling mean
df['sma_7'] = df['close'].rolling(window=7).mean()

# 7-day rolling standard deviation
df['volatility_7'] = df['close'].rolling(window=7).std()

# Expanding window (cumulative)
df['expanding_mean'] = df['close'].expanding().mean()
```

**Grouping**

```python
# Group by symbol and compute mean close
df.groupby('symbol')['close'].mean()

# Apply multiple functions
df.groupby('symbol')['close'].agg(['mean', 'std', 'min', 'max'])

# Transform (add group mean as new column)
df['symbol_mean'] = df.groupby('symbol')['close'].transform('mean')
```

**Merging and Joining**

```python
# Concatenate rows
combined = pd.concat([df1, df2], axis=0)

# Merge on columns (like SQL join)
merged = pd.merge(df1, df2, on='date', how='inner')

# Join on index
joined = df1.join(df2, lsuffix='_left', rsuffix='_right')
```

### A.2 NumPy Operations

NumPy provides fast array operations.

**Creating Arrays**

```python
import numpy as np

# From list
arr = np.array([1, 2, 3])

# Zeros, ones
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))

# Range
arr = np.arange(0, 10, 2)  # [0,2,4,6,8]

# Random numbers
np.random.seed(42)
rand = np.random.rand(5)        # uniform [0,1]
randn = np.random.randn(5)      # standard normal
randint = np.random.randint(0, 10, size=5)
```

**Indexing and Slicing**

```python
arr = np.array([10, 20, 30, 40])
arr[1]        # 20
arr[1:3]      # [20,30]
arr[[0,2]]    # [10,30]

# 2D array
mat = np.array([[1,2],[3,4]])
mat[0,1]      # 2
mat[:,0]      # first column [1,3]
```

**Universal Functions (ufuncs)**

```python
np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.abs(arr)
```

**Linear Algebra**

```python
# Dot product
np.dot(a, b)

# Matrix multiplication (Python 3.5+)
a @ b

# Transpose
a.T

# Inverse
np.linalg.inv(a)

# Eigenvalues
np.linalg.eig(a)
```

**Statistics**

```python
np.mean(arr)
np.std(arr)
np.var(arr)
np.percentile(arr, 75)
np.corrcoef(x, y)
```

### A.3 Scikit‑learn API

Scikit‑learn provides a consistent interface for machine learning.

**Train/Test Split (with time‑series caution!)**

```python
from sklearn.model_selection import train_test_split

# For non‑time‑series, random split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# For time‑series, use temporal split
split_idx = int(len(X) * 0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]
```

**Preprocessing**

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # use same scaler
```

**Model Training**

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

**Evaluation**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

**Cross‑Validation for Time‑Series**

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
    # train model...
```

**Hyperparameter Tuning**

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'n_estimators': [50, 100], 'max_depth': [5, 10]}
grid = GridSearchCV(RandomForestRegressor(), param_grid, cv=tscv)
grid.fit(X, y)
best_model = grid.best_estimator_
```

### A.4 Common Patterns

**Pipeline**

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor())
])
pipeline.fit(X_train, y_train)
```

**Feature Engineering with pandas and NumPy**

```python
# Lag features
for lag in [1, 2, 3]:
    df[f'lag_{lag}'] = df['close'].shift(lag)

# Rolling features
df['rolling_mean_7'] = df['close'].rolling(7).mean()
df['rolling_std_7'] = df['close'].rolling(7).std()

# Date features
df['dayofweek'] = df.index.dayofweek
df['month'] = df.index.month
df['quarter'] = df.index.quarter
```

**Saving and Loading Models**

```python
import joblib

joblib.dump(model, 'model.pkl')
model = joblib.load('model.pkl')
```

### A.5 Code Templates

**Template for a Feature Engineering Function**

```python
def engineer_features(df):
    """
    Add time‑series features to a DataFrame.
    Assumes df has a DatetimeIndex and a 'close' column.
    """
    df = df.copy()
    
    # Lag features
    for lag in [1, 2, 3, 5, 10]:
        df[f'close_lag_{lag}'] = df['close'].shift(lag)
    
    # Rolling statistics
    for window in [7, 14, 30]:
        df[f'close_rolling_mean_{window}'] = df['close'].rolling(window).mean()
        df[f'close_rolling_std_{window}'] = df['close'].rolling(window).std()
    
    # Date features
    df['dayofweek'] = df.index.dayofweek
    df['month'] = df.index.month
    
    # Drop rows with NaN
    df = df.dropna()
    
    return df
```

**Template for a Training Script**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load and prepare data
df = pd.read_csv('data.csv', parse_dates=['date'], index_col='date')
df = engineer_features(df)

# Define features and target
feature_cols = [c for c in df.columns if 'close' in c or 'day' in c]
X = df[feature_cols]
y = df['close'].shift(-1).dropna()
X = X.iloc[:-1]  # align

# Time‑based split
split = int(0.8 * len(X))
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

# Train
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'MAE: {mae:.2f}')

# Save
joblib.dump(model, 'model.pkl')
```

**Template for a Prediction API (FastAPI)**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()
model = joblib.load('model.pkl')
feature_cols = joblib.load('feature_cols.pkl')  # saved list

class PredictionRequest(BaseModel):
    features: dict  # e.g., {'lag_1': 105.2, 'lag_2': 106.1, ...}

class PredictionResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    # Convert to DataFrame (one row)
    df = pd.DataFrame([request.features])
    # Ensure columns are in the right order
    X = df[feature_cols]
    pred = model.predict(X)[0]
    return PredictionResponse(prediction=pred)
```

---

## Appendix B: Mathematical Foundations

This appendix summarises the essential mathematical concepts used throughout the handbook. It is intended as a refresher, not a full textbook.

### B.1 Statistics Review

**Descriptive Statistics**

- **Mean**: μ = (1/n) ∑ xᵢ
- **Variance**: σ² = (1/n) ∑ (xᵢ – μ)²
- **Standard deviation**: σ = √(σ²)
- **Correlation**: ρ(X,Y) = Cov(X,Y) / (σ_X σ_Y)

**Probability Distributions**

- **Normal (Gaussian)**: f(x) = (1/√(2πσ²)) exp(–(x–μ)²/(2σ²))
- **t‑distribution**: used in small‑sample inference
- **Chi‑squared**: used in goodness‑of‑fit tests
- **F‑distribution**: used in ANOVA

**Hypothesis Testing**

- **Null hypothesis H₀**, alternative H₁
- **p‑value**: probability of observing the data (or more extreme) if H₀ is true
- **Type I error**: rejecting true H₀ (false positive)
- **Type II error**: failing to reject false H₀ (false negative)

**Time‑Series Specific**

- **Autocorrelation**: correlation of a series with its lagged self
- **Stationarity**: a series whose statistical properties (mean, variance, autocorrelation) are constant over time
- **White noise**: a series with zero mean, constant variance, and no autocorrelation

### B.2 Linear Algebra Basics

**Vectors and Matrices**

- **Vector**: an ordered list of numbers
- **Matrix**: a 2‑D array of numbers
- **Transpose**: A^T (swap rows and columns)
- **Dot product**: a·b = ∑ aᵢ bᵢ

**Matrix Operations**

- **Addition**: A + B (element‑wise)
- **Multiplication**: A B (if A is m×n and B is n×p)
- **Inverse**: A⁻¹ exists if A is square and invertible (det ≠ 0)
- **Determinant**: det(A) – a scalar measure of volume scaling
- **Eigenvalues and eigenvectors**: A v = λ v (λ scalar, v vector)

**Special Matrices**

- **Identity matrix I**: 1s on diagonal, 0s elsewhere
- **Diagonal matrix**: non‑zero only on diagonal
- **Symmetric matrix**: A = A^T
- **Positive definite matrix**: x^T A x > 0 for all non‑zero x

**Use in ML**

- Data matrices: rows = samples, columns = features
- Covariance matrix: Σ = (1/n) (X – μ)^T (X – μ)
- Principal Component Analysis (PCA): eigendecomposition of covariance matrix

### B.3 Calculus for ML

**Derivatives**

- Derivative of f(x) at x: f'(x) = lim_{h→0} (f(x+h) – f(x))/h
- Partial derivative: ∂f/∂xᵢ (for functions of multiple variables)
- Gradient: ∇f = vector of partial derivatives
- Chain rule: (f∘g)'(x) = f'(g(x)) g'(x)

**Optimisation**

- **Gradient descent**: θ ← θ – η ∇L(θ) (η = learning rate)
- **Stochastic gradient descent (SGD)** : use one sample at a time
- **Momentum**: incorporate past gradients to smooth updates
- **Adam**: adaptive learning rate method

**Integrals**

- Definite integral: ∫_a^b f(x) dx = area under curve
- Expected value: E[X] = ∫ x f(x) dx for continuous X

### B.4 Probability Theory

**Basic Rules**

- **Conditional probability**: P(A|B) = P(A∩B) / P(B)
- **Bayes' theorem**: P(A|B) = P(B|A) P(A) / P(B)
- **Law of total probability**: P(A) = ∑ P(A|Bᵢ) P(Bᵢ)

**Random Variables**

- **Discrete**: takes countable values (e.g., Poisson)
- **Continuous**: takes any value in an interval (e.g., Normal)
- **Expected value**: E[X] = ∑ x P(X=x) (discrete) or ∫ x f(x) dx (continuous)
- **Variance**: Var(X) = E[(X – μ)²] = E[X²] – (E[X])²
- **Covariance**: Cov(X,Y) = E[(X – μ_X)(Y – μ_Y)]

**Important Distributions**

- **Bernoulli**: coin flip (0 or 1)
- **Binomial**: number of successes in n trials
- **Poisson**: number of events in fixed interval
- **Normal**: bell‑shaped, central limit theorem
- **Exponential**: waiting times

### B.5 Optimisation Theory

**Unconstrained Optimisation**

- Find x that minimises f(x)
- Necessary condition: ∇f(x*) = 0 (stationary point)
- Sufficient condition: Hessian ∇²f(x*) positive definite

**Constrained Optimisation**

- **Lagrange multipliers**: minimise f(x) subject to g(x)=0 → ∇f = λ ∇g
- **KKT conditions**: for inequality constraints

**Convexity**

- A function is convex if f(θx + (1–θ)y) ≤ θ f(x) + (1–θ) f(y) for θ∈[0,1]
- Convex functions have no local minima; any local minimum is global
- Many ML problems are non‑convex (e.g., neural networks)

---

## Appendix C: Data Resources

This appendix lists publicly available time‑series datasets and APIs that can be used for learning and experimentation.

### C.1 Public Datasets

**Finance**

- **Yahoo Finance** (via `yfinance`): stock prices, dividends, splits
- **Alpha Vantage**: free API for stock, forex, crypto data
- **Quandl** (now Nasdaq Data Link): economic and financial data
- **NEPSE** (Nepal Stock Exchange): official site provides daily reports (CSV)
- **Kaggle Datasets**: search "stock market", "finance"

**Retail and E‑Commerce**

- **UCI Machine Learning Repository**: Online Retail, Instacart Market Basket Analysis
- **Kaggle**: M5 Forecasting, Walmart Sales, Rossmann Store Sales

**Weather and Climate**

- **NOAA** (National Oceanic and Atmospheric Administration): global weather data
- **ECMWF** (European Centre for Medium‑Range Weather Forecasts): reanalysis data
- **OpenWeatherMap**: API for current and forecast weather

**Energy**

- **PJM** (Pennsylvania‑New Jersey‑Maryland Interconnection): hourly load data
- **ENTSO‑E** (European Network of Transmission System Operators): electricity data
- **UCI**: Individual household electric power consumption

**IoT and Sensors**

- **UCI**: Gas sensor array, Activity Recognition from Single Chest‑Mounted Accelerometer
- **NASA** Prognostics Data Repository: turbofan engine degradation data

**Healthcare**

- **MIMIC‑III** (Medical Information Mart for Intensive Care): requires training and access
- **UCI**: Heart Disease, Diabetes, Epileptic Seizure Recognition

### C.2 Data Providers

- **FRED** (Federal Reserve Economic Data): macroeconomic indicators
- **World Bank Open Data**: global development data
- **IMF Data**: international financial statistics
- **Google Trends**: search interest over time
- **Twitter API**: social media sentiment (requires developer account)

### C.3 API Documentation

- **Yahoo Finance**: `yfinance` Python library
- **Alpha Vantage**: [alphavantage.co](https://www.alphavantage.co)
- **Twelve Data**: [twelvedata.com](https://twelvedata.com)
- **IEX Cloud**: stock market data
- **CoinGecko**: cryptocurrency data

### C.4 Data Quality Checklist

Before using any dataset, verify:

- [ ] Date range covers the period of interest
- [ ] No missing values in critical columns (or handle appropriately)
- [ ] Consistent frequency (e.g., daily data every weekday)
- [ ] No duplicate rows
- [ ] Values are within plausible ranges (e.g., prices positive)
- [ ] Metadata available (data dictionary)

### C.5 Data Licensing

Always check the license:

- **Public domain**: free to use for any purpose
- **Creative Commons**: may require attribution
- **Commercial**: may require payment for commercial use
- **Research only**: cannot be used for commercial products

---

## Appendix D: Model Zoo

This appendix catalogs the model architectures, pre‑trained models, and algorithms referenced in the handbook.

### D.1 Pre‑trained Models

**Time‑Series Foundation Models**

| Model | Source | Description |
|-------|--------|-------------|
| Chronos | Amazon | Pre‑trained transformer for forecasting; available on Hugging Face |
| Lag‑Llama | University of Oxford | Decoder‑only foundation model for probabilistic forecasting |
| Moirai | Salesforce | Multivariate foundation model with masked pre‑training |
| TimesFM | Google | Decoder‑only foundation model for time‑series |

**LLMs for Time‑Series (via prompting)**

- GPT‑4 (OpenAI)
- Claude (Anthropic)
- Llama (Meta)

### D.2 Model Architectures

**Statistical**

- ARIMA (Autoregressive Integrated Moving Average)
- SARIMA (Seasonal ARIMA)
- ETS (Error, Trend, Seasonal) – exponential smoothing
- VAR (Vector Autoregression) – multivariate
- GARCH (Generalized Autoregressive Conditional Heteroskedasticity) – volatility

**Tree‑Based**

- Decision Trees
- Random Forest
- Gradient Boosting Machines (GBM)
- XGBoost
- LightGBM
- CatBoost

**Linear Models**

- Linear Regression
- Ridge, Lasso, Elastic Net
- Logistic Regression (classification)

**Support Vector Machines**

- SVM (Support Vector Machine) for classification
- SVR (Support Vector Regression)

**Neural Networks**

- MLP (Multi‑Layer Perceptron)
- RNN (Recurrent Neural Network)
- LSTM (Long Short‑Term Memory)
- GRU (Gated Recurrent Unit)
- CNN (Convolutional Neural Network) for time‑series (1D)
- Transformer (self‑attention)
- N‑BEATS (Neural Basis Expansion Analysis for Time Series)
- DeepAR (Amazon) – probabilistic forecasting

**Ensemble and Hybrid**

- Stacking
- Blending
- Model routing / mixture of experts

### D.3 Model Weights

Pre‑trained weights for deep learning models are typically hosted on:

- **Hugging Face Hub**: [huggingface.co/models](https://huggingface.co/models)
- **TensorFlow Hub**: [tfhub.dev](https://tfhub.dev)
- **PyTorch Hub**: [pytorch.org/hub](https://pytorch.org/hub)

For time‑series, search for "time series", "forecasting", "chronos", etc.

### D.4 Usage Examples

**Loading Chronos from Hugging Face**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("amazon/chronos-t5-small")
tokenizer = AutoTokenizer.from_pretrained("amazon/chronos-t5-small")
```

**Using XGBoost**

```python
import xgboost as xgb
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
model.fit(X_train, y_train)
```

### D.5 Performance Benchmarks

| Dataset | Best Model (as of 2024) | Typical MAE/RMSE |
|---------|-------------------------|------------------|
| M4 (monthly) | ES‑RNN / Theta | sMAPE ~11.5 |
| Electricity | N‑BEATS / Transformer | RMSE ~0.05 (normalised) |
| Traffic | Graph Wavenet | MAE ~18 |
| NEPSE (example) | XGBoost with features | MAE ~12 (depends on period) |

*Note: Benchmarks vary; always test on your own data.*

---

## Appendix E: Tool and Library Reference

### E.1 Data Libraries

| Library | Purpose | Installation |
|---------|---------|--------------|
| `pandas` | Data manipulation and analysis | `pip install pandas` |
| `numpy` | Numerical computing | `pip install numpy` |
| `scipy` | Scientific computing (stats, optimisation) | `pip install scipy` |
| `polars` | Fast DataFrame library (alternative to pandas) | `pip install polars` |
| `pyspark` | Distributed data processing | `pip install pyspark` |
| `dask` | Parallel computing with pandas‑like API | `pip install dask[complete]` |
| `ray` | Distributed execution | `pip install ray` |

### E.2 ML Libraries

| Library | Purpose | Installation |
|---------|---------|--------------|
| `scikit-learn` | Classical ML algorithms, preprocessing | `pip install scikit-learn` |
| `xgboost` | Gradient boosting | `pip install xgboost` |
| `lightgbm` | Lightweight gradient boosting | `pip install lightgbm` |
| `catboost` | Gradient boosting with categorical support | `pip install catboost` |
| `statsmodels` | Statistical models (ARIMA, VAR, etc.) | `pip install statsmodels` |
| `pmdarima` | Auto‑ARIMA | `pip install pmdarima` |
| `sktime` | Time‑series specific ML | `pip install sktime` |
| `darts` | Time‑series forecasting library | `pip install darts` |
| `tsfresh` | Automatic feature extraction | `pip install tsfresh` |
| `featuretools` | Automated feature engineering | `pip install featuretools` |

### E.3 Deep Learning Frameworks

| Framework | Purpose | Installation |
|-----------|---------|--------------|
| `tensorflow` | Deep learning | `pip install tensorflow` |
| `torch` (PyTorch) | Deep learning | `pip install torch` |
| `jax` | High‑performance numerical computing | `pip install jax jaxlib` |
| `keras` | High‑level API (part of TF) | `pip install keras` |
| `pytorch-lightning` | PyTorch wrapper | `pip install pytorch-lightning` |
| `transformers` | Hugging Face transformers | `pip install transformers` |

### E.4 MLOps Tools

| Tool | Purpose | Installation / Access |
|------|---------|----------------------|
| `mlflow` | Experiment tracking, model registry | `pip install mlflow` |
| `wandb` (Weights & Biases) | Experiment tracking | `pip install wandb` |
| `dvc` (Data Version Control) | Version data and models | `pip install dvc` |
| `apache-airflow` | Workflow orchestration | `pip install apache-airflow` |
| `prefect` | Workflow orchestration | `pip install prefect` |
| `kubeflow` | ML workflows on Kubernetes | Platform‑specific |
| `seldon-core` | Model serving on Kubernetes | `helm install` |
| `bentoml` | Model serving | `pip install bentoml` |
| `fastapi` | REST API framework | `pip install fastapi uvicorn` |
| `prometheus_client` | Metrics exposition | `pip install prometheus_client` |
| `grafana` | Dashboarding | Download from grafana.com |

### E.5 Cloud Services

| Provider | ML Service | Description |
|----------|------------|-------------|
| AWS | SageMaker | End‑to‑end ML platform |
| GCP | Vertex AI | Unified ML platform |
| Azure | Machine Learning | Cloud ML service |
| Databricks | Unified Data Analytics | Spark‑based platform |
| Snowflake | Data Cloud | Data warehousing with ML capabilities |

### E.6 Comparison Tables

**Time‑Series Forecasting Libraries**

| Library | Models | Probabilistic | Deep Learning | Ease of Use |
|---------|--------|---------------|----------------|-------------|
| `statsmodels` | ARIMA, ETS, VAR | No | No | Medium |
| `pmdarima` | Auto‑ARIMA | No | No | Easy |
| `sktime` | Many (ARIMA, TBATS, etc.) | Some | Via wrappers | Medium |
| `darts` | Many (incl. TFT, N‑BEATS) | Yes | Yes | Easy |
| `prophet` | Additive seasonality | Yes | No | Easy |
| `neuralforecast` | Deep learning (RNN, TFT) | Yes | Yes | Medium |

**MLflow vs. Weights & Biases**

| Feature | MLflow | Weights & Biases |
|---------|--------|------------------|
| Open source | Yes | No (but free tier) |
| Experiment tracking | Yes | Yes |
| Model registry | Yes | Yes |
| Hyperparameter tuning | Limited | Yes (sweeps) |
| Collaboration | Via tracking server | Built‑in |
| Artifact storage | Local or S3 | Cloud |

---

## Appendix F: Troubleshooting Guide

This appendix catalogs common issues encountered in time‑series prediction systems and provides diagnostic steps and solutions.

### F.1 Common Data Issues

**Issue: Missing values in critical columns**

- **Symptoms**: Model training fails; predictions are NaN.
- **Check**: `df.isnull().sum()`.
- **Solutions**: Impute (forward fill, mean, interpolation) or drop rows. Ensure imputation method respects time order.

**Issue: Duplicate rows (same symbol, same date)**

- **Symptoms**: Model performance inconsistent; unexpected duplicates in aggregations.
- **Check**: `df.duplicated(subset=['symbol','date']).sum()`.
- **Solutions**: Drop duplicates, keeping last: `df.drop_duplicates(subset=['symbol','date'], keep='last')`.

**Issue: Outliers (extreme values)**

- **Symptoms**: Model predictions are unrealistic; scaling is distorted.
- **Check**: `df.describe()`, plot histograms.
- **Solutions**: Cap values (winsorization), remove if clearly erroneous, or use robust scaling.

**Issue: Data not sorted by date**

- **Symptoms**: Lag features incorrect; rolling windows produce wrong values.
- **Check**: `df.index.is_monotonic_increasing`.
- **Solutions**: `df.sort_index(inplace=True)`.

**Issue: Incorrect date parsing**

- **Symptoms**: Dates appear as strings; resampling fails.
- **Check**: `df['date'].dtype`.
- **Solutions**: `df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')`.

### F.2 Model Training Problems

**Issue: Model fails to converge (high loss)**

- **Symptoms**: Loss flat or increasing; predictions constant.
- **Checks**: Learning rate too high/low; data not scaled; architecture too complex.
- **Solutions**: Reduce learning rate, use learning rate schedules, check gradients (exploding/vanishing), simplify model.

**Issue: Overfitting (training loss much lower than validation loss)**

- **Symptoms**: High validation error despite low training error.
- **Checks**: Monitor loss curves; check model complexity.
- **Solutions**: Regularisation (L1/L2), dropout, early stopping, reduce model size, get more data.

**Issue: Underfitting (both training and validation loss high)**

- **Symptoms**: Model too simple; cannot capture patterns.
- **Checks**: Loss curves plateau at high value.
- **Solutions**: Increase model capacity, add features, reduce regularisation, try different algorithm.

**Issue: Data leakage (performance too good to be true)**

- **Symptoms**: Validation accuracy > 95% on a hard problem; backtesting shows unrealistic profits.
- **Checks**: Verify that all features use only past information (e.g., `shift()` used correctly); ensure train/test split respects time order.
- **Solutions**: Re‑engineer features with proper temporal alignment; use walk‑forward validation.

**Issue: Inconsistent results across runs**

- **Symptoms**: Model performance varies widely with same hyperparameters.
- **Checks**: Random seeds not set; non‑deterministic algorithms.
- **Solutions**: Set `random_state` in all estimators; use `np.random.seed(42)`; for deep learning, set `torch.manual_seed(42)` and `tf.random.set_seed(42)`.

### F.3 Deployment Challenges

**Issue: Prediction service returns 500 errors**

- **Symptoms**: API calls fail.
- **Checks**: Check service logs; verify model file exists and is loaded correctly; check input data format.
- **Solutions**: Fix exception (e.g., missing feature, type error). Add better error handling.

**Issue: High latency**

- **Symptoms**: API response time > expected.
- **Checks**: Profile code; check if model inference is the bottleneck; check database queries.
- **Solutions**: Cache model in memory; use batch predictions; optimise feature computation; scale horizontally.

**Issue: Model drift in production**

- **Symptoms**: Prediction error increases over time.
- **Checks**: Monitor error metrics; compare feature distributions with training.
- **Solutions**: Set up automated retraining; trigger alerts on drift.

### F.4 Performance Issues

**Issue: Slow feature engineering**

- **Symptoms**: Pipeline takes hours.
- **Checks**: Profile code (cProfile); identify bottlenecks (e.g., row‑wise loops).
- **Solutions**: Vectorise operations; use NumPy/pandas built‑ins; parallelise with Dask or multiprocessing.

**Issue: Memory exhaustion**

- **Symptoms**: Process crashes with MemoryError.
- **Checks**: Monitor memory usage; check data size.
- **Solutions**: Process in chunks; use more efficient data types (e.g., `float32`); use Dask for out‑of‑core computation.

**Issue: Slow model training**

- **Symptoms**: Training takes days.
- **Checks**: Hardware utilisation (CPU/GPU); algorithm complexity.
- **Solutions**: Use GPU if applicable; reduce dataset size (sample); use simpler model; early stopping.

### F.5 Debugging Techniques

**1. Print statements**: Insert `print()` to check variable values at key points.

**2. Logging**: Use `logging` module with different levels (DEBUG, INFO, WARNING, ERROR).

**3. Assertions**: `assert condition, "message"` to catch invalid states early.

**4. Interactive debugging**: Insert `breakpoint()` to start pdb session.

**5. Visualisation**: Plot data, predictions, residuals to spot patterns.

**6. Unit tests**: Write tests for individual functions to isolate issues.

**7. Git bisect**: If a bug appeared after a change, use `git bisect` to find the offending commit.

### F.6 Error Messages

| Error | Likely Cause | Solution |
|-------|--------------|----------|
| `ValueError: cannot reindex from a duplicate axis` | Duplicate index values | `df = df[~df.index.duplicated(keep='first')]` |
| `KeyError: 'column_name'` | Column not found | Check spelling; list columns with `df.columns` |
| `TypeError: 'float' object is not subscriptable` | Trying to index a float (e.g., `x[i]` where x is float) | Check variable type; ensure it's list/array |
| `MemoryError` | Data too large for RAM | Use chunking; reduce dtype precision; use Dask |
| `AttributeError: 'NoneType' object has no attribute 'fit'` | Model object not created | Ensure model class instantiated correctly |
| `ModuleNotFoundError` | Missing library | `pip install library_name` |

### F.7 Solutions Database

For quick reference, keep a team wiki of past issues and their resolutions. Example entry:

```
Issue: XGBoost training slow with large categorical features
Solution: Use `enable_categorical=True` and ensure categories are pandas Categorical type.
```

---

## Appendix G: Checklists

This appendix provides checklists for each phase of a time‑series prediction project. Use them to ensure nothing is overlooked.

### G.1 Data Collection Checklist

- [ ] Data sources identified and access confirmed
- [ ] Data frequency understood (daily, hourly, etc.)
- [ ] Historical data period covers at least 2‑3 full cycles (e.g., years) if possible
- [ ] Data format consistent (CSV, Parquet, etc.)
- [ ] Missing value strategy defined (imputation, drop)
- [ ] Data quality checks automated (schema validation, range checks)
- [ ] Data versioning in place (e.g., DVC)
- [ ] Data storage location secured and backed up
- [ ] Data update frequency determined (daily, weekly)
- [ ] Data collection pipeline automated (Airflow, cron)

### G.2 Feature Engineering Checklist

- [ ] Date/time features extracted (hour, day, month, year, dayofweek)
- [ ] Cyclical features encoded (sin/cos for hour, dayofweek, month)
- [ ] Lag features created for relevant variables (1, 2, 3, 7, ...)
- [ ] Rolling window features computed (mean, std, min, max over windows)
- [ ] Technical indicators added (if applicable: RSI, MACD, Bollinger Bands)
- [ ] Domain‑specific features included (holidays, events, external data)
- [ ] Interaction features considered
- [ ] Features checked for look‑ahead bias (all `shift` used correctly)
- [ ] Features scaled appropriately (if needed by model)
- [ ] Feature store designed (online/offline)
- [ ] Feature engineering code tested with sample data

### G.3 Model Development Checklist

- [ ] Problem type defined (regression, classification, probabilistic)
- [ ] Evaluation metric(s) selected (MAE, RMSE, MAPE, etc.)
- [ ] Baseline model established (naïve forecast, historical average)
- [ ] Train/validation/test split respects time order
- [ ] Time‑series cross‑validation implemented (e.g., `TimeSeriesSplit`)
- [ ] Candidate models selected (statistical, tree‑based, deep learning)
- [ ] Hyperparameter tuning performed (grid search, Bayesian optimisation)
- [ ] Model ensembling considered
- [ ] Model performance compared to baseline
- [ ] Model interpretability tools applied (SHAP, feature importance)
- [ ] Model saved and versioned (MLflow, joblib)

### G.4 Model Evaluation Checklist

- [ ] Overall performance metrics computed on test set
- [ ] Performance evaluated across subgroups (sectors, time periods)
- [ ] Residuals analysed (normality, autocorrelation, heteroscedasticity)
- [ ] Backtesting performed with a realistic trading strategy (if applicable)
- [ ] Probabilistic forecast evaluation (CRPS, pinball loss) if applicable
- [ ] Model robustness tested under different market regimes
- [ ] Sensitivity analysis conducted (how much do predictions change with small input variations)

### G.5 Deployment Checklist

- [ ] Model exported to deployment format (`.pkl`, `.tflite`, ONNX)
- [ ] Prediction service designed (REST API, batch, streaming)
- [ ] Service containerised (Docker)
- [ ] Configuration externalised (environment variables, config files)
- [ ] Dependencies pinned (`requirements.txt` or `pyproject.toml`)
- [ ] Service deployed to staging environment
- [ ] Integration tests pass (end‑to‑end)
- [ ] Load testing performed (throughput, latency)
- [ ] Model caching strategy implemented (if needed)
- [ ] API documented (OpenAPI)
- [ ] Deployment orchestrated (Kubernetes, serverless)

### G.6 Monitoring Checklist

- [ ] Prediction logs enabled (request/response, timestamp, model version)
- [ ] Performance metrics tracked (MAE over time)
- [ ] Data drift detection set up (feature distributions)
- [ ] Concept drift detection (model error over time)
- [ ] System metrics monitored (CPU, memory, latency, error rate)
- [ ] Alerts configured for critical thresholds
- [ ] Dashboard created (Grafana, etc.)
- [ ] Incident response runbook documented

### G.7 Maintenance Checklist

- [ ] Model retraining schedule defined (e.g., weekly)
- [ ] Retraining pipeline automated
- [ ] Model registry used to manage versions
- [ ] A/B testing framework for model comparison
- [ ] Feedback loop from users incorporated
- [ ] Regular code refactoring and technical debt reduction
- [ ] Dependencies updated periodically
- [ ] Security patches applied
- [ ] Documentation reviewed and updated

---

## Appendix H: Templates

This appendix provides ready‑to‑use templates for common documents and code structures.

### H.1 Project Structure Template

```
project_name/
├── .github/               # GitHub Actions workflows
├── config/                # Configuration files (YAML, JSON)
├── data/
│   ├── raw/               # Immutable raw data
│   ├── processed/         # Cleaned, feature‑engineered data
│   └── external/          # External data sources
├── notebooks/             # Jupyter notebooks for exploration
├── src/
│   ├── __init__.py
│   ├── data/              # Data ingestion, validation
│   ├── features/          # Feature engineering
│   ├── models/            # Model definitions, training
│   ├── api/               # Prediction service (FastAPI)
│   └── utils/             # Helper functions
├── tests/                 # Unit and integration tests
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
├── models/                # Saved model files (git‑ignored)
├── reports/               # Generated analysis (PDF, HTML)
├── .gitignore
├── README.md
├── pyproject.toml         # Project dependencies (Poetry)
├── setup.py               # Alternative for pip
└── docker-compose.yml     # Local development services
```

### H.2 Code Template (Python Module)

```python
"""
Module docstring: describe what this module does.
"""

import logging
from typing import Optional, Union, List
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

class FeatureEngineer:
    """
    Class for feature engineering.
    """
    
    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
        self.feature_columns = []
    
    def compute_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Main feature engineering function.
        
        Args:
            df: Raw DataFrame with required columns.
        
        Returns:
            DataFrame with engineered features.
        """
        df = df.copy()
        # ... feature logic ...
        return df

def helper_function(param1: int, param2: str) -> bool:
    """
    Helper function description.
    """
    # ... implementation ...
    return True

if __name__ == "__main__":
    # Example usage when run as script
    pass
```

### H.3 Documentation Template (README.md)

```markdown
# Project Name

Brief description of the project.

## Installation

```bash
git clone https://github.com/yourorg/project.git
cd project
poetry install
```

## Usage

```python
from src import FeatureEngineer
# ...
```

## Documentation

See [docs/](docs/) for detailed documentation.

## Testing

Run tests with `pytest`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
```

### H.4 Model Card Template

```markdown
# Model Card: [Model Name]

## Model Details
- **Version**: 
- **Type**: 
- **Date trained**: 
- **Training data**: 
- **Features**: 
- **License**: 

## Intended Use
- 

## Factors
- 

## Metrics
- **Overall MAE**: 
- **Per‑group performance**: 

## Evaluation Data
- 

## Ethical Considerations
- 

## Caveats and Recommendations
- 
```

### H.5 API Specification Template (OpenAPI)

```yaml
openapi: 3.0.0
info:
  title: NEPSE Prediction API
  version: 1.0.0
paths:
  /predict:
    post:
      summary: Predict next day close price
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PredictionRequest'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PredictionResponse'
components:
  schemas:
    PredictionRequest:
      type: object
      properties:
        symbol:
          type: string
        date:
          type: string
          format: date
    PredictionResponse:
      type: object
      properties:
        symbol:
          type: string
        date:
          type: string
          format: date
        predicted_close:
          type: number
        model_version:
          type: string
```

### H.6 Deployment Plan Template

```
# Deployment Plan for [Release Version]

## Overview
- Date: 
- Services affected: 
- Estimated downtime: 

## Pre‑deployment Checklist
- [ ] All tests passed
- [ ] Model performance validated on hold‑out data
- [ ] Rollback plan documented
- [ ] Stakeholders notified

## Deployment Steps
1. 
2. 
3. 

## Post‑deployment Verification
- [ ] Smoke tests passed
- [ ] Metrics monitored for 1 hour
- [ ] Users confirmed functionality

## Rollback Plan
- If issue X occurs, run:
  ```
  kubectl rollout undo deployment/prediction-service
  ```
```

---

## Appendix I: Glossary

| Term | Definition |
|------|------------|
| **ARIMA** | Autoregressive Integrated Moving Average; a class of statistical models for time‑series forecasting. |
| **Autoencoder** | A neural network trained to reconstruct its input, used for anomaly detection and dimensionality reduction. |
| **Backtesting** | Evaluating a trading strategy on historical data to assess its performance. |
| **Bagging** | Bootstrap Aggregating; an ensemble method that trains multiple models on bootstrap samples and averages predictions. |
| **Bias (statistical)** | Systematic error in predictions, e.g., always under‑predicting. |
| **Bias (ethical)** | Unfair prejudice in model outcomes, e.g., performing worse for a particular group. |
| **Boosting** | An ensemble method that trains models sequentially, each focusing on the errors of the previous. |
| **Causal inference** | The process of drawing conclusions about causal relationships from data. |
| **Concept drift** | Change in the statistical properties of the target variable over time. |
| **Cross‑validation** | A technique for assessing model performance by partitioning the data into training and validation sets multiple times. |
| **Data leakage** | Using information from the future when training a model, leading to overly optimistic performance. |
| **Data parallelism** | Distributing data across multiple workers, each training a copy of the model. |
| **Differential privacy** | A framework for ensuring that a model does not reveal information about any individual in the training data. |
| **Distributed tracing** | Tracking a request as it flows through multiple services. |
| **Drift detection** | Monitoring for changes in data or model performance. |
| **Edge AI** | Running AI models on edge devices (near the data source) rather than in the cloud. |
| **Ensemble** | Combining multiple models to improve performance. |
| **Event‑driven architecture** | A software architecture where services communicate via events. |
| **Explainable AI (XAI)** | Techniques that make model predictions understandable to humans. |
| **Fairness metric** | A quantitative measure of bias (e.g., demographic parity, equal opportunity). |
| **Feature store** | A central repository for storing and serving features for training and inference. |
| **Foundation model** | A large pre‑trained model that can be adapted to many downstream tasks. |
| **Granger causality** | A statistical test for whether one time series helps predict another. |
| **Heteroscedasticity** | Non‑constant variance of errors over time. |
| **Hyperparameter** | A parameter set before training (e.g., learning rate, number of trees). |
| **Incremental learning** | Updating a model continuously as new data arrives (online learning). |
| **Interpretability** | The degree to which a human can understand the cause of a model's decision. |
| **Kernel method** | A technique for implicitly mapping data to a higher‑dimensional space, used in SVMs. |
| **Look‑ahead bias** | A form of data leakage where future information is used in features. |
| **Microservices** | An architectural style where an application is composed of loosely coupled, independently deployable services. |
| **MLOps** | Practices for deploying and maintaining machine learning models in production. |
| **Model card** | A document that describes a model's purpose, performance, and limitations. |
| **Model parallelism** | Distributing different parts of a model across multiple workers. |
| **Multicollinearity** | High correlation among predictor variables, which can destabilise linear models. |
| **Online learning** | See incremental learning. |
| **Outlier** | An observation that deviates significantly from other observations. |
| **Overfitting** | A model that learns the training data too well, including noise, and performs poorly on new data. |
| **p‑value** | The probability of obtaining test results at least as extreme as the observed results, under the null hypothesis. |
| **Prequential evaluation** | Test‑then‑train evaluation for streaming data. |
| **Probabilistic forecast** | A forecast that provides a probability distribution over possible outcomes. |
| **Pruning** | Removing less important weights from a neural network to reduce size. |
| **Quantization** | Reducing the numerical precision of a model's weights to reduce size and speed up inference. |
| **Quantum machine learning (QML)** | Using quantum computing to perform machine learning tasks. |
| **Reinforcement learning (RL)** | Learning a policy by interacting with an environment to maximise cumulative reward. |
| **Residual** | The difference between an observed value and a predicted value. |
| **Seasonality** | Regular patterns that repeat at fixed intervals (daily, weekly, yearly). |
| **SHAP (SHapley Additive exPlanations)** | A game‑theoretic approach to explain the output of any machine learning model. |
| **Stationarity** | A property of a time series where its statistical properties (mean, variance, autocorrelation) are constant over time. |
| **Symbolic regression** | Discovering mathematical expressions that fit a dataset. |
| **Technical debt** | The implied cost of additional rework caused by choosing an easy solution now instead of a better approach. |
| **TimeSeriesSplit** | A cross‑validation strategy that respects temporal order. |
| **TinyML** | Machine learning on ultra‑low‑power devices like microcontrollers. |
| **Transfer learning** | Using a pre‑trained model on a new, related task. |
| **Underfitting** | A model that is too simple to capture the underlying structure of the data. |
| **Variational quantum circuit (VQC)** | A parameterised quantum circuit trained by classical optimisation. |
| **Walk‑forward validation** | A backtesting method where the model is trained on an expanding window and tested on the next period. |
| **Zero‑shot forecasting** | Making forecasts with a foundation model without any fine‑tuning. |

---

## Appendix J: References and Further Reading

### J.1 Academic Papers

**Foundational Time‑Series**

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time Series Analysis: Forecasting and Control*. Wiley.
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice*. OTexts.

**Machine Learning for Time‑Series**

- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018). The M4 Competition: Results, findings, conclusion and way forward. *International Journal of Forecasting*, 34(4), 802‑808.
- Salinas, D., Flunkert, V., Gasthaus, J., & Januschowski, T. (2020). DeepAR: Probabilistic forecasting with autoregressive recurrent networks. *International Journal of Forecasting*, 36(3), 1181‑1191.
- Oreshkin, B. N., Carpov, D., Chapados, N., & Bengio, Y. (2020). N‑BEATS: Neural basis expansion analysis for interpretable time series forecasting. *International Conference on Learning Representations*.

**Transformers for Time‑Series**

- Wu, N., Green, B., Ben, X., & O'Banion, S. (2020). Deep Transformer models for time series forecasting: The influenza prevalence case. *arXiv preprint arXiv:2001.08317*.
- Lim, B., & Zohren, S. (2021). Time‑series forecasting with deep learning: a survey. *Philosophical Transactions of the Royal Society A*, 379(2194), 20200209.

**Foundation Models**

- Ansari, A. F., et al. (2024). Chronos: Learning the language of time series. *arXiv preprint arXiv:2403.07815*.
- Rasul, K., et al. (2023). Lag‑Llama: Towards foundation models for time series forecasting. *arXiv preprint arXiv:2310.08278*.
- Woo, G., et al. (2024). Moirai: A time series foundation model for universal forecasting. *arXiv preprint arXiv:2402.02592*.

**Causal Inference**

- Pearl, J. (2009). *Causality*. Cambridge University Press.
- Runge, J., et al. (2019). Detecting and quantifying causal associations in large nonlinear time series datasets. *Science Advances*, 5(11), eaau4996.

**Ethical AI**

- Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86‑92.
- Mitchell, M., et al. (2019). Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220‑229.

### J.2 Books

- Géron, A. (2022). *Hands‑On Machine Learning with Scikit‑Learn, Keras, and TensorFlow*. O'Reilly.
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (online).
- Molnar, C. (2022). *Interpretable Machine Learning*. Leanpub.

### J.3 Online Courses

- **Time Series Forecasting** by Kaggle (free)
- **Practical Time Series Analysis** by Coursera (University of Washington)
- **Deep Learning Specialization** (Sequence Models) by Coursera (deeplearning.ai)
- **MLOps Specialization** by Coursera (DeepLearning.AI)

### J.4 Blogs and Websites

- **Towards Data Science** (Medium): many practical tutorials
- **Machine Learning Mastery** by Jason Brownlee
- **InfluxData Blog**: time‑series database and analytics
- **AWS Machine Learning Blog**: case studies and how‑tos
- **Google AI Blog**: research updates

### J.5 Communities and Forums

- **Stack Overflow**: tag `time-series`
- **Cross Validated** (stats.stackexchange.com): statistical questions
- **Kaggle**: competitions and forums
- **Reddit** r/MachineLearning, r/datascience

### J.6 Conferences

- **NeurIPS** (Neural Information Processing Systems)
- **ICML** (International Conference on Machine Learning)
- **ICLR** (International Conference on Learning Representations)
- **KDD** (Knowledge Discovery and Data Mining)
- **IJCAI** (International Joint Conference on Artificial Intelligence)
- **IEEE Big Data**

### J.7 Standards and Specifications

- **OpenAPI** (swagger.io)
- **PEP 8** – Python Style Guide
- **PEP 484** – Type Hints
- **MLflow** Model Registry
- **ONNX** (Open Neural Network Exchange)

---

## Appendix K: Code Repository

This appendix describes the structure of the accompanying code repository for the handbook. The repository contains all code examples, from simple snippets to complete pipelines.

### K.1 Repository Structure

```
time-series-prediction-handbook/
├── README.md
├── requirements.txt           # Core dependencies
├── environment.yml             # Conda environment
├── .gitignore
├── chapter2/                  # Code for Chapter 2
│   ├── load_nepse_data.py
│   └── visualisation.py
├── chapter3/                   # Environment setup
├── ...
├── chapter10/                  # Feature engineering
│   ├── nepse_feature_engineer.py
│   └── test_features.py
├── chapter74/                  # Complete system
│   ├── ingestion.py
│   ├── feature_store.py
│   ├── train.py
│   ├── predict.py
│   └── docker/
├── chapter78/                  # IoT case study
│   ├── generate_sensor_data.py
│   ├── streaming_features.py
│   └── anomaly_detection.py
├── data/                       # Small sample datasets (git‑ignored in full)
│   └── nepse_sample.csv
├── notebooks/                  # Jupyter notebooks
│   ├── 02_EDA.ipynb
│   ├── 10_Feature_Engineering.ipynb
│   └── ...
└── utils/                      # Shared utilities
    ├── __init__.py
    └── metrics.py
```

### K.2 Code Organization

Each chapter's code is in its own folder. Key scripts are named descriptively. For large systems (e.g., Chapter 74), the code is organised into modules.

### K.3 Usage Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourorg/time-series-prediction-handbook.git
   cd time-series-prediction-handbook
   ```

2. Set up environment (choose one):
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Using conda
   conda env create -f environment.yml
   conda activate tsp-handbook
   ```

3. Run a script:
   ```bash
   python chapter10/nepse_feature_engineer.py
   ```

4. Launch notebooks:
   ```bash
   jupyter notebook
   ```

### K.4 Contribution Guidelines

We welcome contributions! Please:

- Fork the repository.
- Create a feature branch.
- Ensure code follows PEP 8 and includes tests.
- Submit a pull request with a clear description.

### K.5 License Information

The code is released under the MIT License. See `LICENSE` file for details.

---

## Appendix L: Index

*(This would be a comprehensive index with page numbers in a printed book. In this digital version, we provide a keyword list for search.)*

- A/B testing, 47
- Accountability, 87, 98
- ADWIN drift detector, 84
- Agile methodology, 88
- Airflow, 9, 41
- Alerting, 73
- Anomaly detection, 58, 78
- API documentation, 89
- ARIMA, 21, 76
- Autoencoder, 58, 78
- AutoML, 53, 99
- Backtesting, 33, 74, 75
- Bagging, 51, 83
- Batch prediction, 41, 74
- Bias, 18, 77, 98
- Boosting, 22, 51, 83
- C4 model, 89
- Cascade models, 83
- Causal inference, 59, 95
- CI/CD, 62, 86
- Circuit breaker (NEPSE), 10, 73
- Code review, 86
- Concept drift, 45, 84
- Conformal prediction, 55
- Containerisation, 43, 81
- CQRS, 82
- Cross‑validation, 20, 34
- Dask, 48, 85, 91
- Data drift, 45, 77
- Data ingestion, 5, 74
- Data leakage, 10, 20, 92
- Data quality, 5, 6, 90
- Data versioning, 5
- Datetime features, 11
- Debugging, 92
- Deployment, 38‑50, 74, 81
- Differential privacy, 49, 77
- Distributed systems, 48, 85
- Docstrings, 86, 89
- Documentation, 10, 89
- Domain knowledge, 10, 14, 75, 76
- Drift detection, 45, 77, 84
- Edge AI, 96
- Email alerts, 73
- Energy forecasting, 79
- Ensemble, 51, 83
- Entanglement (quantum), 97
- Error analysis, 37
- Ethics, 98
- Event sourcing, 82
- Event‑driven architecture, 82
- Explainability, 36, 77, 98
- Fairness, 77, 98
- FastAPI, 40, 74, 81
- Feature engineering, 10‑17, 74‑80
- Feature selection, 16, 10
- Feature store, 63, 74
- Featuretools, 17, 10
- Few‑shot learning (LLM), 94
- Financial prediction, 74
- Fine‑tuning (foundation models), 93
- Forecasting (general), 1
- Foundation models, 93, 99
- GDPR, 49, 98
- Git, 3, 86
- Gradient boosting, 22, 75
- Granger causality, 56, 95
- Grafana, 44, 73
- Great Expectations, 90
- Healthcare prediction, 77
- Hierarchical time series, 57
- Holiday effects, 11, 75
- Hyperparameter tuning, 35
- Imputation, 4, 6
- Incremental learning, 84
- Inference (distributed), 85
- Integration tests, 86, 90
- Internet of Things (IoT), 78
- Interpretability, 36, 77
- Inventory optimisation, 80
- Jupyter, 3
- Kafka, 42, 78, 82
- Kanban, 88
- Knowledge distillation, 96
- Kubernetes, 43, 81
- Lag features, 11, 75
- Large language models (LLMs), 94
- Lead time prediction, 80
- LightGBM, 22, 75
- LIME, 36, 98
- Linear regression, 23
- Load forecasting, 79
- Logging, 44, 92
- Look‑ahead bias, 10
- LSTM, 26, 74
- Microservices, 81
- Missing values, 4, 6
- MLOps, 61‑69
- Model card, 66, 77, 89
- Model drift, 45
- Model registry, 39, 74
- Model routing, 83
- Monitoring, 44, 73, 74
- Multi‑echelon inventory, 80
- Multi‑model systems, 83
- Multicollinearity, 10, 16
- Multivariate time series, 56
- NEPSE dataset, 2, 5
- Neural networks, 25‑29
- Notification channels, 73
- NumPy, 4, A
- Online learning, 84
- ONNX, 39
- OpenAPI, 89
- Optimisation (performance), 91
- Outliers, 4, 6
- pandas, 4, A
- Parallel processing, 48, 91
- Performance testing, 90
- Pinball loss, 79
- Prequential evaluation, 84
- Predictive maintenance, 78
- Privacy, 49, 77, 98
- Probabilistic forecasting, 55, 79, 99
- Profiling, 48, 91
- Project management, 88
- Prompt engineering, 94
- Pruning (model), 96
- Python, 3, 4
- Qiskit, 97
- Quality assurance, 90
- Quantization, 96
- Quantum machine learning, 97
- Random forest, 22, 77
- Ray, 48, 85, 91
- Readmission prediction, 77
- Real‑time learning, 84
- Refactoring, 86
- Regression metrics, 31
- Reinforcement learning, 54
- Remaining useful life (RUL), 78
- Reproducibility, 6, 86
- Resilience patterns, 81
- REST API, 40, 74
- Retail forecasting, 75
- Retrospectives, 88
- Retraining, 46, 80
- Risk management, 88
- River (online ML), 84
- RNN, 26
- Robust scaling, 15
- Routing (models), 83
- RSI (Relative Strength Index), 10, 73
- Runbooks, 89
- SARIMA, 21, 79
- Scaling (feature), 15
- Scrum, 88
- Security, 49, 90
- Sensitivity analysis, 90
- Sensor data, 78
- Service discovery, 81
- SHAP, 36, 77, 98
- Slack alerts, 73
- SLO/SLA, 68
- SMS alerts, 73
- Spatial features, 76
- Sprint planning, 88
- Stacking, 51, 83
- Stakeholders, 88
- Standardisation, 15
- Stationarity, 2, 10
- Statistical models, 21
- Streaming data, 42, 78
- Supply chain, 80
- Support vector machines (SVM), 24
- Symbolic regression, 95
- Technical debt, 86
- Technical indicators, 10, 13
- TensorFlow Lite, 78, 96
- Testing, 86, 90
- TimeSeriesSplit, 20, 34
- TinyML, 96
- Transfer learning, 52
- Transformer models, 28
- Transparency, 98
- Troubleshooting, 92
- tsfresh, 17, 10
- Type hints, 86
- Uncertainty, 55, 79, 99
- Unit tests, 86, 90
- User documentation, 89
- Validation (time‑series), 20, 34, 77
- Version control, 3, 86
- Walk‑forward validation, 20, 74
- Weather forecasting, 76
- Web scraping, 5
- XGBoost, 22, 74, 75
- Zero‑shot forecasting, 93, 99
- Zoo (models), D

---

**End of Appendices**