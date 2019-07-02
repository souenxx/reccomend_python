file = "test2.txt"
file2 = "test2c.txt"

def mydict(path):
    result={}
    with open(file) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            result[(s[0],s[1])] = s[2] 
    return result

def ndcg(list1,list2):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(10):
        dcg+=get_dcg(mini_list[i],i+1)
        idcg+=get_dcg(mini_list2[i],i+1)
        
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

for mykey in n.keys():
    if mykey in n2:
        n2[mykey]=n[mykey]
    else:
        n2[mykey]=0
        
 

print(n2)

#print(n.keys())