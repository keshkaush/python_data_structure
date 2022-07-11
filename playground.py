#interview Question
#a list consist of elements like ["(i1,i2)"] where i2 is the parent of i1check if these elments can form a binary tree
#  
def TreeConstructor(strArr):
    parent_list=list()
    for i in range(len(strArr)):
        c=strArr[i]
        parent_list.append(int(c[3])) #"(i1,i2)" 3rd element is the parent.
        if(i==len(strArr)-1): # this will only execute if all the parents are stored
            for i in range(len(strArr)):
                count=0
                k=parent_list[i]
                #putting parent node in k
                for j in range(len(strArr)):
                    if k == parent_list[j]:
                        count += 1;
                       # print(w[j])
                   # print(f"the present parent {k}")
                if count > 2: # if count exceeds 2 means there are >2 node that have same parent
                    return False
            return True


if __name__ == "__main__":
    strArr = [["(1,2)", "(2,4)", "(7,2)"], ["(1,2)", "(4,4)", "(7,2)"] ]
    res = TreeConstructor(strArr[1]);
    print(res)