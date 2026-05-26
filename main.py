import config
import pandas as pd
from data.fetch import fetch_data
from data.clean import gap_detection

# Stage 1: Fetch
fetch_data()

# Stage 2: Load + Process
df = pd.read_csv(config.RAW_DATA_PATH, index_col="timestamp", parse_dates=True)
gaps = gap_detection(df)
