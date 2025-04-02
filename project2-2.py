import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px

df = pd.read_csv("./during_school.csv")
lat = df["accuracy"]
lon = df["latitude"]

min_latitude = 43.69
max_latitude = 43.75
min_longitude = -72.35
max_longitude = -72.25

filtered_data = df[
    (df["accuracy"] >= min_latitude)
    & (df["accuracy"] <= max_latitude)
    & (df["latitude"] >= min_longitude)
    & (df["latitude"] <= max_longitude)
]

coords = np.array(list(zip(filtered_data["accuracy"], filtered_data["latitude"])))

kmeans = KMeans(n_clusters=10)
filtered_data["cluster"] = kmeans.fit_predict(coords)

fig = px.scatter_mapbox(
    filtered_data,
    lat="accuracy",
    lon="latitude",
    color="cluster",
    color_continuous_scale=px.colors.qualitative.Plotly,
    title="K-Means Clustering of GPS Data During School",
    mapbox_style="carto-positron",
    zoom=10,
)

fig.show()


df2 = pd.read_csv("./before_school.csv")
lat = df2["accuracy"]
lon = df2["latitude"]

filtered_data2 = df2[
    (df2["accuracy"] >= min_latitude)
    & (df2["accuracy"] <= max_latitude)
    & (df2["latitude"] >= min_longitude)
    & (df2["latitude"] <= max_longitude)
]

coords2 = np.array(list(zip(filtered_data2["accuracy"], filtered_data2["latitude"])))

kmeans2 = KMeans(n_clusters=10)
filtered_data2["cluster"] = kmeans2.fit_predict(coords2)

fig2 = px.scatter_mapbox(
    filtered_data2,
    lat="accuracy",
    lon="latitude",
    color="cluster",
    color_continuous_scale=px.colors.qualitative.Plotly,
    title="K-Means Clustering of GPS Data After School",
    mapbox_style="carto-positron",
    zoom=10,
)

fig2.show()
