print "Enter the tree"
inputtree = raw_input()
inputtree = inputtree.replace('(', ' ( ')
for i in range(0, len(inputtree)):
    if inputtree[i] is not '(':
        continue
    else:
        inputtree = inputtree[i:]
        break
tempList = (inputtree.replace('(', ' ( ')).replace(')', ' ) ')
treeList = ' '.join(tempList.split())
treeList = treeList.split(' ')
for i in range(0, len(treeList)):
    if treeList[i] is not '(' and treeList[i] is not ')':
        treeList[i] = int(treeList[i])
treelen = len(treeList)
head = Node()
parseInputIntoTree(0, head, 1)
print head.children
treeHead = head.children[0]
treeHead.value = maxwithAlpha(treeHead, -sys.maxint - 1, sys.maxint)
print "Path=" + str(treeHead.path)