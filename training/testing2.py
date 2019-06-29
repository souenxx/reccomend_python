import get_matrices
import train
import numpy as np
import random

def get_user_care(user_id, user_index, aspect_index, user_feature_matrix):
    user_i = user_index[user_id]
    for k, v in aspect_index.items():
        print k + " : " + str(user_feature_matrix[user_i, v])

def get_item_care(product_id, product_index, aspect_index, product_feature_matrix):
    user_i = product_index[product_id]
    for k, v in aspect_index.items():
        print k + " : " + str(product_feature_matrix[user_i, v])

def top_k(product_index, user_id, X, Y, A, user_index, user_feature_matrix, k, alpha,aspect_index):
    user_i = user_index[user_id]
    print ('user_i=\n'+str(user_i))
    user_care = user_feature_matrix[user_i, :]
    print ('user_care=\n'+str(user_care))
    idx = np.argpartition(user_care, -k)
    #print ('idx=\n'+str(idx))
    idx = idx[-k:]
    #print ('idx=\n'+str(idx))
    #idx = np.argsort(user_care)[::-1]
    for i in range(10):
        aspect_id = get_aspect_id(aspect_index, idx[i])
        print ('aspect_id=\n'+str(aspect_id))
    print ('idx=\n'+str(idx))
    R_i = np.zeros(Y.shape[0])
    print ('R_i=\n'+str(R_i))
    for i in range(R_i.shape[0]):
        tmp = X[user_i, idx].dot(Y[i, idx].T) / k / 5.0
        R_i[i] = tmp * alpha + (1 - alpha) * A[user_i, i]
    print ('R_i=\n'+str(R_i))
    idx = np.argpartition(R_i, -3)
    print ('idx=\n'+str(idx))
    idx = idx[-3:]
    print ('idx=\n'+str(idx))
    item_id = get_item_id(product_index, idx[-1])
    print ('item_id=\n'+str(item_id))
    return item_id

def top_feature(a,user_id, user_id2, X_,X_x,user_index, aspect_index, user_index2):
    user_i = user_index[user_id]
    user_i2 = user_index2[user_id2]
    #user_ix = user_index2[user_idx]
    #user_i = 0
    #print ('user_i=\n'+str(user_i))
    user_care = X_[user_i, :]
    user_care2 = X_x[user_i2, :]
    #user_care3 = X_[user_i3, :]
    #user_care4 = X_[user_i4, :]
    #user_care5 = X_[user_i5, :]
    #user_care6 = X_[user_i6, :]
    #print('a=\n'+str(a))
    #user_carex = X_x[user_ix, :]
    print ('user_care=\n'+str(user_care))
    print ('user_care2=\n'+str(user_care2))
    #print ('user_feature_matrix=\n'+str(user_feature_matrix))
    #print ('X_=\n'+str(X_))
    #print aspect_index
    #print user_care
    idx = np.argsort(user_care)[::-1]
    idx2 = np.argsort(user_care2)[::-1]
    #idxx = random.sample(idx,len(idx))
    #idxx = np.argsort(user_carex)[::-1]
    #print user_care
    #print('idx=\n'+str(idx))
    #print('idx2=\n'+str(idx2))
    #print aspect_index
    dcg=0
    idcg=0
    #print('a=\n'+str(a))
    for i in range(a):
        #print('i=\n'+str(i))
        aspect_id = get_aspect_id(aspect_index, idx[i])
        aspect_id2 = get_aspect_id(aspect_index, idx2[i])
        #print('a=\n'+str(a))
        #aspect_value = get_aspect_value(aspect_index, idx[i])
        dcg += get_dcg2(user_care2[idx[i]],i+1)
        #print('user_care2[idx[i]]\n'+str(user_care2[idx[i]]))
        #print('dcg=\n'+str(get_dcg2(user_care2[idx[i]],i+1)))
        #print('dcg_total=\n'+str(dcg))
        idcg += get_dcg2(user_care2[idx2[i]],i+1)
        #print('user_care2[idx2[i]]=\n'+str(user_care2[idx2[i]]))
        #print('idcg=\n'+str(get_dcg2(user_care2[idx2[i]],i+1)))
        #print('idcg_total=\n'+str(idcg))
        print ('aspect_id=\n'+str(aspect_id))
        print ('aspect_id2=\n'+str(aspect_id2))
        #print ('aspect_value=\n'+str(aspect_value))
    #print ('ndcg=\n'+str(dcg/idcg))
    ndcg = dcg/idcg
    return ndcg

def top_feature_random(user_i, user_id2, X_,X_x,user_index, aspect_index, user_index2):
    #user_i = user_index[user_id]
    user_i2 = user_index2[user_id2]
    #user_ix = user_index2[user_idx]
    #user_i = 0
    #print ('user_i=\n'+str(user_i))
    user_care = X_[user_i, :]
    user_care2 = X_x[user_i2, :]
    #user_care3 = X_[user_i3, :]
    #user_care4 = X_[user_i4, :]
    #user_care5 = X_[user_i5, :]
    #user_care6 = X_[user_i6, :]

    #user_carex = X_x[user_ix, :]
    #print ('user_care=\n'+str(user_care))
    #print ('user_feature_matrix=\n'+str(user_feature_matrix))
    #print ('X_=\n'+str(X_))
    #print aspect_index
    #print user_care
    idx = np.argsort(user_care)[::-1]
    idx2 = np.argsort(user_care2)[::-1]
    #random.shuffle(user_care)
    #idxx = np.argsort(user_carex)[::-1]
    #print user_care
    #print idx
    #print idxx
    #print aspect_index
    most_f_random = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,5)
    most_f_random_10 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,10)
    most_f_random_15 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,15)
    most_f_random_20 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,20)
    most_f_random_25 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,25)
    most_f_random_30 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,30)
    most_f_random_35 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,35)
    most_f_random_40 = get_ndcg(aspect_index,idx,idx2,user_care,user_care2,40)

    return most_f_random,most_f_random_10,most_f_random_15,most_f_random_20,most_f_random_25,most_f_random_30,most_f_random_35,most_f_random_40

def get_ndcg(aspect_index,idx,idx2,user_care,user_care2,a):
    dcg=0
    idcg=0
    ndcg=0
    for i in range(a):
        aspect_id = get_aspect_id(aspect_index, idx[i])
        aspect_id2 = get_aspect_id(aspect_index, idx2[i])
        #print('a=\n'+str(a))
        dcg += get_dcg2(user_care2[idx[i]],i+1)
        #print('user_care2[idx[i]]\n'+str(user_care2[idx[i]]))
        #print('dcg=\n'+str(dcg))
        idcg += get_dcg2(user_care2[idx2[i]],i+1)
        #print('user_care2[idx2[i]]=\n'+str(user_care2[idx2[i]]))
        #print('idcg=\n'+str(idcg))
        #print ('aspect_id=\n'+str(aspect_id))
        #print ('aspect_id2=\n'+str(aspect_id2))

    ndcg = dcg/idcg
    return ndcg


def get_item_id(product_index, index):
    for k, v in product_index.items():
        if v == index:
            return k

def get_aspect_id(aspect_index, index):
    for k, v in aspect_index.items():
        if v == index:
            return k

def get_dcg2(rel, rank):
    dcg = (np.power(2.0,rel)-1.0)/(np.log2(rank+1));
    return dcg

def get_dcg(rel, rank):
    if rank==1:
        dcg = rel
    else:
        dcg = rel/(np.log2(rank))
    return dcg

def random_pertition(files):
    for f in files:
        if random.random() >= 0.3:
            print(train_file,f)
    else:
        print(test_file,f)

if __name__ == "__main__":
    feature_cluster_path = "../data/Cell_Phones_and_Accessories_5/feature-cluster.txt"
    reviews_path = "../data/Cell_Phones_and_Accessories_5/extractedReviews.txt"
    train_path = "../data/Cell_Phones_and_Accessories_5/train4.txt"
    test_path = "../data/Cell_Phones_and_Accessories_5/test4.txt"
    neg_entries = "../data/Cell_Phones_and_Accessories_5/opinion-lexicon-English/negative-words.txt"
    pos_entries = "../data/Cell_Phones_and_Accessories_5/opinion-lexicon-English/positive-words.txt"
    [lookup_dict, aspect_index] = get_matrices.get_cluster(feature_cluster_path)
    print(train_path)
    #print aspect_index
    #print aspect_index.values()
    #print [lookup_dict, aspect_index]
    #[user_dict, product_dict] = get_matrices.get_reviews(reviews_path)
    [user_dict, product_dict] = get_matrices.get_reviews(train_path)
    [user_dict2, product_dict2] = get_matrices.get_reviews(test_path)
    #[user_dict3, product_dict3] = get_matrices.get_reviews(userb_path)
    #[user_dict4, product_dict4] = get_matrices.get_reviews(userc_path)
    [user_index, product_index] = get_matrices.get_index(user_dict, product_dict)
    [user_index2, product_index2] = get_matrices.get_index(user_dict2, product_dict2)
    #[user_index3, product_index3] = get_matrices.get_index(user_dict3, product_dict3)
    #[user_index4, product_index4] = get_matrices.get_index(user_dict4, product_dict4)
    user_item_matrix = get_matrices.get_user_item_matrix(train_path, user_index, product_index)
    user_item_matrix2 = get_matrices.get_user_item_matrix(test_path, user_index2, product_index2)
    #user_item_matrix3 = get_matrices.get_user_item_matrix(userb_path, user_index3, product_index3)
    #user_item_matrix4 = get_matrices.get_user_item_matrix(userc_path, user_index4, product_index4)
    user_feature_matrix = get_matrices.get_user_feature_matrix(user_dict, user_index, lookup_dict, aspect_index, 5)
    user_feature_matrix2 = get_matrices.get_user_feature_matrix(user_dict2, user_index2, lookup_dict, aspect_index, 5)
    user_feature_matrix_count = get_matrices.get_user_feature_matrix_count(user_dict2, user_index2, lookup_dict, aspect_index, 5)
    #user_feature_matrix3 = get_matrices.get_user_feature_matrix(user_dict3, user_index3, lookup_dict, aspect_index, 5)
    #user_feature_matrix4 = get_matrices.get_user_feature_matrix(user_dict4, user_index4, lookup_dict, aspect_index, 5)

    neg_dict = get_matrices.get_entries(neg_entries, -1)
    pos_dict = get_matrices.get_entries(pos_entries, 1)
    product_feature_matrix = get_matrices.get_product_feature_matrix(product_dict, product_index, lookup_dict, aspect_index, 5,
                                                        neg_dict, pos_dict)
    product_feature_matrix2 = get_matrices.get_product_feature_matrix(product_dict2, product_index2, lookup_dict, aspect_index, 5,
                                                        neg_dict, pos_dict)
    #product_feature_matrix3 = get_matrices.get_product_feature_matrix(product_dict3, product_index3, lookup_dict, aspect_index, 5,
                                                        #neg_dict, pos_dict)
    #product_feature_matrix4 = get_matrices.get_product_feature_matrix(product_dict4, product_index4, lookup_dict, aspect_index, 5,
                                                        #neg_dict, pos_dict)
    #u_id = user_index["A10UHQH1YL5Q6B"]
    #p_id = product_index["B00HH7MAUW"]
    #p_id = product_index["B00BGG5LO2"]
    #user_item_matrix[u_id, p_id] = 0
    [U1, U2, V, H1, H2] = train.training(user_item_matrix, user_feature_matrix, product_feature_matrix, 50, 50, 0.01, 0.01, 0.01, 0.01, 0.01, 5000, 0.002)
    [U1x, U2x, Vx, H1x, H2x] = train.training(user_item_matrix2, user_feature_matrix2, product_feature_matrix2, 50, 50, 0.01, 0.01, 0.01, 0.01, 0.01, 5000, 0.002)
    #[U1y, U2y, Vy, H1y, H2y] = train.training(user_item_matrix3, user_feature_matrix3, product_feature_matrix3, 50, 50, 0.01, 0.01, 0.01, 0.01, 0.01, 5000, 0.002)
    #[U1z, U2z, Vz, H1z, H2z] = train.training(user_item_matrix4, user_feature_matrix4, product_feature_matrix4, 50, 50, 0.01, 0.01, 0.01, 0.01, 0.01, 5000, 0.002)


    X_ = U1.dot(V.T)
    Y_ = U2.dot(V.T)
    A_ = U1.dot(U2.T) + H1.dot(H2.T)

    X_x = U1x.dot(Vx.T)
    Y_x = U2x.dot(Vx.T)
    A_x = U1x.dot(U2x.T) + H1x.dot(H2x.T)
    '''
    X_y = U1y.dot(Vy.T)
    Y_y = U2y.dot(Vy.T)
    A_y = U1y.dot(U2y.T) + H1y.dot(H2y.T)
    X_z = U1z.dot(Vz.T)
    Y_z = U2z.dot(Vz.T)
    A_z = U1z.dot(U2z.T) + H1y.dot(H2z.T)

    print A_[u_id, p_id]
    print user_item_matrix
    most_rec = top_k(product_index, "AYB4ELCS5AM8P", X_, Y_, A_, user_index, user_feature_matrix, 5, 1.0)
    most_rec = top_k(product_index, "A10UHQH1YL5Q6B", X_, Y_, A_, user_index, user_feature_matrix, 5, 1.0,aspect_index)
    print most_rec
    print get_user_care("A10UHQH1YL5Q6B", user_index, aspect_index, user_feature_matrix)
    print get_item_care(most_rec, product_index, aspect_index, product_feature_matrix)
    most_f = top_feature(product_index, "A1E1LEVQ9VQNK", X_, Y_, A_, user_index, user_feature_matrix, 5,aspect_index)
    most_f = top_feature(product_index2, "A1E1LEVQ9VQNK", X_x, Y_x, A_x, user_index2, user_feature_matrix2, 5,aspect_index)
    '''

    user_id_list5=["A1E1LEVQ9VQNK","A1EVV74UQYVKRY","A1F7YU6O5RU432","A1ODOGXEYECQQ8","A1PI8VBCXXSGC7","A1U11IP6K6NHAK","A1UQBFCERIP7VJ","A1W415JP5WEAJK","A2BLFCOPSMBOZ9","A2BYV7S1QP2YIG",
                   "A2D1LPEUCTNT8X","A2LTYEYGKBYXRR","A2NOW4U7W3F7RI","A2NYK9KWFMJV4Y","A2WLNSZ9U0T1S3","A3A4ZAIBQWKOZS","A3AYSYSLHU26U9","A3EXWV8FNSSFL6","A3NEAETOSXDBOM","A3NHUQ33CFH3VM",
                   "A3OXHLG6DIBRW8","A3PCEB9ND82AGE","A3R19YKNL641X3","A3V5F050GVZ56Q","A3TAS1AG6FMBQW","A10UHQH1YL5Q6B","A10ZFE6YE0UHW8","A18U49406IPPIJ","A22CW0ZHY3NJH8","A23GFTVIETX7DS",
                   "A25C2M3QF9G7OQ","A36K2N527TXXJN","A328S9RN3U5M68","A680RUE1FDO8B","AAOYA0DKWED4W","ABDR6IJ93HFIO","ACJT8MUC0LRF0","ADLVFFE4VBT8","ARBKYIVNYWK3C","AT53ZTTO707MB",
                   "AVPNQUVZWMDSX","AWPODHOB4GFWL","AYB4ELCS5AM8P","AZMY6E8B52L2T"]

    user_id_list1=["A1E1LEVQ9VQNK","A1EVV74UQYVKRY","A1F7YU6O5RU432","A1ODOGXEYECQQ8","A1PI8VBCXXSGC7","A1U11IP6K6NHAK","A1UQBFCERIP7VJ","A1W415JP5WEAJK","A2BLFCOPSMBOZ9","A2BYV7S1QP2YIG","AVPNQUVZWMDSX"]

    user_id_list2=["A2D1LPEUCTNT8X","A2LTYEYGKBYXRR","A2NOW4U7W3F7RI","A2NYK9KWFMJV4Y","A2WLNSZ9U0T1S3","A3A4ZAIBQWKOZS","A3AYSYSLHU26U9","A3EXWV8FNSSFL6","A3NEAETOSXDBOM","A3NHUQ33CFH3VM","AWPODHOB4GFWL"]

    user_id_list3=["A3OXHLG6DIBRW8","A3PCEB9ND82AGE","A3R19YKNL641X3","A3V5F050GVZ56Q","A3TAS1AG6FMBQW","A10UHQH1YL5Q6B","A10ZFE6YE0UHW8","A18U49406IPPIJ","A22CW0ZHY3NJH8","A23GFTVIETX7DS","AYB4ELCS5AM8P"]

    user_id_list=["A25C2M3QF9G7OQ","A36K2N527TXXJN","A328S9RN3U5M68","A680RUE1FDO8B","AAOYA0DKWED4W","ABDR6IJ93HFIO","ACJT8MUC0LRF0","ADLVFFE4VBT8","ARBKYIVNYWK3C","AT53ZTTO707MB","AZMY6E8B52L2T"]



    user_id_list0=["A1E1LEVQ9VQNK"]

    most_f = []
    most_f_10 = []
    most_f_15 = []
    most_f_20 = []
    most_f_25 = []
    most_f_30 = []
    most_f_35 = []
    most_f_40 = []
    '''
    most_fcount = []
    most_f_10count = []
    most_f_15count = []
    most_f_20count = []
    most_f_25count = []
    most_f_30count = []
    most_f_35count = []
    most_f_40count = []
    '''
    a=0
    for i in range(len(user_id_list)):

        most_f.append(top_feature(5,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_10.append(top_feature(10,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_15.append(top_feature(15,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_20.append(top_feature(20,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_25.append(top_feature(25,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_30.append(top_feature(30,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_35.append(top_feature(35,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        most_f_40.append(top_feature(40,user_id_list[i],user_id_list[a],X_, X_x, user_index, aspect_index, user_index2))
        '''
        most_fcount.append(top_feature(5,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_10count.append(top_feature(10,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_15count.append(top_feature(15,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_20count.append(top_feature(20,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_25count.append(top_feature(25,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_30count.append(top_feature(30,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_35count.append(top_feature(35,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        most_f_40count.append(top_feature(40,user_id_list[i],user_id_list[0], X_,user_feature_matrix_count,user_index, aspect_index, user_index2))
        '''
    user_i = user_index[user_id_list[0]]
    random.shuffle(X_[user_i, :])


    most_f_random = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random2 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random3 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random4 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random5 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random6 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random7 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random8 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random9 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random10 = top_feature_random(user_i,user_id_list[a],X_, X_x, user_index, aspect_index, user_index2)
    '''

    most_f_random = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random2 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random3 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random4 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random5 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random6 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random7 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random8 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random9 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    random.shuffle(X_[user_i, :])
    most_f_random10 = top_feature_random(user_i,user_id_list[0],X_, user_feature_matrix_count, user_index, aspect_index, user_index2)
    '''
    #most_f_random_15 = top_feature_random(15,user_id_list[0],user_id_list[0],X_, X_x, user_index, aspect_index, user_index2)
    #most_f_random_25 = top_feature_random(25,user_id_list[0],user_id_list[0],X_, X_x, user_index, aspect_index, user_index2)
    #most_f_random_35 = top_feature_random(35,user_id_list[0],user_id_list[0],X_, X_x, user_index, aspect_index, user_index2)
    #most_f_random_40 = top_feature_random(40,user_id_list[0],user_id_list[0],X_, X_x, user_index, aspect_index, user_index2)


    print('most_f=\n'+str(most_f))
    print('most_f_10=\n'+str(most_f_10))
    print('most_f_15=\n'+str(most_f_15))
    print('most_f_20=\n'+str(most_f_20))
    print('most_f_25=\n'+str(most_f_25))
    print('most_f_30=\n'+str(most_f_30))
    print('most_f_35=\n'+str(most_f_35))
    print('most_f_40=\n'+str(most_f_40))
    '''
    print('most_fcount=\n'+str(most_fcount))
    print('most_f_10count=\n'+str(most_f_10count))
    print('most_f_15count=\n'+str(most_f_15count))
    print('most_f_20count=\n'+str(most_f_20count))
    print('most_f_25count=\n'+str(most_f_25count))
    print('most_f_30count=\n'+str(most_f_30count))
    print('most_f_35count=\n'+str(most_f_35count))
    print('most_f_40count=\n'+str(most_f_40count))
    '''
    print('most_f_random=\n'+str(most_f_random))
    print('most_f_random2=\n'+str(most_f_random2))
    print('most_f_random3=\n'+str(most_f_random3))
    print('most_f_random4=\n'+str(most_f_random4))
    print('most_f_random5=\n'+str(most_f_random5))
    print('most_f_random6=\n'+str(most_f_random6))
    print('most_f_random7=\n'+str(most_f_random7))
    print('most_f_random8=\n'+str(most_f_random8))
    print('most_f_random9=\n'+str(most_f_random9))
    print('most_f_random10=\n'+str(most_f_random10))

    #print('most_f_random_40=\n'+str(most_f_random_40))
    #for i in range(len(user_id_list)):
        #print('most_f'+str(i)+'=\n'+str(most_f[i]))

    #for i in range(len(user_id_list)):
        #print('most_f'+str(i)+'_15=\n'+str(most_f_15[i]))

    #for i in range(len(user_id_list)):
        #print('most_f'+str(i)+'_25=\n'+str(most_f_25[i]))

    #for i in range(len(user_id_list)):
        #print('most_f'+str(i)+'_35=\n'+str(most_f_35[i]))

    #for i in range(len(user_id_list)):
        #print('most_f'+str(i)+'_40=\n'+str(most_f_40[i]))
    #most_f3 = top_feature(X_z, X_x, user_index4, user_feature_matrix4,aspect_index, user_index2, user_feature_matrix2)
    #most_f2 = top_feature("A1PI8VBCXXSGC7","A1E1LEVQ9VQNK", X_x,user_index3, user_feature_matrix3,aspect_index, user_index2, user_feature_matrix2)
