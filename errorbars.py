import pandas as pd
import numpy as np
from numpy import median

import seaborn as sns
import matplotlib.pyplot as plt

asd = pd.read_excel(r'C:\Users\asd.xlsx', sheet_name='Sheet1')
asdd = pd.DataFrame(asd, columns= ['Mesec','Broj zahteva poslednjeg dana u mesecu'])

sns.barplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd, estimator=median, capsize=0.3)

plt.show()