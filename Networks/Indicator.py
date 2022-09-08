import numpy as np
import networkx as nx
import pandas as pd
import pymssql
from networkx.algorithms import community
from func_timeout import func_set_timeout, FunctionTimedOut


def Connect():
    conn = pymssql.connect(host='localhost', user="ZhuJinyan", password="Zhu2022Jinyan", database="Project")
    cur = conn.cursor()
    if not cur:
        raise (NameError, "Connection failed.")
    else:
        return conn, cur

def indicator(hs, period, regions, df):
    conn, cur = Connect()

    DG = nx.from_numpy_array(df, create_using=nx.MultiDiGraph)
    # 无向图版
    G = nx.from_numpy_array(df)

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
    # diameter = nx.diameter(DG)
    try:
        diameter = nx.diameter(G)
    except Exception:
        diameter = 0
    # 平均路径长度(距离）
    try:
        aspl = nx.average_shortest_path_length(G)
    except Exception:
        aspl = 100
    # 网络同配性(度度相关性）
    dac = nx.degree_assortativity_coefficient(DG)
    # 聚类系数：某一个点的邻居节点的相连程度
    # 平均集聚系数
    ac = nx.average_clustering(G)
    # 全局集聚系数
    trans = nx.transitivity(G)

    try:
        cur.execute("""
            insert into single_indicator (hs, time, nodes, edges, avg_degree, avg_in_degree, avg_out_degree, local_efficiency, 
            global_efficiency, density, diameter, average_shortest_path_length, degree_assortativity_coefficient, average_clustering,
            transitivity) values
            (%s, %s, %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)
        """ % (str(hs), str(period), n, m, d_avg, d_avg_in, d_avg_out, le, ge, density, diameter, aspl, dac, ac, trans))
        conn.commit()
    except Exception:
        pass

    # ～～～～长度51（节点个数)的有序数据
    # 度
    d = DG.degree
    # 入度 出度
    d_in = DG.in_degree
    d_out = DG.out_degree
    # 集聚系数（点的邻接点之间相互连接的程度）
    cluster = nx.clustering(G)
    # 核度(剥洋葱）
    ks = nx.core_number(G)
    # 度中心性 Degree Centrality（邻居多少）
    dc = nx.degree_centrality(DG)
    dc_in = nx.in_degree_centrality(DG)
    dc_out = nx.out_degree_centrality(DG)
    # 特征向量中心性（邻居多少，及邻居的重要性）
    ec = nx.eigenvector_centrality(G)
    # 二阶中心性（二阶中心度值越低，则表明中心度越高。）
    try:
        soc = nx.second_order_centrality(G)
    except Exception:
        soc = [0]*51
    # 中介中心性 Betweeness centrality（多少最短路经过了它）
    bc = nx.betweenness_centrality(DG)
    # 紧密中心性 Closeness centrality （更几何）
    cc = nx.closeness_centrality(DG)
    # 点权（加权度，连边权重和）
    d_weigh = nx.degree(DG, weight='weight')
    # pagerank（需要scipy的版本）
    try:
        pr = nx.pagerank(DG, max_iter=600)
    except Exception:
        pr = [100]*51
    # 单位权（权/度）

    # 权重分布差异性【（各个连边权度/点权）平方求和】（在1/d到1之间？）

    # @func_set_timeout(0.5)
    # def get_clc(G, seed):
    #     clc = community.louvain_communities(G, seed=seed)
    #     return clc
    #
    # clc_success = False
    # seed = 1
    # while not clc_success:
    #     try:
    #         print('try:seed={}'.format(seed))
    #         clc = get_clc(G, seed)
    #         print('success on seed = {}'.format(seed))
    #         clc_success = True
    #     except FunctionTimedOut:
    #         seed += 1
    clc = community.louvain_communities(G)
    CLC = []
    for i in range(51):
        for j, s in enumerate(clc):
            if i in s:
                CLC.append(j+1)
                break

    cgmc = community.greedy_modularity_communities(DG, weight='weight')
    CGMC = []
    for i in range(51):
        for j, s in enumerate(cgmc):
            if i in s:
                CGMC.append(j+1)
                break

    for i in range(51):
        try:
            cur.execute("""
                    insert into multiple_indicator (hs, time, region, degree, in_degree, out_degree, clustering, core_number, degree_centrality,
                    in_degree_centrality, out_degree_centrality, eigenvector_centrality, second_order_centrality, betweenness_centrality,
                    closeness_centrality, degree_weight, pagerank, community_louvain_communities, community_greedy_modularity_communities) values
                    (%s, %s, \'%s\', %d, %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)
                """ % (str(hs), str(period), regions[i], d[i], d_in[i], d_out[i], cluster[i], ks[i], dc[i], dc_in[i], dc_out[i], ec[i], soc[i],
                       bc[i], cc[i], d_weigh[i], pr[i], CLC[i], CGMC[i]))
            conn.commit()
        except Exception:
            pass

    conn.close()
    cur.close()


if __name__ == '__main__':
    df = pd.read_csv(r"D:\ZHUJINYAN\lab\haiguan\UNdata\hs92_201001.csv", index_col=0)
    df = np.array(df)
    DG = nx.from_numpy_array(df, create_using=nx.MultiDiGraph)
    # 无向图版
    G = nx.from_numpy_array(df)

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
    diameter = nx.diameter(DG)
    # 平均路径长度(距离）
    aspl = nx.average_shortest_path_length(G)
    # 网络同配性(度度相关性）
    dac = nx.degree_assortativity_coefficient(DG)
    # 聚类系数：某一个点的邻居节点的相连程度
    # 平均集聚系数
    ac = nx.average_clustering(G)
    # 全局集聚系数
    trans = nx.transitivity(G)


    # ～～～～长度51（节点个数)的有序数据
    # 度
    d = DG.degree
    # 入度 出度
    d_in = DG.in_degree
    d_out = DG.out_degree
    # 集聚系数（点的邻接点之间相互连接的程度）
    cluster = nx.clustering(G)
    # 核度(剥洋葱）
    ks = nx.core_number(G)
    # 度中心性 Degree Centrality（邻居多少）
    dc = nx.degree_centrality(DG)
    dc_in = nx.in_degree_centrality(DG)
    dc_out = nx.out_degree_centrality(DG)
    # 特征向量中心性（邻居多少，及邻居的重要性）
    ec = nx.eigenvector_centrality(G)
    # 二阶中心性（二阶中心度值越低，则表明中心度越高。）
    soc = nx.second_order_centrality(G)
    # 中介中心性 Betweeness centrality（多少最短路经过了它）
    bc = nx.betweenness_centrality(DG)
    # 紧密中心性 Closeness centrality （更几何）
    cc = nx.closeness_centrality(DG)
    # 点权（加权度，连边权重和）
    d_weigh = nx.degree(DG,weight='weight')
    # pagerank（需要scipy的版本）
    pr = nx.pagerank(DG)
    # 单位权（权/度）

    # 权重分布差异性【（各个连边权度/点权）平方求和】（在1/d到1之间？）

    # 鲁棒性 connected_components
    # 启发式：最大度（HD）（HDA）K核（k-core）集体影响力（Collective Influence）（桥节点）https://github.com/zhfkt/ComplexCi
    # 强化学习：FINDER https://www.nature.com/articles/s42256-020-0177-2 https://www.linkresearcher.com/theses/ce4bd554-704f-43a8-9c09-ae072d90b3f9
    largest_cc = max(nx.connected_components(G), key=len)

    # ～～～～长度m（边个数)的有序数据(似乎不好存储）
    # 边介数
    ebc = nx.edge_betweenness_centrality(DG)



    # ～～～～51*51的矩阵
    #  点点距离
