import numpy as np
import random

file = "C:/Users/kidos/git/reccomend_python/data_preprocess/review_original.txt"

def review_count(path):
    reviewer_list=[]
    user_list=[]
    review_num=[]
    with open(path) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            user_id = s[0]
            if user_id not in user_list:
                user_list.append(user_id)
            reviewer_list.append(user_id)
    for myid in user_list:
        review_num.append(reviewer_list.count(myid))
    return review_num

def review_split(path,review_num):
    list1=[]
    list2=[]
    minilist=[]
    list1mini=[]
    list2mini=[]
    i=0
    card=0
    with open(path) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            #print(line)
            if i<review_num[card]:
                minilist.append(line)
                i=i+1
            else:
                i=0
                z=0
                for key in minilist:
                    z=z+1
                    random.shuffle(minilist)
                    if z<(len(minilist)//2):
                        list1mini.append(key)
                    else:
                        list2mini.append(key)
                list1.append(list1mini)
                list2.append(list2mini)
                list1mini=[]
                list2mini=[]
                minilist=[]
                minilist.append(line)
                card=card+1
                i=i+1
        z=0
        for key in minilist:
            z=z+1
            random.shuffle(minilist)
            if z<(len(minilist)//2):
                list1mini.append(key)
            else:
                list2mini.append(key)
        list1.append(list1mini)
        list2.append(list2mini)
    return list1,list2

num=review_count(file)
l1,l2=review_split(file,num)

with open("split1.txt",'wt') as f:
    for i in range(len(num)):
        l=[]
        l=map(str,l1[i])
        for ele in l:
            f.write(ele)
            
with open("split2.txt",'wt') as f:
    for i in range(len(num)):
        l=[]
        l=map(str,l2[i])
        for ele in l:
            f.write(ele)            
