import pandas as pd
df=pd.read_csv("student_results.csv")
print("\nRemoving duplicates:")
df=df.drop_duplicates()
subjects=['Math','Science','English']
df['Total_Marks']=round(df[subjects].sum(axis=1),2)
df['Average']=round(df[subjects].mean(axis=1),2)
def grade(average):
    if average>=90:
        return  "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"
df['Grade']=df['Average'].apply(grade)
def status(average):
    if average>=50:
        return "Pass"
    else:
        return "Fail"
df['Status']=df['Average'].apply(status)
highest_marks_index=df['Total_Marks'].idxmax()
highest_mark=df.loc[highest_marks_index]['Name']
lowest_marks_index=df['Total_Marks'].idxmin()
lowest_marks=df.loc[lowest_marks_index]['Name']
average_score=round(df['Average'].mean(),2)
above=df['Average']>average_score
above_score=df.loc[above]
below=df['Average']<average_score
below_score=df.loc[below]
attendance=df['Attendance']>=90
attendance_score=df.loc[attendance]
low_attendance=df['Attendance']<90
low_attendance_score=df.loc[low_attendance]
average_sub=round(df[subjects].mean(),2)
grade_distribution=df['Grade'].value_counts()
passed_number_students=df['Status'].value_counts()
passed_students=round((passed_number_students/len(df))*100,2)
top_3=df.nlargest(3,'Average')
sorting=df.sort_values('Average',ascending=False)
print(df)
print(f"\n1:Highest_Scorer: {highest_mark}")
print(f"2:Lowest_Scorer: {lowest_marks}")
print(f"3:Class Average Score: {average_score}")
print(f"4:Subjects average:\n{average_sub}")
print(f"5:Students above class averages:\n{above_score}")
print(f"6:Students below class averages:\n{below_score}")
print(f"7:Students with maximum attendance:\n{attendance_score}")
print(f"8:Students with  attendance lower than 90:\n{low_attendance_score}")
print(f"9:Grade Distribution:\n{grade_distribution}")
print(f"10:Number of passed or failed students:\n{passed_number_students}")
print(f"11:Passed Students percentage:\n{passed_students}")
print(f"12:Top 3 students:\n{top_3}")
print(f"13:Highest scorer to lowest scorer:\n{sorting}")
df.to_csv("cleaned_student_results.csv",index=False)





