import re

featurelist=[]
entrylist=[]

f=open('big-dvd-Arff-efm.txt')
line2=f.readlines()
f.close()

for line in line2:
  part=re.split('[,:/ ]',line)
  i=3
  flag=0
  while part[i] != "<":
    if not part[i] in featurelist:
      featurelist.append(part[i])
    flag=1
    i=i+2
  j=3
  if flag:
    strr=part[0]+","+part[1]+","+part[2]+","
    while part[j] != "<":
      strr+=str(featurelist.index(part[j]))+":"+part[j+1]
      j=j+2
      if part[j] != "<":
        strr+=" "
    entrylist.append(strr)

featurelist2=[]
j=0
for ff in featurelist:
  ff=str(j)+"="+ff
  featurelist2.append(ff)
  j=j+1

with open('amazon.entry',mode='w') as f:
  f.write('\n'.join(entrylist))

with open('amazon.featuremap',mode='w') as f:
  f.write('\n'.join(featurelist2))
