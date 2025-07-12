import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv("data/output_file.csv")
df.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis=1, inplace=True)
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

df_encoded = pd.get_dummies(df, drop_first=True)
corr_matrix = df_encoded.corr()

plt.figure(figsize=(15, 12))
sns.heatmap(corr_matrix, cmap='coolwarm', annot=False, linewidths=0.5)
plt.title("Correlation Heatmap (Attrition vs Features)")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
print("✅ Saved: correlation_heatmap.png")
