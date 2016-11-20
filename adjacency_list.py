array=[]

array.append([1,5])
array.append([1,2])
array.append([1,4])
array.append([2,3])
array.append([2,4])
array.append([3,4])
array.append([4,5])
array.append([5,3])
vertices=5
adj_list=[ [] for i in range(0,vertices+1)]
for i in range(0,len(array)):
    adj_list[(array[i])[0]].append((array[i])[1])

indegree=[0 for x in range(0,vertices+1)]
for i in range(1,vertices+1):
    edges=adj_list[i]
    for j in range(0,len(edges)):
        indegree[edges[j]]+=1




print array
print indegree
print adj_list