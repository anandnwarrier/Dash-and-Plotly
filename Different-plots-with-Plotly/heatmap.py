import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv(r'data\2010SantaBarbaraCA.csv')

dat=[
       go.Heatmap(
        x=df['DAY'],
        y=df['LST_TIME'],
        z=df['T_HR_AVG'],#z is the color colorscale. It doesn't accept pandas dataframe, so convert into a list
        colorscale='Jet'
        # ,zmin=None, zmax=None # Limits z
        )
    ]
lay=go.Layout(title='Santa Barbara Temperatures')
fig=go.Figure(data=dat,layout=lay)
pyo.plot(fig,filename='Generated_HTML_plots/heatmap.html')
