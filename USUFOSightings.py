import plotly
import pandas as pd

df = pd.read_csv('UFOSightingsData.csv')

states = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga',
          'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md',
          'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj',
          'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc',
          'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

results = {state.upper(): df['state'].value_counts()[state] for state in states}

data = [dict(
    type='choropleth',
    autocolorscale=False,
    colorscale=[[0, 'rgb(100, 100, 100)'], [1, 'rgb(0, 153, 0)']],
    locations=list(results.keys()),
    z=list(results.values()),
    locationmode='USA-states',
    marker=dict(
        line=dict(
            color='rgb(10,10,10)',
            width=1
        )
    ),
    colorbar=dict(title="UFO Sitings")
)]

layout = dict(
    title='US UFO Sitings',
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(0, 5, 153)',
    )
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename="UFO_Choropleth_Plot.html")
