import pandas as pd
df=pd.read_csv("employee_salary.csv")
df=df.drop_duplicates()
df=df.replace("(empty)",0)
df['Salary']=df['Salary'].astype(float)
df['Experience']=df['Experience'].astype(int)
average_salary=round(df['Salary'].mean(),2)
average_rating=round(df['Rating'].mean(),2)
df['Salary']=df['Salary'].replace(0,average_salary)
print(df)
print(f"\n1:Total employees: {len(df['Employee'])}")
highest_salary_index=df['Salary'].idxmax()
highest_salary=df.loc[highest_salary_index]
print(f"\n2:Highest_salary:\n{highest_salary}")
lowest_salary_index=df['Salary'].idxmin()
lowest_salary=df.loc[lowest_salary_index]
print(f"\n3:Lowest_salary:\n{lowest_salary}")
print(f"\n4:Average salary: {average_salary}")
print(f"\n5:Average salary by department: {df.groupby('Department')['Salary'].mean().round(2)}")
print(f"\n6:Total salary by department: {df.groupby('Department')['Salary'].sum().round(2)}")
above=df['Salary']>average_salary
above_avg=df.loc[above]
print(f"\n7:Above average salary: \n{above_avg}")
rating=df['Rating']>4.5
rating_avg=df.loc[rating]
print(f"\n8:Employees with Rating greater than 4.5: \n{rating_avg}")
sort=df.sort_values('Salary',ascending=False)
print(f"\n9:Salaries from highest to lowest: \n{sort}")
highest=df.nlargest(3,'Salary')
print(f"\n10:Top 3 employees with highest salary: \n{highest}")
df.to_csv("cleaned_employee_salary.csv",index=False)
