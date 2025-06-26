import pandas as pd
import numpy as np

df=pd.read_csv('student_interaction_data 1.csv')
print(df)


df['course_difficulty'] = pd.Categorical(df['course_difficulty']).codes
df['instructor_quality'] = pd.Categorical(df['instructor_quality']).codes


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chaitrraa*45",
    database="smdb6"
)
cursor = conn.cursor()


for _, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO student_interactions (student_id, course_id, interaction_date, interaction_type)
            VALUES (%s, %s, %s, %s)
        """, (
            row['student_id'],
            row['course_id'],
            row['interaction_date'],
            row['interaction_type']
        ))

        cursor.execute("""
            INSERT INTO assessment_scores (student_id, course_id, score)
            VALUES (%s, %s, %s)
        """, (
            row['student_id'],
            row['course_id'],
            row['score']
        ))

        cursor.execute("""
            INSERT INTO dropout_records (student_id, course_id, dropout, course_difficulty)
            VALUES (%s, %s, %s,%s)
        """, (
            row['student_id'],
            row['course_id'],
            row['dropout'],
            row['course_difficulty']
        ))
    except mysql.connector.errors.IntegrityError:
        continue

conn.commit()
cursor.close()
conn.close()


    


