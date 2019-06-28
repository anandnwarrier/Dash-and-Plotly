import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

x=np.linspace(0,1,100)
y=x**2+np.random.normal(0,0.1,100)
z=abs(x)

trace1=go.Scatter(x=x,y=y,name='Scatter plot',mode='markers' ,marker=dict(size=z*50))
trace2=go.Scatter(x=x,y=y,mode='lines')
trace3=go.Histogram(x=y)
trace4=go.Box(y=y,boxpoints='all',pointpos=0)

fig=tools.make_subplots(rows=2,#rows & cols
                        cols=2,
                        subplot_titles=['scatter','Line','Histogram','Box Whisker plot'],
                        shared_yaxes=False)

trace=[[trace1,trace2],[trace3,trace4]]
for j in range(2):
    for i in range(2):
        fig.append_trace(trace[j][i],j+1,i+1)

fig['layout'].update(title='Many plots!')

fig['layout']['xaxis1'].update(title='x')
fig['layout']['xaxis2'].update(title='x')
fig['layout']['xaxis3'].update(title='x', showgrid=False)
fig['layout']['xaxis4'].update(title='')

fig['layout']['yaxis1'].update(title='y')
fig['layout']['yaxis2'].update(title='y')
fig['layout']['yaxis3'].update(title='Frequency', showgrid=False)
fig['layout']['yaxis4'].update(title='y')

pyo.plot(fig,filename='Generated_HTML_plots/subplots.html')
