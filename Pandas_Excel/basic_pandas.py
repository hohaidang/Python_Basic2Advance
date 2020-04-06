import pandas as pd

# Creating DataFrames
data = {
    'apples' : [3, 2, 0, 1],
    'oranges' : [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
print(purchases.head())

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases.head())
print(purchases.loc['June'])