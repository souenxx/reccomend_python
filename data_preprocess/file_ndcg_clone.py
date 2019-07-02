file = "test2.txt"
file2 = "test2c.txt"


def mydict(path):
    result={}
    with open(file) as data_file:
        for line in data_file:
            s=list(line.rstrip().split(","))
            result[(s[0],s[1])]=s[2]
    return result

def get_cluster(cluster_path):
    lookup_dict = {}
    aspect_index = {}
    index = 0
    with open(file) as datafile:
        for line in datafile:
            aspect = line.split(":")[0].strip()
            aspect_index[aspect] = index
            index += 1
            features = line.split(":")[1].strip().split(",")
            for feature in features:
                feature = feature.strip();
                lookup_dict[feature] = aspect
    return [lookup_dict, aspect_index]

def get_user_feature_matrix(user_dict, user_index, lookup_dict, aspect_index, N):
    result = np.zeros((len(user_index), len(aspect_index)))
    for key in user_dict.keys():
        index_user = user_index[key]
        user_reviews = user_dict[key]
        count_dict = {}
        for review in user_reviews:
            feature = review[0]
            if feature not in lookup_dict:
                continue
            aspect = lookup_dict[feature]
            if aspect not in count_dict:
                count_dict[aspect] = 0;
            count_dict[aspect] += 1
        for aspect in count_dict.keys():
            index_aspect = aspect_index[aspect]
            count = count_dict[aspect]
            result[index_user, index_aspect] = 1 + (N - 1) * (2 / (1 + exp(-count)) - 1)
    return result

n=mydict(file)
n2=mydict(file2)

[lookup_dict, aspect_index] = get_cluster(feature_cluster_path)
user_feature_matrix = get_user_feature_matrix(user_dict, user_index, lookup_dict, aspect_index, 5)

for mykey in n.keys():
    if mykey in n2:
        n2[mykey]=n[mykey]
    else:
        n2[mykey]=0
        
 
print(n2)


#print(n.keys())