"""
Box whisker plots have a box(called the inter-quartile range(IQR) which consists of 50% of the data)
and 2 whiskers which consist of the other two 25%
Box is bewteen q1 and q3
The box contains 50% of the data
Upper whisker is b/w Max val and q3 and contains 25% of the data
Lower whisker is b/w q1 and Min val  and contains 25% of the data
IQR is q1-q3
Med is the median

A value is an outlier if:
    1) it is > (1.5*IQR)+q3
    2) it is < (1.5*iqr)-q1

  -----  Max
    |
    |
----------- q3
|         |
|---------| Med
----------- q1
    |
    |
  -----  Min
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

a=np.random.randint(0,10,100)

trace1=go.Box(y=a)
trace2=go.Box(y=a,boxpoints='all')
trace3=go.Box(y=a,boxpoints='all',jitter=1)#jitter spreads the boxpoints
trace4=go.Box(y=a,boxpoints='all',jitter=0.6,pointpos=0)# pointpos=0 means both boxpoints and boxplot should overlay
trace5=go.Box(y=a,boxpoints='all',jitter=0.3,pointpos=2)# pointpos >0 puts boxpoints onto right.

# When a little Gaussian data with high variance is added to a large data with less variance, the newly added ones become outliers
b=np.concatenate([np.random.normal(0,1,50),np.random.normal(0,5,10)])
trace6=go.Box(y=b,boxpoints='outliers')# only outliers are plotted as boxpoints
#if pointpos<0, boxpoints are put on left. By default, pointpos is <0

fig=go.Figure(data=[trace1,trace2,trace3,trace4,trace5,trace6],layout=go.Layout(title='Box whisker plots'))
pyo.plot(fig,filename='Generated_HTML_plots/box_plot.html')
