# config.py

SYMBOL = "BTC/USDT"
TIMEFRAME = "1h"  # 1m, 5m, 15m, 1h, 4h, 1d
LIMIT = 1000  # number of candles to fetch
EXCHANGE = "binance"

MODEL_PATH = "models/model.joblib"
RAW_DATA_PATH = "data/raw/ohlcv.csv"
PROCESSED_DATA_PATH = "data/processed/features.csv"
