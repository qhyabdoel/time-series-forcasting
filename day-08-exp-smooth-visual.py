import matplotlib.pyplot as plt
import pandas as pd

data = {"followers": [10, 20, 30, 40, 50, 60, 70]}

df = pd.DataFrame(data)

# Exponential Smoothing
df["ES_01"] = df["followers"].ewm(alpha=0.1, adjust=False).mean()
df["ES_08"] = df["followers"].ewm(alpha=0.8, adjust=False).mean()

plt.plot(df["followers"], label="Actual", marker="o")

plt.plot(df["ES_01"], label="Alpha 0.1")

plt.plot(df["ES_08"], label="Alpha 0.8")

plt.title("Exponential Smoothing")
plt.xlabel("Day")
plt.ylabel("New Followers")
plt.legend()
# plt.show()

plt.savefig("day-08-exp-smooth-visual.png", dpi=150, bbox_inches="tight")
plt.close()
