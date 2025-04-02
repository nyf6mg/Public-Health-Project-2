import pandas as pd
import plotly.express as px

df1 = pd.read_csv("./before_school.csv", delimiter=",")
df2 = pd.read_csv("./during_school.csv", delimiter=",")

fig = px.scatter_mapbox(
    df1, lat="accuracy", lon="latitude", title="Before and After School"
)
fig.update_traces(cluster={"enabled": True})

fig.update_layout(mapbox_style="open-street-map")
fig.show()

fig2 = px.scatter_map(df2, lat="accuracy", lon="latitude", title="During School Day")
fig2.update_traces(cluster={"enabled": True})

fig2.update_layout(mapbox_style="open-street-map")
fig2.show()
