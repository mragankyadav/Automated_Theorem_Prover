def abcd(s,x):
    ans=[]
    temp=[]
    for i in range(0,len(s)):
        if(i+x<len(s)):
            temp.append(s[i:i+x])
    print temp
    for i in range(0,len(temp)):
        ans.append(min(temp[i]))
    print max(ans)

abcd([3,1,1,1],2)