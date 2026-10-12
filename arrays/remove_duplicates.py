arr = [1,2,3,4,5,6,8,5,2,4]   

arr.sort()

if arr:
    slow=0

    for fast in range(1,len(arr)):
        if arr[fast]!=arr[slow]:
            slow+=1
            arr[slow]=arr[fast]

    print(arr[:slow+1])
else:
    print([])