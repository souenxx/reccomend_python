import numpy as np
import random
#file = "C:/Users/kidos/desktop/efm_f_c.txt"
#file2 = "C:/Users/kidos/desktop/efm_f_c.txt"

file = "C:/Users/kidos/desktop/mbpr_f.txt"
#file2 = "C:/Users/kidos/desktop/efm2_3new.txt"
#file2 = "C:/Users/kidos/desktop/efm3_4new.txt"
#file2 = "C:/Users/kidos/desktop/efm4_5new.txt"
#file2 = "C:/Users/kidos/desktop/mbpr2_3.txt"
#file2 = "C:/Users/kidos/desktop/mbpr3_4.txt"
file2 = "C:/Users/kidos/desktop/mbpr4_5.txt"
#file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"
#file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"

def mydict(path):
    user_dict={}
    user_list=[]
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
                user_list.append(user_id)
            user_dict[user_id].append(pair)
            #user_dict[user_id].append(pair)
    return user_dict,user_list

def get_ndcg(list1,list2,num_f):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(num_f):
        dcg+=get_dcg(list1[i],i+1)
        idcg+=get_dcg(list2[i],i+1)
    #print(dcg)
    #print(idcg)
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

def generate_nlist(n,nc,n2,main_user,num_f):
    nlist=[]
    nclist=[]
    flist=get_featurelist(nc,main_user)
    flist2=[]
    flist2=get_featurelist(n2,main_user)
    for i in range(100):
        name_values=[]
        name_values = [x['feature'] for x in n[main_user] if x['feature'] == flist2[i]]
        if len(name_values):
            nc[main_user][i]['score']=n[main_user][flist.index(n2[main_user][i]['feature'])]['score']
        else:
            nc[main_user][i]['score']=0

    minilist=[]
    minilistc=[]
    minilist_a=[]
    minilistc_a=[]
    for i in range(100):
        minilist.append(float(n[main_user][i]['score']))
        minilistc.append(float(nc[main_user][i]['score']))
    #random.shuffle(minilistc)
    for i in range(num_f):
        minilist_a.append(minilist[i])
        minilistc_a.append(minilistc[i])
    nlist.extend(minilist_a)
    nclist.extend(minilistc_a)
    kekka=get_ndcg(nclist,nlist,num_f)    
    return kekka

def generate_nlist_c(n,nc,n2,main_user,num_f):
    nlist=[]
    nclist=[]
    flist=get_featurelist(nc,main_user)
    for user_id in nc.keys():
        flist2=[]
        flist2=get_featurelist(n2,user_id)
        for i in range(num_f):
            name_values=[]
            name_values = [x['feature'] for x in n[main_user] if x['feature'] == flist2[i]]
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
        #print(nlist)
        #print(nclist)
    kekka=get_ndcg(nclist[int(main_user)],nlist[int(main_user)],num_f)
    #kekka_list=[]
    #for i in range(len(n.keys())):
        #kekka=get_ndcg(nclist[i],nlist[int(main_user)],num_f)
        #kekka_list.append(kekka)
    #kekka_index=sorted(range(len(kekka_list)),key=lambda k: kekka_list[k],reverse=True)
    #result=kekka_index.index(int(main_user))+1
    return kekka

n,u=mydict(file)
nc,uc=mydict(file)
n2,u2=mydict(file2)

num_f=5
goukei=0
for i in u:
    result=generate_nlist(n,nc,n2,i,num_f)
    #print(result)
    goukei=goukei+result
print(goukei/len(u))