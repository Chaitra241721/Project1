import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('student_interaction_data 1.csv')
print(df)

df = df.drop(['interaction_date','course_difficulty'], axis=1)

le_instructor = LabelEncoder()
df['instructor_name'] = le_instructor.fit_transform(df['instructor_name'])
le_course = LabelEncoder()
df['course_id'] = le_course.fit_transform(df['course_id'])
le_type = LabelEncoder()
df['interaction_type'] = le_type.fit_transform(df['interaction_type'])


X = df.drop('dropout', axis=1)
y = df['dropout']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")