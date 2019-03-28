##Suicide Data from WHO

import pandas as pd

import numpy as np # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns
import os

dataset = pd.read_csv("master.csv")

dataset.head()

dataset.columns.values

dataset.columns = ['country', 'year', 'sex', 'age', 'suicides_no', 'population',
       'suicidesper100kpop', 'country-year', 'HDI for year',
       'gdp_for_year_dollars', 'gdp_per_capita_dollars', 'generation']

dataset.columns.values

dataset['gdp_for_year_dollars'] = dataset['gdp_for_year_dollars'].str.replace(',','').astype(float)


dataset.info()

dataset.isnull().sum().sort_values(ascending=False)

data_n = dataset.drop(['HDI for year', 'country-year'], axis=1)

data_n.head(3)

data_n.describe()

data_n.describe(include=['O'])

data_n[['sex','suicides_no']].groupby(['sex']).mean().sort_values(by='suicides_no', ascending=False).plot(kind='bar')

plt.figure(figsize=(10,5))
sns.barplot(x = 'age', y='suicides_no', hue='sex', data=data_n.groupby(["age","sex"]).sum().reset_index()).set_title('Age vs Suicides')
plt.xticks(rotation=90)






