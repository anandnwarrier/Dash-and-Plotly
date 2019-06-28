import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo
df=pd.read_csv(r'data\2018WinterOlympics.csv')
print(df.head())

trace1=go.Bar(x=df['NOC'],y=df['Gold'],name='Gold',marker=dict(color='#FFD700'))
trace2=go.Bar(x=df['NOC'],y=df['Silver'],name='Silver',marker=dict(color='#9EA0A1'))
trace3=go.Bar(x=df['NOC'],y=df['Bronze'],name='Bronze',marker=dict(color='#CD7F32'))

data=[trace1,trace2,trace3]
#layout=go.Layout(title='Medals vs country',xaxis=dict(title='Country'),yaxis=dict(title='No of medals'))#nested
layout=go.Layout(title='Medals vs country',xaxis=dict(title='Country'),yaxis=dict(title='No of medals'),barmode='stack')#stack
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Generated_HTML_plots/bar.html')
