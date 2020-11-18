import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


income = open("CaseStudy/income.csv", "r")
income = np.array(income.read().split(","), dtype="f")
income = income / income[0]

inflation = open("CaseStudy/cpi.csv", "r")
inflation = np.array(inflation.read().split(","), dtype="f")
inflation = inflation / inflation[0]

years = np.array(list(range(1996, 2019)))

r_squared = "r^2=" + str((np.corrcoef(income, inflation)[0,1])**2)[0:4]

df_inflation = pd.DataFrame(inflation, years)
df_income = pd.DataFrame(income, years)

print('\nYear\tInflation')
print(df_inflation)

print('\nYear\tIncome')
print( df_income)
plt.xlabel("Year")
plt.ylabel("Indexed to 1995=1.0")
plt.title("Inflation & Net National Income in The United States")

plt.plot(years, income, label="Net National Income")
plt.plot(years, inflation, label="Consumer Price Index")

plt.text(1996, 1.55, r_squared)
plt.annotate("Financial Crisis", xy=(2008, 1.325), xytext=(2008.5, 1.25), arrowprops=dict(facecolor="black"))
plt.legend(loc="upper left")
plt.show()
