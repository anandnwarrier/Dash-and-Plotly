import pandas as pd
import numpy as np

df=pd.read_csv(r'data\nst-est2017-alldata.csv')
print(df.head())

df2=df[df['DIVISION']=='1']
print('\n\n# NOTE:  After setting NAME as an index:-')
df2.set_index(['NAME'],inplace=True)  #  Sets column 'NAME' as the index, inplace=True makes the changes to df2..like. df2=df2.set_index(...)
print(df2)

print('\n\n# NOTE:  After setting REGION and  STATE also as indices:-')
df3=df2.set_index(['REGION','STATE'])
print(df3,'\n\n')

list_of_cols=[col for col in df2.columns if col.startswith('POP') ]  # FOR POPULATION type columns
print(list_of_cols,'\n')
df2=df2[list_of_cols]
print(df2)

import plotly.offline as pyo
import plotly.graph_objs as go

print(df2.loc['Maine'])
data=[
    go.Scatter(x=df2.columns,
                y=df2.loc[name],
                mode='lines',
                name=name) for name in df2.index
    ]

pyo.plot(data,filename='Generated_HTML_plots/line_plot2.html')
