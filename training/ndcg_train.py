import numpy as np

def get_ndcg(mini_list,mini_list2):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(10):
        dcg += get_dcg(mini_list[i],i+1)
        #print(dcg)
        idcg += get_dcg(mini_list2[i],i+1)
        #print(idcg)

    ndcg = dcg/idcg
    return ndcg

def get_dcg2(rel, rank):
    dcg = (np.power(2.0,rel)-1.0)/(np.log2(rank+1));
    return dcg

def get_dcg(rel, rank):
    if rank==1:
        dcg = rel
    else:
        dcg = rel/(np.log2(rank))
    return dcg

mini_list=[3,3,3,3,3,0,0,0,0,5]
mini_list2=[5,3,3,3,3,3,0,0,0,0]

print(get_ndcg(mini_list,mini_list2))
