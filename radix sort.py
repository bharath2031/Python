def counting_sort(arr,exp):
    m = max(arr)
    count=[0]*(m+1)
    for i in arr:
        count[i]+=1
    i=0
    for c in range(m+1):
        while count[c]>0:
            arr[i]=c
            i+=1
            count[c]-=1
def radix_sort(arr):
    max_ele=max(arr)
    exp=1
    while max_ele//exp>0:
        counting_sort(arr,exp)
        exp*=10
arr=list(map(int,input("enter the element").split()))
radix_sort(arr)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
