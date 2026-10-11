import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

returns = np.random.randn(50)
price = 100 + np.cumsum(returns)

dates = pd.date_range(start='2020-09-01', periods=50, freq='B')
df = pd.DataFrame(zip(dates, price), columns=['Date', 'Company_A'])

# Plotly Express
fig_express = px.line(df, x='Date', y='Company_A', title='Company A Stock Price (Plotly Express)')
fig_express.update_layout(xaxis_title='Date', yaxis_title='Price')
fig_express.show()

# Plotly Graph Objects
fig_go = go.Figure()
fig_go.add_trace(go.Scatter(x=df['Date'], y=df['Company_A'], mode='lines', name='Company_A'))
fig_go.update_layout(
    title='Company A Stock Price (Graph Objects)',
    xaxis_title='Date',
    yaxis_title='Price'
)
fig_go.show()