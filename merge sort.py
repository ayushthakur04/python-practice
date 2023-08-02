#merge sort
def merge(arr):
    if len(arr)>1:
        r=len(arr)//2
        left=arr[:r]
        right=arr[r:]
        
        merge(left)
        merge(right)
        
        i,j,k=0,0,0
        
        while (i<len(left)) and (j<len(right)):
            if left[i]<right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
                k+=1   
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            i+=1
            j+=1

            
arr=[2,5,2,1]
merge(arr)
print(arr)
