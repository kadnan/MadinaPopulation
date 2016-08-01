import pandas as pd
import matplotlib.pyplot as plt

#Read Excel
xls_population = pd.ExcelFile('Madina-2012.xlsx',index_col=False)
names = xls_population.sheet_names
df = xls_population.parse('population-Madinah-Region-2012')
#df.set_index('Governorate', inplace = True)
df.index.name = None
df.columns = ['Region','Saudi','Non Saudi','Total']
print(df['Region'])
# df.to_csv('pop.csv')
# df = pd.read_csv('pop.csv',index_col = False)
# df.set_index('Governorate', inplace = True)

plt.style.use('ggplot')
ax = df[['Saudi','Non Saudi']].plot(kind='bar', title ="Population 2012 Medinah Region",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("Regions",fontsize=12)
ax.set_ylabel("Population",fontsize=12)
ax.set_xticklabels(df['Region'],rotation=0)

plt.show()


