import pandas as pd   
import numpy as np  #packages for importing data as DataFrame
from numpy import median

import seaborn as sns
import matplotlib.pyplot as plt#packages for creating plots

asd = pd.read_excel(r'C:\Users\asd.xlsx', sheet_name='Sheet1')
asdd = pd.DataFrame(asd, columns= ['Mesec','Broj zahteva poslednjeg dana u mesecu']) #database of the Danube insurance company 

sns.barplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd, estimator=median, capsize=0.3) #creating barplot-visualizing error bars for each claim thah has been received at the end of month

plt.show()

