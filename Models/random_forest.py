import pandas as pd
import os

# Get absolute path
data_path = os.path.join(os.getcwd(), "Data", "total_merged_data.parquet")

# Load parquet file
df = pd.read_parquet(data_path)