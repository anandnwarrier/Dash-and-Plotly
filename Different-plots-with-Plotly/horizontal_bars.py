import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df=pd.read_csv(r'data\mocksurvey.csv')
print(df)

data=[go.Bar(y=df['Unnamed: 0'],x=df[column],orientation='h',name=column) for column in df.columns[1:]]
layout=go.Layout(title='Mock survey',xaxis=dict(title='index'),barmode='stack')
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Generated_HTML_plots/horizontal_bars.html')
