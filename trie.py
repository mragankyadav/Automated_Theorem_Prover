class node:
    def __init__(self, v=None, e=0):
        self.val = v
        self.end = e
        self.children = []
        self.values=[]

    def addChild(self, c):
        self.children.append(c)
    def addValues(self,v):
        self.values.append(v)


def addChild(word, trie=None):
    if trie == None:
        trie = node()
    itr = trie
    for i in range(0, len(word)):
        if (word[i] not in itr.values):
            if (i == len(word) - 1):
                itr.children.append(node(word[i], 1))
                itr.addValues(word[i])
                #print "added end"+word[i]
            else:
                itr.children.append(node(word[i]))
                itr.addValues(word[i])
                #print "added " + word[i]

            itr = itr.children[len(itr.children) - 1]
        else:
            #print itr.values
            #print itr.end
            pos = itr.values.index(word[i])
            itr = itr.children[pos]

    return trie


def findAllChildren(itr, count):
    if itr is None:
        return 0;
    else:
        if itr.end==1:
            count+=1
            #print "bhada"+itr.val
        for i in range(0,len(itr.children)):
            #print count
            count=findAllChildren(itr.children[i],count)
            #print count
        return count


def show(trie):
    for i in range(0,len(trie.children)):
        print str(trie.val) +" "+ str(trie.end)
        show(trie.children[i])

def findChildren(word, trie):
    count = 0
    if (trie == None):
        return 0
    else:
        itr = trie
        for i in range(0, len(word)):
            if (word[i] not in itr.values):
                return count
            else:

                pos = itr.values.index(word[i])

                itr = itr.children[pos]


        count = findAllChildren(itr, count)
        return count


n = int(raw_input().strip())
trief = None
f = file('out.txt', 'w')
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    #print op
    if (trief == None):
        if (op == 'add'):
            trief = addChild(contact)
    else:
        if (op == 'add'):
            trief = addChild(contact, trief)

    if (op == 'find'):
        print >>f, findChildren(contact, trief)

    if(op =="show"):
        show(trief)




















