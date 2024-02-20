import pandas as pd
import plotly.graph_objects as go
import base64

df = pd.read_csv('filepath/file.csv')


fig.add_trace(go.Bar(x=df['Month/day'], y=df['metric 1'],
                     marker_color='rgb(248, 192, 7)',
                     opacity=0.4,
                     name='name 1',
                     yaxis='y2'))



fig.add_trace(go.Scatter(x=df['Month/day'], y=df['metric 2'],
                         mode='lines',
                         line=dict(color='rgb(34, 149, 253)', width=2, shape='spline'),
                         name='name 2'))



fig.add_trace(go.Scatter(x=df['Month/day'], y=df['metric 3'],
                         mode='lines',
                         line=dict(color='rgb(173, 216, 230)', width=2, shape='spline'),
                         name='name 3'))

# you can use other templates as well // simply search for plotly templates
  
fig.update_layout(title='page title',
                  xaxis_title='x axis title',
                  yaxis_title='y axis title',
                  template='simple_white',
                  legend=dict(x=0, y=1, traceorder='normal', orientation='h'),
                  yaxis=dict(title='title'),
                  yaxis2=dict(title='title', overlaying='y', side='right')
                  )

fig.write_html('filepath/output.html')
