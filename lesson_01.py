import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data followers selama 30 hari
np.random.seed(42)

dates = pd.date_range(start="2026-10-01", periods=30, freq="D")

followers = 1000 + np.arange(30) * 20 + np.random.randint(-15, 15, 30)

# Membuat DataFrame
df = pd.DataFrame({"date": dates, "followers": followers})

# Melihat data
print(df.head())

# Visualisasi
plt.figure(figsize=(12, 5))

plt.plot(df["date"], df["followers"], marker="o")

plt.title("Instagram Followers Growth")
plt.xlabel("Date")
plt.ylabel("Followers")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
