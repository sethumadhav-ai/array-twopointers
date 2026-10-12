arr=[-7,-3,2,3,11]

left=0
right=len(arr)-1
result=[0]*len(arr)
pos=len(arr)-1

while left <= right:
    if abs(arr[left]) > abs(arr[right]):
        result[pos]=arr[left]**2
        left+=1
    else:
        result[pos]=arr[right]**2
        right-=1

    pos-=1
print(result)