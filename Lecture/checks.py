import pandas as pd
import numpy as np

df = pd.read_excel("BaMFA_Template.xlsx")

# 假设你想按每个 Process Stage 汇总质量流入和流出
# 示例：我们把“Source”为某一节点视为流入，“Destination”为某节点视为流出

nodes = set(df["Source"]).union(set(df["Destination"]))

# Mass Balance
balance = []
for node in nodes:
    inflow = df[df["Destination"] == node]["Quantity"].sum()
    outflow = df[df["Source"] == node]["Quantity"].sum()
    imbalance = inflow - outflow
    balance.append({"Node": node, "Inflow": inflow, "Outflow": outflow, "Balance": imbalance})

balance_df = pd.DataFrame(balance)

# Uncertainty Calculation
def uncertainty_for_node(node):
    flows = df[(df["Source"] == node) | (df["Destination"] == node)]
    weights = flows["Quantity"]
    rel_uncertainties = flows["Uncertainty (%)"] / 100
    combined = np.sqrt((weights * rel_uncertainties) ** 2).sum() / weights.sum()
    return round(combined * 100, 2)

balance_df["Estimated Uncertainty (%)"] = balance_df["Node"].apply(uncertainty_for_node)

print(balance_df)
