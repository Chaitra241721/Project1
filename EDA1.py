import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_interaction_data 1.csv")

# Identify engagement trends (active vs. inactive learners)
plt.figure(figsize=(10, 6))
sns.countplot(x='interaction_type', data=df )
plt.title('Engagement Trends')
plt.show()

# Analyze correlation between attendance and performance
corr_matrix = df[['attendance', 'score']].corr()
print(corr_matrix)


