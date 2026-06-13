import pandas as pd
from backend.db import engine

df = pd.read_csv("data/Superstore_Dataset.csv",encoding="latin1")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

df.to_sql(
    "superstore",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")


