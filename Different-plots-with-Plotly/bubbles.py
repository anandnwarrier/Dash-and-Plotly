import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv(r'data\mpg.csv')
data=[go.Scatter(
                    x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],# to specify name for a bubble
                    mode='markers',
                    marker=dict(
                                size=3*df['cylinders'],
                                color=df['weight'],
                                showscale=True
                                )
                )
    ]
layout=go.Layout(title='Bubble chart',xaxis=dict(title='horsepower'),yaxis=dict(title='mpg'),hovermode='closest')
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Generated_HTML_plots/bubbles.html')
