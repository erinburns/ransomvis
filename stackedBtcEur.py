# Stacked Area chart - x-axis= Timestamp, y-axis= BTC
# coding=utf-8
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load data
ransomData = pd.read_csv("Edata.csv")

# information about ransomData
ransomData.info()

# set variables
x = ransomData.Timestamp
btc = ransomData.BTC
eur = ransomData.EUR
usd = ransomData.USD

# draw graph  TODO - change colours
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=btc,
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(150,150,161)'),
    stackgroup='one',
    name="Bitcoin" 
))
fig.add_trace(go.Scatter(
    x=x, y=eur,
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(9,90,122)'),
    stackgroup='one',
    name="Euro" 
))
fig.add_trace(go.Scatter(
    x=x, y=usd,
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(213,61,28)'),
    stackgroup='one',
    name="USD" 
))

fig.update_layout(yaxis_range=(0, 100000000))

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
            text="Amount Paid"
        )
    )
)

fig.show()