import pandas as pd
df = pd.read_csv("Titanic.csv")
# print(df) #shows limited
# print(df.to_string()) #shows all data

# print(df.head())
# print(df.info())
# print(df.describe())




'''Data Cleaning'''


print(df["Age"].notnull().sum())
# newDf=pd.DataFrame()
# newDf["Age"]=df["Age"].fillna(df["Age"].median())
# print(newDf)

# print(newDf["Age"].notnull().sum())
# print(newDf["Age"])

#way1
# df["Age"] = df["Age"].fillna(df["Age"].median()) 
# print(df["Age"])
# print(df)

#way2
df.fillna({"Age":df["Age"].median()},inplace=True)

# print(df)

# print(df["Age"].notnull().sum())


df.drop(columns=["Cabin","Ticket"],inplace=True)

df["Sex"]=df["Sex"].map({"male":0,"female":1})

# print(df["Sex"].notna().sum())

df.rename(columns={"Sex":"Gender"},inplace=True)


# print(df[(df["Gender"]==1)&(df['Pclass']==1)])



# print(df.groupby("Pclass")["Survived"].mean())

print(df.loc[df['Age'] > 60, ['Name', 'Age', 'Fare']].head(10))

df['Family_Size'] = df['SibSp'] + df['Parch']  +1
# print(df)

df['Title'] =  df['Name'].str.split(',').str[1].str.split('.').str[0].str.strip()


bins = [0, 12, 18, 60, 100]

labels = ['Child', 'Teenager', 'Adult', 'Senior'] 

df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df)

