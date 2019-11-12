import re

opinionlist=[]
entrylist=[]

f=open('otamesi_o.txt')
line2=f.readlines()
f.close()

for line in line2:
  part=re.split('[,: ]',line)
  i=4
  flag=0
  while i < len(part):
    if not part[i] in opinionlist:
      opinion=part[i].rstrip('\n')
      opinionlist.append(opinion)
      flag=1
    i=i+2

opinionlist2=[]
j=0
for ff in opinionlist:
  ff=str(j)+"="+ff
  #print(str(j)+"="+ff)
  opinionlist2.append(ff)
  j=j+1
print(opinionlist2)