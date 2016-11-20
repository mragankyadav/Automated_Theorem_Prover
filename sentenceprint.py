def wordPrint(start,l,sent):
	n=len(l)
	if(start>=n):
		print sent
		return
	else:
		if(n>0):
			for i in range(0,len(l[start])):
				wordPrint(start+1,l,sent+" "+l[start][i])
		return
li=[["you", "we"],
        ["have", "are"],
        ["sleep", "eat", "drink"]]
wordPrint(0,li,"")