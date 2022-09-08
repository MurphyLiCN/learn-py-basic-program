import numpy as np
import networkx as nx
import pandas as pd
from infomap import Infomap

df = pd.read_csv("/Users/murphy/学业/python/学习-复杂网络/数据/hs92_201001.csv", index_col=0)
df = np.array(df)
DG = nx.from_numpy_array(df, create_using=nx.MultiDiGraph)

im = Infomap(silent=True, markov_time=0.01)
mapping = im.add_networkx_graph(DG)
im.run()
ci = im.get_dataframe(columns=["node_id", "module_id"])