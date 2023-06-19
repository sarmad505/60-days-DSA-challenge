def binarySearch(a,searchKey):
    lowerBound = 0
    upperBound = len(a)-1

    while (True):

        
        mid = int((lowerBound + upperBound )/ 2)

        if searchKey == a[mid]:
            return mid
        elif lowerBound > upperBound:
            return len(a)  
        else:
            if a[mid] < searchKey :
                lowerBound = mid + 1
            else:
                upperBound = mid - 1

searchKey = int(input("Enter search key: "))
a = [2,5,6,7,8,9,20,34]

b= binarySearch(a,searchKey)
print("Found at index: ",b)