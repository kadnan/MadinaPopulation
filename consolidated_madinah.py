import pandas as pd
import matplotlib.pyplot as plt

xls_population = pd.ExcelFile('Madina-pop.xlsx',index_col=False)

# select the sheet
df = xls_population.parse('Madinah-2011-2012')
my_dpi = 96
plt.style.use('fivethirtyeight')
ax = df[['Saudi','Non Saudi']].plot(kind='bar', title ="Madinah City 2011-2012",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("Year",fontsize=12)
ax.set_ylabel("Population",fontsize=12)
ax.set_xticklabels(df['Year'],rotation=0)
plt.savefig('2011.png', dpi=my_dpi)
plt.show()
