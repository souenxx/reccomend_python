file = "C:/Users/kidos/Desktop/test.txt"
file2 = "C:/Users/kidos/Desktop/test.txt"

def mydict(path):
    result={}
    with open(file) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            result[(s[0],s[1])]=s[2]
    return result

n=mydict(file)
n2=mydict(file2)

for mykey in n.key():
    if mykey in n2:
        n2[mykey]=n[mykey]
    else:
        n2[mykey]=0
        
 



print(n.values())