import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
)

data = {"actual": [20, 30, 40, 50, 60], "forecast": [18, 25, 35, 45, 55]}

df = pd.DataFrame(data)

# Calculate errors
df["error"] = df["actual"] - df["forecast"]

print(df)

# Calculate metrics
mae = mean_absolute_error(df["actual"], df["forecast"])

rmse = mean_squared_error(df["actual"], df["forecast"]) ** 0.5

mape = mean_absolute_percentage_error(df["actual"], df["forecast"]) * 100

print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)
