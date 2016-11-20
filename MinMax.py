import sys
treeList=[]
treelen=0
def parseInput(st):
    global treelen
    global treeList
    inputtree = st
    tempList=(inputtree.replace('(',' ( ')).replace(')',' ) ')
    treeList= ' '.join(tempList.split())
    treeList=treeList.split(' ')
    for i in range(0,len(treeList)):
        if treeList[i] is not '(' and treeList[i] is not ')':
            treeList[i]=int(treeList[i])
    treelen = len(treeList)





class Node:
    def __init__(self,val=None,d=None):
        self.value=val
        self.children=[]
        self.depth=d
        self.path = []

    def addChild(self, c):
        self.children.append(c)

def parseInputIntoTree(i,node,depth):
    while(i<treelen):
        if(treeList[i]=='('):
            child,i=parseInputIntoTree(i+1,Node(None,depth),depth+1)
            node.addChild(child)
        elif(treeList[i]==')'):
            return node,i
        else:
            node.addChild(Node(treeList[i],depth))
        i+=1

def printSubtree(node):
    stk=[]
    substr=''


def cutNodes( Node):
    '''
    Utility function to print min and max cuts
    :param Node: Node from which subtree has to be printed
    :return: lisp-tree formated sub-tree
    '''

    if len(Node.children) == 0:
        return str(Node.value)
    else:
        return '(' + ' '.join([cutNodes(child) for child in Node.children]) + ')'

def maxTree(start):
    maxVal=-sys.maxint-1
    for i in range(0,len(start.children)):
        if(start.children[i].value is not None):
            if(start.children[i].value>maxVal):
                maxVal=start.children[i].value
                start.path = [i + 1] + start.children[i].path
        else:
            tempVal=minTree(start.children[i])
            if(tempVal>maxVal):
                maxVal=tempVal
                start.path = [i + 1] + start.children[i].path
            start.children[i].value=tempVal

    return maxVal


def minTree(start):
    minVal = sys.maxint
    for i in range(0,len(start.children)):
        if (start.children[i].value is not None):
            if (start.children[i].value < minVal):
                minVal = start.children[i].value
                start.path = [i + 1] + start.children[i].path
        else:
            tempVal = maxTree(start.children[i])
            if (tempVal < minVal):
                minVal = tempVal
                start.path = [i + 1] + start.children[i].path
            start.children[i].value = tempVal

    return minVal

def maxwithAlpha(start,alpha,beta):
    maxVal=-sys.maxint-1
    for i in range(0,len(start.children)):
        if(start.children[i].value is not None):
            if(start.children[i].value>maxVal):
                maxVal=start.children[i].value
                start.path = [i + 1] + start.children[i].path
                if (maxVal >= beta):
                    print "Cut after "+cutNodes(start.children[i])+" in subtree "+ cutNodes(start)
                    return maxVal
                alpha = max(maxVal, alpha)
        else:
            tempVal=minwithBeta(start.children[i],alpha,beta)
            if(tempVal>maxVal):
                maxVal=tempVal
                start.path = [i + 1] + start.children[i].path
                if (maxVal >= beta):
                    print "Cut after " + cutNodes(start.children[i]) + " in subtree "+ cutNodes(start)
                    return maxVal
                alpha = max(maxVal, alpha)
            start.children[i].value=tempVal

    return maxVal

def minwithBeta(start,alpha,beta):
    minVal = sys.maxint
    for i in range(0,len(start.children)):
        if (start.children[i].value is not None):
            if (start.children[i].value < minVal):
                minVal = start.children[i].value
                start.path = [i + 1] + start.children[i].path
                if(minVal<=alpha):
                    print "Cut after " + cutNodes(start.children[i]) + " in subtree "+ cutNodes(start)
                    return minVal
                beta=min(minVal,beta)
        else:
            tempVal = maxwithAlpha(start.children[i],alpha,beta)
            if (tempVal < minVal):
                minVal = tempVal
                start.path = [i + 1] + start.children[i].path
                if (minVal <= alpha):
                    print "Cut after " + cutNodes(start.children[i]) + " in subtree "+ cutNodes(start)
                    return minVal
                beta = min(minVal, beta)
            start.children[i].value = tempVal

    return minVal





def mainfunction():
    print "Enter the tree the '(...) format"
    inputtree = raw_input()
    inputtree = inputtree.replace('(', ' ( ')
    for i in range(0, len(inputtree)):
        if inputtree[i] is not '(':
            continue
        else:
            inputtree = inputtree[i:]
            break
    parseInput(inputtree)
    head = Node()
    parseInputIntoTree(0, head, 1)

    treeHead = head.children[0]
    treeHead.value = maxwithAlpha(treeHead, -sys.maxint - 1, sys.maxint)
    print "Path=" + str(treeHead.path)


if __name__ == "__main__":
    mainfunction()