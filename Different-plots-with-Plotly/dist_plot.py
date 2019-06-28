"""
Distribution plots have 3 plots:
    1) histogram,
    2) Rug plot ,i.e., crowdness on number line ( like |   |   |   |  |  |  | | | |||||||| | | |  |  |   |   |  )
    3) a KDE(Kernel Density function)
"""
import numpy as np
import plotly.figure_factory as ff
import plotly.offline as pyo

x1=np.random.normal(0,3,1000)
x2=np.random.normal(10,3,1000)
x3=np.random.normal(20,3,1000)
x4=np.random.normal(30,3,1000)

fig=ff.create_distplot(hist_data=[x1,x2,x3,x4],group_labels=['x1','x2','x3','x4'],bin_size=[1,2,3,4])
pyo.plot(fig,filename='Generated_HTML_plots/dist_plot.html')
