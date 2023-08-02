#binary search
def search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low<=high:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1



arr=[1,2,3,4,5]
x=10

result=search(arr,x)
if result!=-1:
    print(":)")
else:
    print(":(")
