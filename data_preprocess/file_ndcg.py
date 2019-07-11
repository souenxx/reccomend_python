import numpy as np
file = "C:/Users/kidos/desktop/test.txt"
file2 = "C:/Users/kidos/desktop/test2.txt"
#file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"
#file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"

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

def get_ndcg(list1,list2,num_f):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(num_f):
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

main_user='99'

num_f=100

nlist=[]
nclist=[]

flist=get_featurelist(n,main_user)

for user_id in n.keys():
    flist2=get_featurelist(n2,user_id)
    for i in range(num_f):
        name_values = [x['feature'] for x in n[user_id] if x['feature'] == flist2[i]]
        if len(name_values):
            nc[main_user][i]['score']=n[main_user][flist.index(n2[user_id][i]['feature'])]['score']
        else:
            nc[main_user][i]['score']=0
    minilist=[]
    minilistc=[]
    for i in range(num_f):
        minilist.append(float(n[main_user][i]['score']))
        minilistc.append(float(nc[main_user][i]['score']))
    nlist.append(minilist)
    nclist.append(minilistc)

"""
for user_id in n.keys(): 
    minilist=[]
    minilistc=[]
    for i in range(20):
        minilist.append(float(n[user_id][i]['score']))
        minilistc.append(float(nc[user_id][i]['score']))
    nlist.append(minilist)
    nclist.append(minilistc)
#print(nclist[0])
"""
kekka_list=[]
for i in range(len(n.keys())):
    kekka=get_ndcg(nclist[i],nlist[int(main_user)],num_f)
    kekka_list.append(kekka)
#print(kekka_list)
kekka_index=sorted(range(len(kekka_list)),key=lambda k: kekka_list[k],reverse=True)
print(kekka_index.index(int(main_user))+1)
