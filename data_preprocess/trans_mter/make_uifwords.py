import re

def make_dict(mapfile):

  f=open(mapfile)
  line2=f.readlines()
  f.close

  flist=[]

  for line in line2:
    part=re.split('=',line)
    part[1]=part[1].rstrip('\n')
    flist.append(part)
    
  return dict(flist)


fmap=make_dict('amazon.featuremap')
omap=make_dict('amazon.wordmap')

uifwlist=[]
keys=[]

f=open('big-dvd-Arff-cmf-sim_only_pos.txt')
line2=f.readlines()
f.close

for line in line2:
  part=re.split('[,: ]',line) 
  i=3
  while i < len(part):
    part[i+1]=part[i+1].rstrip('\n')
    keys = [k for k, v in fmap.items() if v == part[i]]
    feature=keys[0]
    keys = [k for k, v in omap.items() if v == part[i+1]]
    opinion=keys[0]
    parts=part[0]+","+part[1]+","+feature+","+opinion+","+str(int(part[0])+1)
    uifwlist.append(parts)
    i+=2

with open('amazon.uifwords_entry',mode='w') as f:
  f.write('\n'.join(uifwlist))