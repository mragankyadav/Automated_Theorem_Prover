def sub(s,k,path):
    if len(s)==0:
        print path
        return
    else:
        for i in range(len(s)):
            ch=s[i]
            sub(s[:i]+s[i+1:],k,path+[ch])
sub("abcdef",5,[])