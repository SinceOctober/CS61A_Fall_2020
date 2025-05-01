import pandas as pd
import plotly.graph_objects as go

# Data for Sankey Diagram (Flow data)
df = pd.read_excel("Biomass_MFA_UK_v2_expanded.xlsx", sheet_name="Flow")

# Create nodes and links for Sankey diagram
labels = list(pd.unique(df[["From", "To"]].values.ravel()))
label_index = {label: i for i, label in enumerate(labels)}
source = df["From"].map(label_index)
target = df["To"].map(label_index)
value = df["Quantity"]

# Generate Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5), label=labels),
    link=dict(source=source, target=target, value=value)
)])

fig.update_layout(title_text="UK Biomass Flow Sankey Diagram", font_size=10)
fig.show()
