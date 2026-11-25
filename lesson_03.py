import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Membuat data selama 90 hari
np.random.seed(42)

dates = pd.date_range(start="2026-08-01", periods=90, freq="D")

# Efek hari dalam seminggu
weekly_effect = np.array([-20, -15, -10, 0, 10, 35, 25])[dates.day_of_week]

# Membuat trend + seasonality + noise
likes = 150 + 0.8 * np.arange(90) + weekly_effect + np.random.normal(0, 8, 90)

df = pd.DataFrame({"date": dates, "likes": likes})

df = df.set_index("date")

# Rolling mean 7 hari
df["rolling_mean_7d"] = df["likes"].rolling(window=7).mean()
print("Rolling mean likes 7 hari pertama:")
print(df[["likes", "rolling_mean_7d"]].head(10).round(2))

# Rata-rata likes berdasarkan hari dalam seminggu
weekday_names = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
weekday_average = df.groupby(df.index.day_of_week)["likes"].mean()
best_weekday = weekday_average.idxmax()
print("\nRata-rata likes per hari:")
print(weekday_average.rename(index=dict(enumerate(weekday_names))).round(2))
print(
    f"Hari dengan rata-rata likes tertinggi: {weekday_names[best_weekday]} "
    f"({weekday_average.loc[best_weekday]:.2f} likes)"
)

# Visualisasi likes harian dan rolling mean
plt.figure(figsize=(12, 5))

plt.plot(df.index, df["likes"], label="Daily Likes", marker="o", markersize=3)
plt.plot(
    df.index,
    df["rolling_mean_7d"],
    label="7-Day Rolling Mean",
    color="red",
    linewidth=2,
)

plt.title("Instagram Daily Likes")
plt.xlabel("Date")
plt.ylabel("Likes")
plt.legend()
plt.grid(True)

plt.tight_layout()
# plt.show()

plt.savefig("lesson_03.png", dpi=150, bbox_inches="tight")
plt.close()

# Dekomposisi time series dengan periode mingguan
decomposition = seasonal_decompose(df["likes"], model="additive", period=7)
fig, axes = plt.subplots(4, 1, figsize=(12, 9), sharex=True)
components = [
    (decomposition.observed, "Observed", "Likes", "steelblue"),
    (decomposition.trend, "Trend", "Likes", "green"),
    (decomposition.seasonal, "Seasonal", "Likes", "orange"),
    (decomposition.resid, "Residual", "Residual", "purple"),
]

for ax, (component, title, ylabel, color) in zip(axes, components):
    ax.plot(component.index, component, color=color)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True)

axes[-1].axhline(0, color="black", linewidth=1, linestyle="--")
axes[-1].set_xlabel("Date")
fig.tight_layout()
plt.savefig("lesson_03_decomposition.png", dpi=150, bbox_inches="tight")
plt.close()

trend = decomposition.trend.dropna()
trend_change = trend.iloc[-1] - trend.iloc[0]
seasonal_range = decomposition.seasonal.max() - decomposition.seasonal.min()

print("\nKesimpulan:")
if trend_change > 0:
    print(f"Terdapat trend meningkat (komponen trend naik {trend_change:.2f} likes).")
elif trend_change < 0:
    print(f"Terdapat trend menurun (komponen trend turun {abs(trend_change):.2f} likes).")
else:
    print("Tidak terlihat perubahan trend pada komponen trend.")

if seasonal_range > 0:
    print(
        "Terdapat seasonality mingguan; rentang komponen seasonal "
        f"adalah {seasonal_range:.2f} likes."
    )
else:
    print("Tidak terlihat seasonality mingguan pada komponen seasonal.")
