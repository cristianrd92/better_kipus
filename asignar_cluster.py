def asignar_cluster(df):
    clusters = list()
    for x in range(len(df)):
        #1
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==1:
            clusters.append(1)
        #2
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==2:
            clusters.append(3)
        #3
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==3:
            clusters.append(3)
        #4
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==1:
            clusters.append(4)
        #5
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==2:
            clusters.append(5)
        #6
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==3:
            clusters.append(6)
        #7
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==1:
            clusters.append(7)
        #8
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==2:
            clusters.append(8)
        #9
        if df.iloc[x]['cluster_b']==1 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==3:
            clusters.append(9)
        #10
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==1:
            clusters.append(10)
        #11
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==2:
            clusters.append(11)
        #12
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==3:
            clusters.append(12)
        #13
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==1:
            clusters.append(13)
        #14
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==2:
            clusters.append(14)
        #15
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==3:
            clusters.append(15)
        #16
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==1:
            clusters.append(16)
        #17
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==2:
            clusters.append(17)
        #18
        if df.iloc[x]['cluster_b']==2 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==3:
            clusters.append(18)
        #19
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==1:
            clusters.append(19)
        #20
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==2:
            clusters.append(20)
        #21
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==1 and df.iloc[x]['cluster_d']==3:
            clusters.append(21)
        #22
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==1:
            clusters.append(22)
        #23
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==2:
            clusters.append(23)
        #24
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==2 and df.iloc[x]['cluster_d']==3:
            clusters.append(24)
        #25
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==1:
            clusters.append(25)
        #26
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==2:
            clusters.append(26)
        #27
        if df.iloc[x]['cluster_b']==3 and df.iloc[x]['cluster_c']==3 and df.iloc[x]['cluster_d']==3:
            clusters.append(27)
    return clusters