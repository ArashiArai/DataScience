import pandas as pd



data1 = pd.DataFrame(
    [[98, 76, 65], [54, 342, 31]],
    index=[1, 2],                  
    columns=['a', 'b', 'c']
)
print(data1)
print("----------------------------")

data2 = pd.Series([1.0,20,300],
        index=["A","B","C"])
# print(data2["B"])

# print(data2.info())

# print(data2.loc["A"])

# print(data2.head(1))

# print(data2.describe())

# print(data2.isnull())

print(data2[data2>1.0]) #filtering