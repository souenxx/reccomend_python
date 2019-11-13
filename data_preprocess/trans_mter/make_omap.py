import re

opinionlist=[]
entrylist=[]

f=open('big-dvd-Arff-cmf-sim_only_pos.txt')
line2=f.readlines()
f.close()

for line in line2:
  part=re.split('[,: ]',line)
  i=4
  while i < len(part):
    if not part[i] in opinionlist:
      opinion=part[i].rstrip('\n')
      if not opinion in opinionlist:
        opinionlist.append(opinion)
    i=i+2

opinionlist2=[]
j=0
for ff in opinionlist:
  ff=str(j)+"="+ff
  #print(str(j)+"="+ff)
  opinionlist2.append(ff)
  j=j+1

with open('amazon.wordmap',mode='w') as f:
  f.write('\n'.join(opinionlist2))