import re

featurelist=[]
entrylist=[]

f=open('otamesi.txt')
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
    print(part[0]+","+part[1]+","+part[2]+",",end="")
    while part[j] != "<":
      print(str(featurelist.index(part[j]))+":"+part[j+1],end="")
      j=j+2
      if part[j] != "<":
        print(" ",end="")
    print("")

#print(featurelist)

j=0
for ff in featurelist:
  print(str(j)+"="+ff)
  j=j+1