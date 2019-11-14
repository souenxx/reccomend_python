import numpy as np
import random

#file = "C:/Users/kidos/git/reccomend_python/data_preprocess/trans_mter/amazon.entry"
file = "C:/Users/kidos/git/reccomend_python/data_preprocess/trans_mter/amazon.uifwords_entry"

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
    list3=[]
    minilist=[]
    list1mini=[]
    list2mini=[]
    list3mini=[]
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
                    if z<(len(minilist)//3):
                        list1mini.append(key)
                    elif z < (2*len(minilist))//3:
                        list2mini.append(key)
                    else:
                        list3mini.append(key)
                list1.append(list2mini+list3mini)
                list2.append(list3mini+list1mini)
                list3.append(list1mini+list2mini)
                list1mini=[]
                list2mini=[]
                list3mini=[]
                minilist=[]
                minilist.append(line)
                card=card+1
                i=i+1
        z=0
        for key in minilist:
            z=z+1
            random.shuffle(minilist)
            if z< (len(minilist)//3):
                list1mini.append(key)
            elif z< (2*len(minilist))//3:
                list2mini.append(key)
            else:
                list3mini.append(key)
        list1.append(list2mini+list3mini)
        list2.append(list3mini+list1mini)
        list3.append(list1mini+list2mini)
    return list1,list2,list3
    
def write_file(write_file,listt):
  with open(write_file,'wt') as f:
      for i in range(len(num)):
          l=[]
          l=map(str,listt[i])
          for ele in l:
              f.write(ele)
              
num=review_count(file)
l1,l2,l3=review_split(file,num)

write_file("amazon3_1.uifwords_entry",l1)            
write_file("amazon3_2.uifwords_entry",l2)
write_file("amazon3_3.uifwords_entry",l3)
