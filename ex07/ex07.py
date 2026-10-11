import numpy as np
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)

y0 = np.random.randn(50)
y1 = np.random.randn(50) + 1
y2 = np.random.randn(50) + 2

fig = go.Figure()
fig.add_trace(go.Box(y=y0, name='Distribution 0'))
fig.add_trace(go.Box(y=y1, name='Distribution 1'))
fig.add_trace(go.Box(y=y2, name='Distribution 2'))

fig.update_layout(
    title='Plotly Box Plots - Three Distributions',
    showlegend=True
)
fig.show()