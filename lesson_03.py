import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data selama 90 hari
np.random.seed(42)

dates = pd.date_range(start="2026-08-01", periods=90, freq="D")

# Efek hari dalam seminggu
weekly_effect = np.array([-20, -15, -10, 0, 10, 35, 25])[dates.day_of_week]

# Membuat trend + seasonality + noise
likes = 150 + 0.8 * np.arange(90) + weekly_effect + np.random.normal(0, 8, 90)

df = pd.DataFrame({"date": dates, "likes": likes})

df = df.set_index("date")

# Visualisasi
plt.figure(figsize=(12, 5))

plt.plot(df.index, df["likes"], label="Daily Likes", marker="o", markersize=3)

plt.title("Instagram Daily Likes")
plt.xlabel("Date")
plt.ylabel("Likes")
plt.legend()
plt.grid(True)

plt.tight_layout()
# plt.show()

plt.savefig("lesson_03.png", dpi=150, bbox_inches="tight")
plt.close()
