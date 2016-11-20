from collections  import Counter
def rep(s,k,l,m):
    ans=[]
    for i in range(0,len(s)-k+1):
        temp=s[i:i+k]
        if(len(set(temp))>m):
             continue
        else:
            ans.append(temp)
    counts=Counter(ans)
    a,b=counts.most_common(1)[0]
    print b

s="abbdeabbhijabbmn"
k=3
rep(s,k,5,10)
