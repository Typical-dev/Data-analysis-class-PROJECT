import csv
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("attempt.csv")
student_df = df.loc[df["level"] == "Level 4"]
print(student_df.groupby("student_id")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = student_df.groupby("student_id")["attempt"].mean(),
    #y = ["level 1", "level 2", "level 3", "level 4"],
    orientation = "h"
))
fig.show()

