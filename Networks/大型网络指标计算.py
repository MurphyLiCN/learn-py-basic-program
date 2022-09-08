import numpy as np
import networkx as nx
import pandas as pd
import os
import igraph as ig

df = pd.read_excel('/Users/murphy/学业/python/学习-复杂网络/数据/ADB-MRIO-2021.xlsx', header=[5, 6], na_values=0.0)
df.fillna(0, inplace=True)
columns = df.columns.tolist()[4:2209]
df = df[columns]
df = df.iloc[:2205]

n = df.shape[0]

# 有权图
DG = nx.from_numpy_array(df, create_using=nx.DiGraph)
for node in DG.nodes:
    for nbr in DG.neighbors(node):
        weight = DG[node][nbr]["weight"]
        DG[node][nbr]["distance"] = 1 / weight

G = ig.Graph.from_networkx(DG)