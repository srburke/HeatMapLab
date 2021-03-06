# -*- coding: utf-8 -*-
"""ShannonB-HeatMap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fUYSKtukyP-vCA6OfZQ90S_s1j4pw0Ki
"""

# library
import seaborn as sns
import pandas as pd
import numpy as np

# Create a dataframe (data table)
df = pd.DataFrame(columns=['risk', 'likelihood', 'impact', 'score'])

df['risk']=['users', 'team', 'budget', 'security']

df['likelihood']=[0.2,0.3,0.1,0.5]

df['impact']=[1,2,7,10]

df['score']=df['impact']*df['likelihood']


scoresPivot=df.pivot('impact', 'likelihood', 'score')
print(scoresPivot)

labelsPivot=df.pivot('impact', 'likelihood', 'risk')
print(labelsPivot)

#replaces no labels with empty string
labelsPivot.fillna('', inplace=True)

# simple heatmap
p1=sns.heatmap(scoresPivot, cmap="RdPu", annot=labelsPivot, fmt='')