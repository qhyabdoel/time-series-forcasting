import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat data contoh
np.random.seed(42)

dates = pd.date_range(start="2026-10-01", periods=30, freq="D")

df = pd.DataFrame(
    {
        "date": dates,
        "followers": 1000 + np.arange(30) * 15,
        "likes": np.random.randint(100, 300, 30),
        "comments": np.random.randint(10, 50, 30),
    }
)

# 2. Membuat beberapa missing values
df.loc[5, "likes"] = np.nan
df.loc[10, "comments"] = np.nan

# 3. Memastikan tipe tanggal
df["date"] = pd.to_datetime(df["date"])

# 4. Sorting
df = df.sort_values("date")

# 5. Mengisi missing values
df["likes"] = df["likes"].interpolate()
df["comments"] = df["comments"].interpolate()

# 6. Membuat date sebagai index
df = df.set_index("date")

# 7. Resampling menjadi mingguan
weekly = df.resample("W").agg({"followers": "last", "likes": "sum", "comments": "sum"})

# 8. Visualisasi
weekly["likes"].plot(figsize=(10, 5), marker="o", title="Weekly Instagram Likes")

plt.ylabel("Total Likes")
plt.grid()
plt.show()

print(weekly)
