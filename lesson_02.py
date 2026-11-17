import pandas as pd
import numpy as np

data = {
    "date": [
        "2026-11-01",
        "2026-11-02",
        "2026-11-03",
        "2026-11-04",
        "2026-11-05",
        "2026-11-06",
        "2026-11-07",
    ],
    "followers": [1000, 1020, 1040, 1050, 1080, 1100, 1150],
    "likes": [120, 135, 150, 140, 180, 190, 220],
    "comments": [15, 18, 20, 17, 25, 28, 32],
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# df = df.sort_values(by="likes").reset_index(drop=True)

# print(df)
# print(df.info())
# print(df.dtypes)

weekly_data = df.resample("W", on="date").agg(
    {"followers": "last", "likes": "sum", "comments": "sum"}
)

print(weekly_data)
