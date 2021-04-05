import csv
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("attempt.csv")
print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = df.groupby("student_id")["attempt"].mean(),
    y = ["student 1", "student 2", "student 3", "student 4", "student 5","student 6","student 7", "student 8", "student 9", "student 10", "student 11", "student 12"],
    orientation = "h"
))
fig.show()
