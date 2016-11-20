def temp(n):
    arr=[]
    arr.append(-1)
    arr.append(0)
    arr.append(1)
    arr.append(1)
    for i in range(4,n):
        for i in range(0,i):
            
        if(i%2!=0):
            arr.append(arr[len(arr)-1])
        else:
            arr.append(arr[i-3]+arr[i-2]+arr[i-1])
    print arr


temp(20)