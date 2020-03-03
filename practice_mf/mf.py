import numpy as np
import random
import pandas as pd
import math

class MFx(object):
	#各変数をセット
	def __init__(self,K=20,alpha=1e-6,beta=0.0):
		self.K=K
		self.alpha=alpha
		self.beta=beta

	def fit(self,X,n_user,n_item,n_iter=100):
		self.R=X.copy()
		self.samples=X.copy()

		#潜在要因の変数に初期値を設定
		self.user_factors = np.random.rand(n_user,self.K)
		self.item_factors = np.random.rand(n_item,self.K)

		#stochastic gradient descent
		self.loss=[]
		for i in range(n_iter):
			self.sgd()
			mse=self.mse()
			self.loss.append((i,mse))

	def sgd(self):
		np.random.shuffle(self.samples)
		for user,item,rating in self.samples:
			err=rating-self.predict_pair(user,item)

			#update parameter
			self.user_factors[user] += self.alpha*(err*self.item_factors[item]-self.beta*self.user_factors[user])
			self.item_factors[item] += self.alpha*(err*self.user_factors[user]-self.beta*self.item_factors[item])

	def mse(self):
		predicted = self.predict(self.R)
		error=np.hstack((self.R,np.array(predicted).reshape(-1,1)))
		error=np.sqrt(pow((error[:,2]-error[:,3]),2).mean())
		return error

	#あるユーザのあるアイテムに対する評価値予測（innerはベクトルの内積）
	def predict_pair(self,user,item):
		return np.inner(self.user_factors[user],self.item_factors[item])

	def predict(self,X):
		rate=[]
		for row in X:
			rate.append(self.predict_pair(row[0],row[1]))
		return rate

	def get_full_matrix(self):
		return np.inner(self.user_factors,self.item_factors)

#データ読み込み
def load_ml100k():
	samples=pd.read_csv('data/ml-100k/u.data',sep='\t',header=None)

	samples=samples.iloc[:,:3]
	samples.columns=['user','item','rate']

	samples['user']=samples['user']-1
	samples['item']=samples['item']-1

	return samples

#データセットをarray型に
df = np.array(load_ml100k())

#同じ値を削除し、ユーザ数とアイテム数を数える
n_user=np.unique(df[:,0]).max()+1
n_item=np.unique(df[:,1]).max()+1
n_rate=np.unique(df[:,2]).max()

#順番をランダムに
random.shuffle(df)
#全体のサイズの8割を訓練用、残りをテスト用
train_size=int(df.shape[0]*0.8)
train_df=df[:train_size]
test_df=df[train_size:]

#MF
MF=MFx(K=20,alpha=0.01,beta=0.5)
MF.fit(train_df,n_user,n_item,n_iter=10)

#テストデータのアイテムの評価値を予測
pre=MF.predict(test_df)
#f=np.array(pre)
#print(type(test_df))
#テストデータの評価値の後に、その予測値をもつ行列を作成
ret1=np.hstack((test_df, np.array(pre).reshape(-1, 1)))
#予測値と実際の評価値の平均二乗誤差を出す
print("pred")
print(np.sqrt(pow((ret1[:,2]-ret1[:,3]),2).mean()))

user=[]
x=[]
for i in np.argsort(ret1[:,0]):
    user.append(ret1[i][0])
    x.append(ret1[i])
users=list(set(user))

columns=['user','item','real','pred']

y=pd.DataFrame(data=ret1, columns=columns, dtype='float')

y.set_index("user",inplace=True)

y_rank=y.sort_values(['user','real'],ascending=[True, False])

ndcg=0
fff=users
for ii in fff:
    f=y_rank.loc[ii,"real":"pred"].values.tolist()
    f
    dcg=0.0
    dcg_p=0.0
    s=1
    if type(f[0])==float:
        f=[f]
    for i in f:
       if s==1:
        dcg+=i[1]
        dcg_p+=i[0]
        s+=1
       else:
        dcg+=i[1]/math.log2(s)
        dcg_p+=i[0]/math.log2(s)
        s+=1
    ndcg+=dcg/dcg_p
print("NDCG")
print(ndcg/len(fff))

