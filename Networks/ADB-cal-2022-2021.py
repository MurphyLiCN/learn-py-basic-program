import pymssql
import os
import pandas as pd
import Indicator2

def Connect():
    conn = pymssql.connect(host='10.51.86.201', user="ZhuJinyan", password="Zhu2022Jinyan", database="Networks")
    cur = conn.cursor()
    if not cur:
        raise (NameError, "Connection failed.")
    else:
        return conn, cur

def create_table():
    conn, cur = Connect()

    cur.execute("""
        create table ADB_multiple_indicator(ID int IDENTITY(1, 1),
                                time int not null,
                                country_apartment varchar(20) not null,
                                country varchar(5) not null,
                                apartment varchar(5) not null,
                                source varchar(5) not null,
                                binomial_cutdown int,
                                degree int,
                                in_degree int,
                                out_degree int,
                                clustering float,
                                clustering_weight float,
                                core_number float,
                                degree_centrality float,
                                in_degree_centrality float,
                                out_degree_centrality float,
                                eigenvector_centrality float,
                                eigenvector_centrality_wight float,
                                second_order_centrality float,
                                betweenness_centrality float,
                                betweenness_centrality_distance float,
                                closeness_centrality float,
                                closeness_centrality_distance float,
                                degree_weight_Di float,
                                degree_weight float,
                                pagerank float,
                                largest_connected_components float,
                                d_unit float,
                                d_diff float,
                                shs_constraint float,
                                shs_constraint_weight float,
                                shs_effective_size float,
                                shs_effective_size_weight float,
                                hits float,
                                d_an_o_o_None float,
                                d_an_o_i_None float,
                                d_an_o_io_None float,
                                d_an_i_o_None float,
                                d_an_i_i_None float,
                                d_an_i_io_None float,
                                d_an_io_o_None float,
                                d_an_io_i_None float,
                                d_an_io_io_None float,
                                d_an_o_o_weight float,
                                d_an_o_i_weight float,
                                d_an_o_io_weight float,
                                d_an_i_o_weight float,
                                d_an_i_i_weight float,
                                d_an_i_io_weight float,
                                d_an_io_o_weight float,
                                d_an_io_i_weight float,
                                d_an_io_io_weight float,
                                closeness_vitality float,
                                closeness_vitality_weight float,
                                community_louvain_communities float,
                                community_greedy_modularity_communities float,
                                community_girvan_newman float,
                                c_flu_2 float,
                                c_flu_3 float,
                                c_flu_4 float,
                                c_flu_5 float,
                                c_flu_6 float,
                                c_flu_7 float,
                                c_flu_8 float,
                                c_flu_9 float,
                                community_kernighan_lin_bisection float,
                                community_asyn_lpa_communities float,
                                community_label_propagation_communities float,
                                primary key (time, country_apartment))
    """)
    conn.commit()

    cur.execute("""
        create table single_indicator (ID int IDENTITY(1, 1),
                                time int not null,
                                binomial_cutdown int,
                                nodes int,
                                edges int,
                                avg_degree float,
                                avg_in_degree float,
                                avg_out_degree float,
                                local_efficiency float,
                                global_efficiency float,
                                density float,
                                diameter float,
                                average_shortest_path_length float,
                                average_shortest_path_length_distance float,
                                average_clustering float,
                                average_clustering_weight float,
                                transitivity float,
                                wiener_index float,
                                dac_out_out_None float,
                                dac_out_in_None float,
                                dac_in_out_None float,
                                dac_in_in_None float,
                                dac_out_out_weight float,
                                dac_out_in_weight float,
                                dac_in_out_weight float,
                                dac_in_in_weight float,
                                primary key (time))
    """)
    conn.commit()

    conn.close()
    cur.close()

def cal():
    conn, cur = Connect()

    root = r'D:\ADB-Data\2021-2020'

    for file in os.listdir(root):
        time = file[9:13]

        df = pd.read_excel(os.path.join(root, file), header=[5, 6], na_values=0.0)
        df.fillna(0, inplace=True)
        columns = df.columns.tolist()[4:2209]
        df = df[columns]
        df = df.iloc[:2205]

        dic = Indicator2.main(df)
        for d in dic:

            cur.execute("""
                insert into single_indicator (time, binomial_cutdown, nodes, edges, avg_degree, avg_in_degree, avg_out_degree, local_efficiency,
                global_efficiency, density, diameter, average_shortest_path_length, average_shortest_path_length_distance, 
                average_clustering, average_clustering_weight, transitivity, wiener_index, 
                dac_out_out_None, dac_out_in_None, dac_in_out_None, dac_in_in_None, dac_out_out_weight, dac_out_in_weight, 
                dac_in_out_weight, dac_in_in_weight)
                values(%s, %d, %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)
            """ % (time, d, dic[d][0], dic[d][1], dic[d][2], dic[d][3], dic[d][4], dic[d][5], dic[d][6], dic[d][7], dic[d][8],
                   dic[d][9], dic[d][10], dic[d][11], dic[d][12], dic[d][13], dic[d][14], dic[d][15]['dacoutoutNone'],
                   dic[d][15]['dacoutinNone'], dic[d][15]['dacinoutNone'], dic[d][15]['dacininNone'], dic[d][15]['dacoutoutweight'],
                   dic[d][15]['dacoutinweight'], dic[d][15]['dacinoutweight'], dic[d][15]['dacininweight']))
            conn.commit()

            for i, column in columns:
                country_apartment = column[0] + '_' + column[1]
                country = column[0]
                apartment = column[1]


                cur.execute("""
                             ADB_multiple_indicator(time, country_apartment, country, apartment, source, binomial_cutdown, degree, in_degree, out_degree, 
                             clustering, clustering_weight, core_number, degree_centrality, in_degree_centrality, out_degree_centrality, 
                             eigenvector_centrality, eigenvector_centrality_wight, second_order_centrality, betweenness_centrality, 
                             betweenness_centrality_distance, closeness_centrality, closeness_centrality_distance, degree_weight_Di, degree_weight, pagerank, 
                             largest_connected_components, d_unit, d_diff, shs_constraint, shs_constraint_weight, shs_effective_size, shs_effective_size_weight, 
                             hits, d_an_o_o_None, d_an_o_i_None, d_an_o_io_None, d_an_i_o_None, d_an_i_i_None, d_an_i_io_None, d_an_io_o_None, 
                             d_an_io_i_None, d_an_io_io_None, d_an_o_o_weight, d_an_o_i_weight, d_an_o_io_weight, d_an_i_o_weight, d_an_i_i_weight, 
                             d_an_i_io_weight, d_an_io_o_weight, d_an_io_i_weight, d_an_io_io_weight, closeness_vitality, 
                             closeness_vitality_weight, community_louvain_communities, community_greedy_modularity_communities, 
                             community_girvan_newman, c_flu_2, c_flu_3, c_flu_4, c_flu_5, c_flu_6, c_flu_7, c_flu_8, c_flu_9, 
                             community_kernighan_lin_bisection, community_asyn_lpa_communities, community_label_propagation_communities)
                             values(%s, \'%s\', \'%s\', \'%s\', \'%s\', %d, %d, %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, 
                             %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, 
                             %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)
                        """ % (time, country_apartment, country, apartment, 'ADB', d, dic[d][16][i], dic[d][17][i], dic[d][18][i],
                               dic[d][19][i], dic[d][20][i], dic[d][21][i], dic[d][22][i], dic[d][23][i], dic[d][24][i], dic[d][25][i],
                               dic[d][26][i], dic[d][27][i], dic[d][28][i], dic[d][29][i], dic[d][30][i], dic[d][31][i], dic[d][32][i],
                               dic[d][33][i], dic[d][34][i], dic[d][35][i], dic[d][36][i], dic[d][37][i], dic[d][38][i], dic[d][39][i],
                               dic[d][40][i], dic[d][41][i], dic[d][42][i], dic[d][43]['o_o_None'][i], dic[d][43]['o_i_None'][i],
                               dic[d][43]['o_io_None'][i], dic[d][43]['i_o_None'][i], dic[d][43]['i_i_None'][i], dic[d][43]['i_io_None'][i],
                               dic[d][43]['io_o_None'][i], dic[d][43]['io_i_None'][i], dic[d][43]['io_io_None'][i], dic[d][43]['o_o_weight'][i],
                               dic[d][43]['o_i_weight'][i], dic[d][43]['o_io_weight'][i], dic[d][43]['i_o_weight'][i], dic[d][43]['i_i_weight'][i],
                               dic[d][43]['i_io_weight'][i], dic[d][43]['io_o_weight'][i], dic[d][43]['io_i_weight'][i], dic[d][43]['io_io_weight'][i],
                               dic[d][44][i], dic[d][45][i], dic[d][46][i], dic[d][47][i], dic[d][48][i], dic[d][49]['c_flu_2'][i],
                               dic[d][49]['c_flu_3'][i], dic[d][49]['c_flu_4'][i], dic[d][49]['c_flu_5'][i], dic[d][49]['c_flu_6'][i], dic[d][49]['c_flu_7'][i],
                               dic[d][49]['c_flu_8'][i], dic[d][49]['c_flu_9'][i], dic[d][50][i], dic[d][51][i], dic[d][52][i]))
                conn.commit()

    conn.close()
    cur.close()


if __name__ == '__main__':
    create_table()
    cal()