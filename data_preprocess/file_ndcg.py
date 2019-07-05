import numpy as np

file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test2.txt"
file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test2c.txt"

def mydict(path):
    user_dict=[]
    with open(path) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            user_id = s[0]
            if user_id not in user_dict:
                user_dict.append(user_id)
            #user_dict[user_id][(s[0],s[1])] = s[2] 
    return user_dict

def get_ndcg(list1,list2):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(10):
        dcg+=get_dcg(list1[i],i+1)
        idcg+=get_dcg(list2[i],i+1)
        
    ndcg=dcg/idcg
    return ndcg

def get_dcg2(rel, rank):
    dcg=(np.power(2.0.rel)-1.0)/(np.log2(rank+1))
    return dcg
    
def get_dcg(rel,rank):
    if rank==1:
        dcg=rel
    else:
        dcg=rel/(np.log2(rank))
    return dcg
    



n=mydict(file)
n2=mydict(file2)


print(n)
#for mykey in n.keys():
    #if mykey in n2:
        #print(mykey)
        #n2[mykey]=n[mykey]
    #else:
        #n2[mykey]=0

#nl=list(n.values())
#nlf=[float(s) for s in nl]

#nl2=list(n2.values())
#nlf2=[float(t) for t in nl2]

#kekka=get_ndcg(nlf,nlf2)

#print(kekka)