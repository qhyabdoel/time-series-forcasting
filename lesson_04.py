import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat dataset 90 hari
np.random.seed(42)

dates = pd.date_range(start="2026-08-01", periods=90, freq="D")

weekly_effect = np.array([-20, -15, -10, 0, 10, 35, 25])[dates.dayofweek]

likes = np.round(
    150 + 0.8 * np.arange(90) + weekly_effect + np.random.normal(0, 8, 90)
).astype(int)

df = pd.DataFrame({"date": dates, "likes": likes}).set_index("date")

# 2. Split training dan testing
train_size = int(len(df) * 0.8)

train = df.iloc[:train_size]
test = df.iloc[train_size:]

# 3. Naive Forecast
naive_forecast = np.repeat(train["likes"].iloc[-1], len(test))

# 4. Seasonal Naive Forecast
season_length = 7

last_season = train["likes"].iloc[-season_length:].to_numpy()

seasonal_forecast = np.tile(last_season, int(np.ceil(len(test) / season_length)))[
    : len(test)
]

# 5. Membuat tabel hasil prediksi
results = pd.DataFrame(
    {
        "actual": test["likes"],
        "naive": naive_forecast,
        "seasonal_naive": seasonal_forecast,
    },
    index=test.index,
)

# 6. Menghitung MAE
naive_mae = np.mean(np.abs(results["actual"] - results["naive"]))

seasonal_mae = np.mean(np.abs(results["actual"] - results["seasonal_naive"]))

print("Naive MAE:", round(naive_mae, 2))
print("Seasonal Naive MAE:", round(seasonal_mae, 2))

# 7. Visualisasi
plt.figure(figsize=(13, 6))

plt.plot(train.index, train["likes"], label="Training Data")

plt.plot(test.index, test["likes"], label="Actual")

plt.plot(results.index, results["naive"], label="Naive Forecast", linestyle="--")

plt.plot(
    results.index, results["seasonal_naive"], label="Seasonal Naive", linestyle="--"
)

plt.title("Instagram Likes Forecasting")
plt.xlabel("Date")
plt.ylabel("Likes")
plt.legend()
plt.grid(True)
plt.tight_layout()
# plt.show()

plt.savefig("lesson_04.png", dpi=150, bbox_inches="tight")
