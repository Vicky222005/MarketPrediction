import config
import pandas as pd


def gap_detection(df, freq="h"):
    """
    Detects gaps in the time series data based on the specified frequency.
    Returns a DataFrame with the start and end timestamps of each gap and its size in hours.
    Run this function after data_fetch to identify any missing data points in the fetched OHLCV data.
    """
    full_index = pd.date_range(start=df.index.min(), end=df.index.max(), freq=freq)
    missing_timestamps = full_index.difference(df.index)

    if missing_timestamps.empty:
        print("No gaps detected.")
        return pd.DataFrame()

    gaps = []
    block_start = missing_timestamps[0]
    previous_timestamp = missing_timestamps[0]

    for timestamp in missing_timestamps[1:]:
        expected_next = previous_timestamp + pd.Timedelta(freq)
        if timestamp != expected_next:
            gaps.append(
                {
                    "start": block_start,
                    "end": previous_timestamp,
                    "size_hours": int(
                        (previous_timestamp - block_start) / pd.Timedelta("1H")
                    )
                    + 1,
                }
            )
            block_start = timestamp
        previous_timestamp = timestamp

    gaps.append(
        {
            "start": block_start,
            "end": previous_timestamp,
            "size_hours": int((previous_timestamp - block_start) / pd.Timedelta("1H"))
            + 1,
        }
    )

    gaps_df = pd.DataFrame(gaps)
    print(
        f"{len(gaps_df)} gap block(s) found, total {gaps_df['size_hours'].sum()} missing hours"
    )
    return gaps_df
