import ccxt
import config
import pandas as pd


def fetch_data():
    exchange_class = getattr(ccxt, config.EXCHANGE)
    exchange = exchange_class()

    ohlcv = exchange.fetch_ohlcv(config.SYMBOL, config.TIMEFRAME, limit=config.LIMIT)

    columns = ["timestamp", "open", "high", "low", "close", "volume"]
    df = pd.DataFrame(ohlcv, columns=columns)
    df.set_index("timestamp", inplace=True)
    df.index = pd.to_datetime(df.index, unit="ms")

    df.to_csv(config.RAW_DATA_PATH, index=True)
    print(f"Data fetched and saved to {config.RAW_DATA_PATH}")
    return df
