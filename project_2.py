import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv("data/output_file.csv")
df.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis=1, inplace=True)
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

def save_plot(fig, filename):
    fig.tight_layout()
    fig.savefig("visuals/" + filename)

# Example: Attrition distribution
fig = plt.figure()
sns.countplot(x='Attrition', data=df)
plt.title("Attrition Distribution")
save_plot(fig, "attrition_distribution.png")
