import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(7)

random_x=np.linspace(0,10,20)
random_y=np.random.normal(0,1,20)

data=[go.Scatter(x=random_x,
                y=random_y,
                mode='markers',
                name='myScatterPlot',
                marker=dict(
                    size=12,
                    color='rgb(51,23,213)',
                    symbol='square',
                    line=dict(width=2)
                )
                )]

layout=go.Layout(title='Some Scatter plot',xaxis={'title':'the x axis'},yaxis=dict(title='the y axis'),hovermode='closest')

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Generated_HTML_plots/scatter.html')
