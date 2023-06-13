arr = [1,2,3,4,5,6,7]
order = 3

for i in range(0,order,1):
    for j in range(len(arr)-1,0,-1):
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp

print(arr)