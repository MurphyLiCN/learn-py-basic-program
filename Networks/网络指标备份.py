import numpy as np
import networkx as nx
import pandas as pd
from networkx.algorithms import community
import matplotlib.pyplot as plt


def Grape(df):
    df = np.array(df)
    n = df.shape[0]
    # 有截止的0-1（binomial）无权图
    BG = nx.DiGraph()
    BG.add_nodes_from(range(n))
    limit = np.mean(df) / 10
    for i in range(n):
        for j in range(n):
            if df[i][j] > limit:
                BG.add_edge(i, j)
    # 有向图
    DG = nx.from_numpy_array(df, create_using=nx.DiGraph)
    for node in DG.nodes:
        for nbr in DG.neighbors(node):
            weight = DG[node][nbr]["weight"]
            DG[node][nbr]["distance"] = 1 / weight
    # 无向图
    G = nx.from_numpy_array(df, create_using=nx.Graph)
    return BG, G, DG


if __name__ == '__main__':
    df = pd.read_csv("/Users/murphy/学业/python/学习-复杂网络/数据/hs92_201001.csv", index_col=0)

    BG, G, DG = Grape(df)

    # ～～～～1个数值的指标
    # 节点数
    n = len(DG.nodes)

    # 关系数
    m = len(DG.edges)

    # 平均度
    d = DG.degree
    d_avg = sum(dict(d).values()) / n

    # 平均入度 出度
    d_in = DG.in_degree
    d_out = DG.out_degree
    d_avg_in = sum(dict(d_in).values()) / n
    d_avg_out = sum(dict(d_out).values()) / n

    # 平均局部效率（局部效率：某节点的邻居引起的子图的平均全局效率）
    le = nx.local_efficiency(G)

    # 全局效率
    ge = nx.global_efficiency(G)

    # 密度: m/[n（n-1）]
    density = nx.density(DG)

    # 直径diameter(max距离）
    diameter = nx.diameter(G)

    # 平均路径长度(距离）
    aspl = nx.average_shortest_path_length(G)
    # 加距离平均路径长度(距离）(weight代表距离！！）
    daspl = nx.average_shortest_path_length(G, weight='distance')

    # 网络同配性(度度相关性）
    dac = nx.degree_assortativity_coefficient(DG)
    # 加权网络同配性(度度相关性）
    wdac = nx.degree_assortativity_coefficient(DG, weight='weight')

    # 聚类系数：某一个点的邻居节点的相连程度
    # 平均集聚系数
    ac = nx.average_clustering(G)
    # 全局集聚系数
    trans = nx.transitivity(G)
    # 加权平均集聚系数
    # (weight代表链接强度！！）
    wac = nx.average_clustering(G, weight='weight')

    # ～～～～长度51（节点个数)的有序数据
    # 度
    d = DG.degree
    # 入度 出度
    d_in = DG.in_degree
    d_out = DG.out_degree

    # 集聚系数（点的邻接点之间相互连接的程度）
    cluster = nx.clustering(G)
    # 加权集聚系数（点的邻接点之间相互连接的程度）
    # (weight代表链接强度！！）
    wcluster = nx.clustering(G, weight='weight')

    # 核度(剥洋葱）
    ks = nx.core_number(G)

    # 度中心性 Degree Centrality（邻居多少）
    dc = nx.degree_centrality(DG)
    dc_in = nx.in_degree_centrality(DG)
    dc_out = nx.out_degree_centrality(DG)

    # 特征向量中心性（邻居多少，及邻居的重要性）
    ec = nx.eigenvector_centrality(G)
    # 加权特征向量中心性（邻居多少，及邻居的重要性）
    # (weight代表链接强度！！）
    wec = nx.eigenvector_centrality(G, weight='weight')

    # 二阶中心性（二阶中心度值越低，则表明中心度越高。）
    soc = nx.second_order_centrality(G)

    # 中介中心性 Betweeness centrality（多少最短路经过了它）
    bc = nx.betweenness_centrality(DG)
    # 加距离中介中心性 Betweeness centrality（多少最短路经过了它）
    # (weight代表距离！！）
    dbc = nx.betweenness_centrality(DG, weight='distance')

    # 紧密中心性 Closeness centrality （更几何）
    cc = nx.closeness_centrality(DG)
    # 加距离紧密中心性 Closeness centrality （更几何）
    # (distance代表距离！！）
    dcc = nx.closeness_centrality(DG, distance='distance')

    # 点权（加权度，连边权重和）
    d_weigh_D = nx.degree(DG, weight='weight')
    d_weigh = nx.degree(G, weight='weight')

    # pagerank（需要scipy的版本）
    # pr = nx.pagerank(DG,weight='weight')
    # 单位权： A点单位权 = A点权/A点度
    # to 朱老师：帮忙算一下qwq

    # 权重分布差异性 就是与某个点相连的各个边的权重的标准差。A点权重分布差异性 = 对于A的所有连边B求和：【（B连边的权/A点权）的平方】
    # to 朱老师：帮忙算一下qwq

    # 鲁棒性 connected_components
    # 启发式：最大度（HD）（HDA）K核（k-core）集体影响力（Collective Influence）（桥节点）https://github.com/zhfkt/ComplexCi
    # 强化学习：FINDER https://www.nature.com/articles/s42256-020-0177-2 https://www.linkresearcher.com/theses/ce4bd554-704f-43a8-9c09-ae072d90b3f9
    largest_cc = max(nx.connected_components(G), key=len)

    # 社区划分
    clc = community.louvain_communities(G)
    cgmc = community.greedy_modularity_communities(DG, weight='weight')

