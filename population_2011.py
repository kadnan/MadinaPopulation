import pandas as pd
import matplotlib.pyplot as plt

#Read Excel
xls_population = pd.ExcelFile('Madina-pop.xlsx',index_col=False)
names = xls_population.sheet_names
df = xls_population.parse('population-Madinah-Region-2011')
#df.set_index('Governorate', inplace = True)
df.index.name = None
df.columns = ['Region','Saudi','Non Saudi','Total']
print(df['Region'])

my_dpi = 96
plt.style.use('ggplot')
ax = df[['Saudi','Non Saudi']].plot(kind='line', title ="Population 2011 Medinah Governorate",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("Regions",fontsize=12)
ax.set_ylabel("Population",fontsize=12)
ax.set_xticklabels(df['Region'],rotation=0)
plt.savefig('2011.png', dpi=my_dpi)
plt.show()



