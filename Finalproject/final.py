import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

i = 0

# TODO: Make sure to include parsing for [Max:,Mini:,Plus:] as well as newlines/spaces and the outliers
def parse_money(input: str):
    # Init Empty Price List
    prices: list = []
 
    # Remove Astericks and Dollar Sign From Price
    input = input.replace('*','')
    input = input.replace('$','')
    
    # Split Into List of Prices
    prices = input.split("/")
 
    # Init i to Zero for Loop
    i: int = 0
 
    # Turn Prices Into Integers
    for price in prices:
        prices[i] = int(price)
        i = i + 1
    
    # Returns Price As List of Integers
    return prices

# Returns Average Money As An Integer (Rounds Up From Float)
def return_average_money(list_of_prices: list):
    # Init Total To Zero
    total: int = 0
 
    # Get Number of Elements in List For Division
    num: int = len(list_of_prices)
    
    # Get Total Price
    for price in list_of_prices:
        total = total + price
 
    # Divide By Number of Elements In List
    average: int = total // num
 
    return average


dataframe = pd.read_excel( 'Finalproject/SeedUnofficialAppleData.xlsx')

dataframe.fillna(' ', inplace = True)
dataframe.columns =['Model', 'Release(d)_with_OS', 'Date','Discontinued', 'Support_Ended', 'Final_OS', 'Lifespan_Max', 'Lifespan_Min', 'Launch_Price']

df = dataframe.set_index('Model')

df1 = df.drop('model')
df2 = df1.drop(df1.index[0])
df2 = df2.iloc[1:]
df2.drop("iPhone SE (1st)", inplace=True)
df2.drop("iPhone SE (2nd)", inplace=True)
print(df2)
price_list = []
models_list = df2.index.tolist()

for n, i in enumerate(df2['Launch_Price']):
    price_list.append(return_average_money(parse_money(df2['Launch_Price'].tolist()[n])))

for n, i in enumerate(models_list):
    print(i + "," + str(price_list[n]))

plt.xlabel("Model")
plt.ylabel("Cost")
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)

plt.plot(models_list, price_list)
plt.show()
