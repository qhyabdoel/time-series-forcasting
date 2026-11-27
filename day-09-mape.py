from sklearn.metrics import mean_absolute_percentage_error

actual = [20, 30, 40, 50, 60]
forecast = [18, 25, 35, 45, 55]

mape = mean_absolute_percentage_error(actual, forecast) * 100

print("MAPE:", mape)
