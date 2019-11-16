import numpy as np
import random
#file = "C:/Users/kidos/desktop/efm_f_c.txt"
#file2 = "C:/Users/kidos/desktop/efm_f_c.txt"

#file = "C:/Users/kidos/desktop/mbpr_f.txt"
#file2 = "C:/Users/kidos/desktop/efm2_3new.txt"
#file2 = "C:/Users/kidos/desktop/efm3_4new.txt"
#file2 = "C:/Users/kidos/desktop/efm4_5new.txt"
#file2 = "C:/Users/kidos/desktop/mbpr2_3.txt"
#file2 = "C:/Users/kidos/desktop/mbpr3_4.txt"
#file2 = "C:/Users/kidos/desktop/mbpr4_5.txt"
#file = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"
#file2 = "C:/Users/kidos/git/reccomend_python/data_preprocess/test.txt"

#file="C:/Users/kidos/git/MTER-master/model_variants/feature_ranking_5.txt"
#file2="C:/Users/kidos/git/MTER-master/model_variants/feature_ranking3_3_5.txt"


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
