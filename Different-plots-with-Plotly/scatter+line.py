import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

np.random.seed(7)

random_x=np.linspace(0,10,20)
random_y=np.random.normal(0,1,20)

trace1=go.Scatter(x=random_x,y=random_y-10,mode='markers',name='myScatterPlot')
trace2=go.Scatter(x=random_x,y=random_y,mode='lines',name='myLinePlot')
trace3=go.Scatter(x=random_x,y=random_y+10,mode='lines+markers',name='myLinePlot')
layout=go.Layout(title='Line charts')
data=[trace1,trace2,trace3]
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Generated_HTML_plots/scatter+line.html')
