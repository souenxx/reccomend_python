import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
user_ids=[0,1,2,4,5,6,7,8,9,11,58,60,63,67,69,73,82,84,88,89,90,94,95,96,97,98,99,100,101,103,107,110,111,113,115,122,123,129,132,136,141,143,144,151,174,178,179,180,181,185,187,189,190,191,228,235,276,278,279,288,289,290,293,306,308,310,311,314,318,319,320,329,384,395,396,397,398,399,407,409,410,412,426,432,433,442,459,463,464,465,466,468,469,472,473,483,488,497,500,504,508]
#diff_user_id=[84,107,115,136,143,289,314,395,464,497]
#userindex
csv_rank=pd.read_csv(filepath_or_buffer="mbpr_f.csv",encoding="ms932",sep=",")
#csv_rank=pd.read_csv(filepath_or_buffer="efm_f.csv",encoding="ms932",sep=",")
#userid
csv_ans=pd.read_csv(filepath_or_buffer="answer.csv",encoding="ms932",sep=",")

z=0
real_ids=list(set(csv_ans['userid']))
idnum=len(real_ids)
real_ind=[]
for t in range(idnum):
  f=user_ids.index(real_ids[t])
  real_ind.append(f)

goukei=0
kaisu=0
for i in range(101):
  first_index=306*i
  usernum = (csv_ans['userid']==user_ids[i])
  print(i)
  if (usernum.sum()):
    for j in range(z,z+usernum.sum()):
      a_fool=(csv_ans.values[j,1]==csv_rank['feature'])&(csv_rank['userindex']==i)
      if (a_fool.sum()):
        feature_and = csv_rank[(csv_rank['feature']==csv_ans.values[j,1])&(csv_rank['userindex']==i)]
        #print(feature_and.index[0])
        #print(first_index)
        zyuni=(feature_and.index[0]-first_index+1)
        #print(zyuni)
        goukei+=zyuni
        kaisu+=1
  z+=(usernum.sum())
print(goukei/kaisu)
