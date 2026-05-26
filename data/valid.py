import config
import pandas as pd


def validate_data(df):
    """
    Checks OHLCV data for consistency and validity.
    """

    conditions = [
        df["high"] >= df["low"],
        df["high"] >= df["open"],
        df["high"] >= df["close"],
        df["low"] <= df["open"],
        df["low"] <= df["close"],
        df["open"] > 0,
        df["close"] > 0,
        df["high"] > 0,
        df["low"] > 0,
        df["volume"] >= 0,
    ]

    valid = pd.concat(conditions, axis=1).all(axis=1)
    n_invalid = (~valid).sum()
    if n_invalid > 0:
        print(f"Structural violations: {n_invalid} rows")
        print(df[~valid])

    return valid
