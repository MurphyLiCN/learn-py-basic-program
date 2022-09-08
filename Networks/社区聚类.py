import numpy as np
import networkx as nx
import pandas as pd
from networkx.algorithms import community

if __name__ == '__main__':
    df = pd.read_csv("/Users/murphy/学业/python/学习-复杂网络/数据/hs92_201001.csv", index_col=0)
    df = np.array(df)
    DG = nx.from_numpy_array(df, create_using=nx.DiGraph)
    G = nx.from_numpy_array(df, create_using=nx.Graph)

    communities_generator = community.girvan_newman(DG)
    GN = next(communities_generator)
    a_GN = sorted(map(sorted, GN))

    a_KL = community.kernighan_lin_bisection(G, max_iter=20)

    lap = community.asyn_lpa_communities(DG)
    a_lap = sorted(map(sorted, lap))

    label = community.label_propagation_communities(G)
    a_label = sorted(map(sorted, label))

    flu = community.asyn_fluidc(G,5)
    a_flu = sorted(map(sorted, flu))