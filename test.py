import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("test.csv")
if 'Unnamed: 0' in df.columns:
    df = df.drop(['Unnamed: 0'], axis=1)
print(df.sample(5))

print("Correlation : ")
print(df.corr(method='spearman'))

plt.plot(df['rating'])
plt.show()

# plt.hist(df['rating'],alpha=0.2)
# plt.show()
# plt.hist(df['registrationTimeSeconds'],alpha=0.2)
# plt.show()
