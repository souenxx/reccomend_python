import numpy as np

file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test2.txt"
file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test2c.txt"

def mydict(path):
    user_dict={}
    feature_list=[]
    with open(path) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            user_id = s[0]
            pair={}
            pair['feature']=s[1]
            pair['score']=s[2]
            if user_id not in user_dict:
                user_dict[user_id]=[]
            user_dict[user_id].append(pair)
            #user_dict[user_id].append(pair)
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

def get_featurelist(n,user_id):
    featurelist=[]
    for i in range(len(n[user_id])):
        featurelist.append(n[user_id][i]['feature'])
    return featurelist

n=mydict(file)
nc=mydict(file)
n2=mydict(file2)

for user_id in n.keys():
    for i in range(len(n[user_id])):
        flist=get_featurelist(n,user_id)
        flist2=get_featurelist(n2,user_id)
        name_values = [x['feature'] for x in n2[user_id] if x['feature'] == flist[i]]
        if len(name_values):
            nc[user_id][i]['score']=n2[user_id][flist2.index(name_values[0])]['score']
        else:
            nc[user_id][i]['score']=0
    print(nc)
            
#print(n2['49'])

#nl=list(n.values())

#print(nl)
#nlf=[float(s) for s in nl]

#nl2=list(n2.values())
#nlf2=[float(t) for t in nl2]

#kekka=get_ndcg(nlf,nlf2)

#print(kekka)