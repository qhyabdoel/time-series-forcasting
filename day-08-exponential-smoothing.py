import pandas as pd

data = {"followers": [10, 20, 30, 40, 50, 60, 70]}

df = pd.DataFrame(data)

# Exponential Smoothing
df["ES"] = df["followers"].ewm(alpha=0.3, adjust=False).mean()

print(df)
