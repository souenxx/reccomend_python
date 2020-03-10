import pandas as pd

samples=pd.read_csv('big-dvd-df-rated.txt',seq=',',header=None)
samples=samples.iloc[:,:3]
samples.columns=['user','item','rate']

samples['user']=samples['user']-1
samples['item']=samples['item']-1

df=np.array(samples)
