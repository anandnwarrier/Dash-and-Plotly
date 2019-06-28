import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv(r'data\mpg.csv')
# if you don't want to plot for all x's, specify range using start and end. size is the length of the bin
data=go.Histogram(x=df['mpg'],xbins=dict(start=0,end=50,size=2))
fig=go.Figure(data=[data],layout=go.Layout(title='Histogram',xaxis=dict(title='x')))
pyo.plot(fig,filename='Generated_HTML_plots/histogram.html')
