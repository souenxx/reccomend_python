path="trans_mter/big-dvd-Arff-efm.txt"

res={"1":0,"2":0,"3":0,"4":0,"5":0}
with open(path) as f:
	for s_line in f:
		i=s_line.split(',')[2]
		res[i]+=1
print(res)
#big-dvd-Arff-efm.txt
#{'1': 123, '2': 232, '3': 548, '4': 925, '5': 695}
