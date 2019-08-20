# Distplot - x-axis= Timestamp, y-axis= BTC
# coding=utf-8
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

# Load data
ransomData = pd.read_csv("Edata.csv")

# information about ransomData
ransomData.info()

# set variables
t = ransomData.Timestamp
y = float(ransomData.EUR)

#df = pd.DataFrame({'2012': np.random.randn(200),
#                  '2013': np.random.randn(200)+1})

# draw distplot
fig = ff.create_distplot([ransomData[c] for c in ransomData.columns], ransomData.columns, bin_size=1)

fig.show()