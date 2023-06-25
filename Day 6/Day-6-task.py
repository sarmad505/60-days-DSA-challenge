arr1 = ["flower","flight","flow","flavor"]
arr2 = ["dog","cat","hello"]

for i in arr1:
    for j in i[0:2]:
        if j[0:2] == "fl":
            print("yes")
        else:
            print("No")
    print(j,end=" ")