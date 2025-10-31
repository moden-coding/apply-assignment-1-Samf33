import pandas as pd
import numpy as np

def assign_letter_grades(df):
    df['Grade'] = df['Exam_Score'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else ('C' if x >= 70 else 'D')))
    return df
def calculate_adjusted_score(df):
    df['Adjusted_Score'] = df.apply(lambda row: row['Exam_Score'] + (row['Study_Hours'] * 1.5) + (row["Attendance"] * 10), axis=1)
    return df

def categorize_performance(df):
    
    df['Performance'] = df.apply(performance, axis = 1)
    return df
def performance(row):
    if row["Grade"] == "A" and row["Study_Hours"] > 6:
        return "Outstanding"
    elif row["Grade"] == "B" and row["Attendance"] >= 0.9:
        return "Strong"
    elif row["Grade"] in ["C", "D"]:
        return "Needs Improvement"
    else:
        return "Average"

# Sample dataset
df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Ella", "Frank"],
    "Exam_Score": [85, 72, 90, 64, 78, 95],
    "Study_Hours": [6, 3, 8, 2, 4, 10],
    "Attendance": [0.95, 0.80, 0.90, 0.70, 0.75, 0.98]
})
print(assign_letter_grades(df))
print(calculate_adjusted_score(df))
print(categorize_performance(df))

