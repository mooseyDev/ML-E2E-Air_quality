import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# See value dist.
df = pd.read_csv("data/processed/pm25_labeled.csv")
print(f" Value Counts = {df['air_quality'].value_counts()}")

# Violin plot to see dist.
sns.violinplot(data = df[df['pm25'] > 0], x = 'air_quality', y = 'pm25')
plt.title("pm25 distribution")
plt.xlabel("Air Quality")
plt.ylabel("pm25 value")
plt.tight_layout()
plt.show()