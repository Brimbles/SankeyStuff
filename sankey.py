# import plotly.graph_objects as go

# fig = go.Figure(data=[go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = ["A1", "A2", "B1", "B2", "C1", "C2"],
#       color = "blue"
#     ),
#     link = dict(
#       source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
#       target = [2, 3, 3, 4, 4, 5],
#       value = [8, 4, 2, 8, 4, 2]
#   ))])

# fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
# fig.show()

# # Libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.sankey import Sankey
 
# # basic sankey chart
# Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10], labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'], orientations=[-1, 1, 0, 1, 1, 1, 0,-1]).finish()
# plt.title("Sankey diagram with default settings")
