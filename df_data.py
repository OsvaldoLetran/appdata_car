import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('cars.csv')
Q7_df = df[(df['manufacturer_name'] == 'Audi') & (df['model_name'] == 'Q7')]

print('DataFrame')
print(df.iloc[0:5, 5:15])
print('*' * 25)
print(Q7_df.head())
print('*' * 25)

print(f"mean: {df['price_usd'].mean()}\nmoda: {df['price_usd'].mode()[0]}")
print('*' * 25)
print(f"freq: {df['price_usd'].value_counts()}")
print('*' * 25)

print(f"median: {df['price_usd'].median()}\nstd dev: {df['price_usd'].std()}")
print(f"range: {df['price_usd'].max() - df['price_usd'].min()}")

q_1 = df['price_usd'].quantile(q = 0.25) 
q_3 = df['price_usd'].quantile(q = 0.75) 

print(f"rango intercuartil: {q_3 - q_1}")
print(f"rango deteccion outliers: {q_1 - 1.5*(q_3 - q_1)}, {q_3 + 1.5*(q_3 - q_1)}")
print('*' * 25)
print(f'datos nulos solo en engine_capacity: {df.engine_capacity.isnull().sum()}')


fig, (ax_hist, ax_box) = plt.subplots(1, 2, figsize = (11.5, 5))
sns.histplot(df, x = 'price_usd', hue = 'engine_type', multiple = 'stack', ax = ax_hist)
sns.boxplot(df, x = 'price_usd', ax = ax_box)
# sns.boxplot(df, x = 'engine_fuel', y = 'price_usd', ax = ax_box)
plt.show()


fig, axes_Q7 = plt.subplots()
sns.histplot(Q7_df, x='price_usd', hue = 'year_produced', ax = axes_Q7)
plt.show()