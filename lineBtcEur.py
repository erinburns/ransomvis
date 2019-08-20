# Line chart - x-axis= Timestamp, y-axis= BTC
# coding=utf-8
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load data
ransomData = pd.read_csv("Edata.csv")

# information about ransomData
ransomData.info()

# set variables
timestamp = ransomData.Timestamp
btc = ransomData.BTC
eur = ransomData.EUR

# draw graph
fig = go.Figure()
fig.add_trace(go.Scatter(x=timestamp, y=eur, name="Euro", fill='tozeroy'))
fig.add_trace(go.Scatter(x=timestamp, y=btc, name="Bitcoin", fill='tonexty'))

# labels
fig.update_layout(
    title=go.layout.Title(
        text="Ransoms paid over time",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Timestamp of Ransom Payment"
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Amount Paid in Bitcoin and Euros"
        )
    )
)

fig.show()