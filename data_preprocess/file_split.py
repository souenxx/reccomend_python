import numpy as np
import random

file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"
file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"

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
    biglist=[]
    minilist=[]
    i=0
    card=0
    with open(path) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            if i<review_num[card]:
                i++
                minilist.append(line)
            else:
                i=0
                card=card+1
                biglist.append(minilist)
                minilist=[]
                minilist.append(line)
num=review_count(file)
print(num[0])
