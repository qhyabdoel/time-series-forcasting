import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

data = {"followers": [10, 20, 30, 40, 50, 60, 70]}

df = pd.DataFrame(data)

model = SimpleExpSmoothing(df["followers"], initialization_method="estimated")

result = model.fit(smoothing_level=0.3)

forecast = result.forecast(steps=3)

print(forecast)
