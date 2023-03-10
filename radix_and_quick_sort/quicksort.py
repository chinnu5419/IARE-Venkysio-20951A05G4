import time
st=time.time()
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
def partition(arr,low,high):
    piv=arr[high]
    s=low-1
    for i in range(low,high):
        if arr[i]<=piv:
            s+=1
            arr[i],arr[s]=arr[s],arr[i]
    arr[s+1],arr[high]=arr[high],arr[s+1]    
    return s+1
arr=[5,7,9,8,2,1]
quicksort(arr,0,len(arr)-1)
print(*arr)
en=time.time()
print(en-st)
