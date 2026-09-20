# Part (a)
import pandas as pd

data = pd.read_csv("Pastry.csv")
print(data.describe())

# Part (b):
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Pastry.csv")

plt.scatter(data["Moisture"], data["Rating"])
plt.xlabel("Moisture")
plt.ylabel("Rating")
plt.title("Moisture vs Rating")
plt.show()

plt.scatter(data["Sweetness"], data["Rating"])
plt.xlabel("Sweetness")
plt.ylabel("Rating")
plt.title("Sweetness vs Rating")
plt.show()

# Part (c):
import pandas as pd

data = pd.read_csv("Pastry.csv")
correlation = data.corr()
print(correlation)

# Part (d):
import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("Pastry.csv")
X = data["Sweetness"]
y = data["Rating"]

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print(model.summary())

# Part (e):
import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("Pastry.csv")
X = data["Moisture"]
y = data["Rating"]

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print("R-squared:", model.rsquared)

# Part (g):
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv("Pastry.csv")

X = data["Moisture"]
y = data["Rating"]

X_const = sm.add_constant(X)

model = sm.OLS(y, X_const).fit()
plt.scatter(X, y)
plt.plot(X, model.predict(X_const))


plt.xlabel("Moisture")
plt.ylabel("Rating")
plt.title("Moisture vs Rating with Regression Line")

plt.show()

# Part (h):
import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("Pastry.csv")

X = data["Moisture"]
y = data["Rating"]

X_const = sm.add_constant(X)
model = sm.OLS(y, X_const).fit()

prediction = model.predict([1, 2])

print("Predicted Rating:", prediction[0])
