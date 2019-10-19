# ファイルをオープンする
test_data = open("delete_set.txt", "r")
test_data2=open("delete_index.txt","r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
inds = test_data2.readlines()

# 一行ずつ表示する
miniline=[]
for ind in inds:
  i=0
  #print(ind)
  for line in lines:
    if (i==int(ind)):
      print(i)
      miniline.append(line)
    i+=1

print(len(miniline))
# ファイルをクローズする
test_data.close()
test_data2.close()

with open("answer_copy2.txt",'wt') as f:
  for ele in miniline:
    f.write(ele)