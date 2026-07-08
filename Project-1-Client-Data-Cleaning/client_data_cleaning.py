import pandas as pd
df=pd.read_csv("client-project1.csv")
df=df.drop_duplicates()
df=df.replace("(empty)",0)
print(df)
print(f"\n1:Total products:{len(df['Product'])}")
df['Price']=df['Price'].astype(int)
print(f"\n2:Average_Price of products= {df['Price'].mean(axis=0).round(2)}")
df0=df['Price'].idxmax()
df1=df.loc[df0]
print(f"\n3:Highest priced product:")
print(df1)
df= df.to_csv("client-project2.csv",index=False)
