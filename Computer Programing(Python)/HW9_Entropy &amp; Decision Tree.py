
# à¸“à¸±à¸à¸Šà¸™à¸™ à¸„à¸‡à¹à¸à¹‰à¸§ 6430110921
import math
def get_rows(S, conditions):
    out = []
    if conditions == {} :
        for e in S :
            out.append(e)
        return out
    else:
        for i in range(len(S)) :
            k=0
            for p in conditions :
                if S[i][0][p] == conditions[p] :
                    k +=1
            if k == len(conditions):    
                out.append(S[i])
        return out
def Entropy(S, conditions):
    deta = get_rows(S,conditions)
    all_leaf = []
    for e in deta :
        all_leaf.append(e[1])
    type_leaf = []
    for e in all_leaf :
        if e not in type_leaf :
            type_leaf.append(e)
    count_leaf = []
    for e in type_leaf :
        count = 0
        for k in all_leaf :
            if e == k :
                count += 1
        count_leaf+= [[e,count]]
    lstP_e = []
    for e in count_leaf :
        P_e = e[1]/len(deta)
        lstP_e.append(float(P_e))
    entropy =  0
    for e in lstP_e :
        if e != 0 :
            entropy += float((-(e)) * math.log(e,2) )
        elif e == 0  :
            entropy += 0
    
    return entropy

def Entropy_with_feature(S, conditions, feature_name):
    deta = get_rows(S,conditions)
    all_feature = []
    type_feature = [] 
    count_type = []
    for e in deta :
        all_feature.append(e[0][feature_name])
    for e in all_feature :
        if e not in type_feature :
            type_feature.append(e)
    for k in type_feature :
        count =0
        for e in all_feature:
            if k == e :
                count+=1
            elif k!= e :
                count += 0
        count_type += [[k,count]]
    nS = 0
    for k in count_type :
        nS += int(k[1])
    lst_entopy = []
    for e in count_type:
        entopy =(e[1]/nS)*Entropy(deta, {feature_name:e[0]})
        lst_entopy.append(entopy)
    sub_entropy = 0 
    for e in lst_entopy :
        sub_entropy+= float(e)
    return sub_entropy
