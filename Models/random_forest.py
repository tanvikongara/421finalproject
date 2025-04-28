import pandas as pd
import os

data_path = os.abspath() + "Data/total_merged_data.pkl"

df = pd.read_csv(data_path)
