import pandas as pd

file_path = "./gps_u00.csv"
df = pd.read_csv(file_path)

df_reste = df.reset_index()

filtered_df = df_reste.iloc[:, [0, 4, 5]]

filtered_df["index"] = pd.to_datetime(filtered_df["index"], unit="s")

filtered_df["time"] = filtered_df["index"].dt.time

before_school = filtered_df[
    (filtered_df["time"] < pd.to_datetime("10:00:00").time())
    | (filtered_df["time"] > pd.to_datetime("15:00:00").time())
]

during_school = filtered_df[
    (filtered_df["time"] >= pd.to_datetime("10:00:00").time())
    & (filtered_df["time"] < pd.to_datetime("15:00:00").time())
]

before_school.to_csv("before_school.csv", index=False)
during_school.to_csv("during_school.csv", index=False)

print(filtered_df)

filtered_df.to_csv("filtered_file.csv", index=False)
