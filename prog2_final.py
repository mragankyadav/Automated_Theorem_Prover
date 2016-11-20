cls_no = 0
KB=[]
conclusions=[]
from copy import deepcopy
class var:
    def __init__(self,n):
        self.name=n
    def getName(self):
        return self.name

class cons:
    def __init__(self,n):
        self.name=n
    def getName(self):
        return self.name

class function:
    def __init__(self,n,v):
        self.name=n
        self.values=v

    def getName(self):
        return self.name

    def getVariables(self):
        return self.values


class clause:
    def __init__(self,num,p,n):
        self.pos_literals=p
        self.neg_literals=n
        self.clause_no=num
        name = []
        name.append("Positive")
        name.append('(')
        for i in self.getPosLiterals():
            fname = i.getName()
            vars = i.getVariables()
            name.append(fname)
            name.append('(')
            for j in vars:
                if(isinstance(j,cons)):
                    name.append('(')
                    name.append(j.getName())
                    name.append(')')
                else:
                    name.append(j.getName())
                name.append(',')
            del name[len(name) - 1]
            name.append(')')
            name.append(' or ')
        if (name[len(name) - 1] != '('):
            del name[len(name) - 1]
        name.append(')')
        name.append(" Negative ")
        name.append('(')

        for i in self.getNegativeLiterals():
            fname = i.getName()
            vars = i.getVariables()
            name.append(fname)
            name.append('(')
            for j in vars:
                if (isinstance(j, cons)):
                    name.append('(')
                    name.append(j.getName())
                    name.append(')')
                else:
                    name.append(j.getName())
                name.append(',')
            del name[len(name) - 1]
            name.append(')')
            name.append(' or ')
        if (name[len(name) - 1] != '('):
            del name[len(name) - 1]
        name.append(')')
        self.clauseName=''.join(str(i) for i in name)

    def getPosLiterals(self):
        return self.pos_literals

    def getNegativeLiterals(self):
        return self.neg_literals


    def getName(self):
        return self.clauseName
    def getClauseNumber(self):
        return self.clause_no





def KnowledgeBase(kb,conc):
    global KB
    global conclusions
    KB=kb
    conclusions=conc



def unify(l1, l2, s):
    if isinstance(l1, cons) and isinstance(l2, cons) and l1 == l2:
        return s
    elif isinstance(l1, var):
        return unify_var(l1, l2, s)
    elif isinstance(l2, var):
        return unify_var(l2, l1, s)
    elif isinstance(l1, function) and isinstance(l2, function):
        return unify_function(l1.values, l2.values, s)
    else:
        return {}


def unify_var(var, l, s):
    if s.has_key(var):
        return unify(s[var], l, s)
    else:
        occurs_check(var, l)
        s[var] = l
        return s

def occurs_check(variable, l):
        if isinstance(l, var):
            if variable == l:
                return {}
        elif isinstance(l, function):
            for elem in l.values:
                occurs_check(variable, elem)
        else:
            pass


def unify_function(l1, l2, s):
    if len(l1) != len(l2):
        return {}
    else:
        for i in range(len(l1)):
            sub = unify(l1[i], l2[i], s)
        return sub


def substitute( clause_1, clause_2, s):

    pos_function = clause_1.getPosLiterals() + clause_2.getPosLiterals()
    neg_function = clause_1.getNegativeLiterals() + clause_2.getNegativeLiterals()
    if(len(s)>0):
        for key in s:
            for i in pos_function:

                v=i.getVariables()
                for j in range(len(v)):

                    if ( v[j].getName() == key.getName()):
                        v[j] = s[key]
            for i in neg_function:

                v = i.getVariables()
                for j in range(len(v)):

                    if (v[j].getName()== key.getName()):
                        v[j] = s[key]
    return pos_function, neg_function

def add_new_clause(total_clauses,new_clause):
    for i in total_clauses:
        if(cmp((i.getName()),new_clause.getName())==0):
            return total_clauses
    total_clauses.append(new_clause)
    return total_clauses

def resolve( clause_1, clause_2):
    global cls_no
    new_clauses = []
    poshash={}
    neghash={}
    pname=''
    nname=''
    for p, pos in enumerate(clause_2.getPosLiterals()):
        for n, neg in enumerate(clause_1.getNegativeLiterals()):
            if pos.name == neg.name:
                poshash[pos.name]=[pos,p,2]
                pname=pos.name
                neghash[neg.name]=[neg,n,1]
                nname=neg.name

    for p, pos in enumerate(clause_1.getPosLiterals()):
        for n, neg in enumerate(clause_2.getNegativeLiterals()):
            if pos.name == neg.name:
                poshash[pos.name] = [pos,p,1]
                pname = pos.name
                neghash[neg.name] = [neg,n,2]
                nname = neg.name

    if(len(poshash)==1 and len(neghash)==1):
        subst = unify(poshash[pname][0], neghash[nname][0], {})
        cls_no += 1
        c1 = deepcopy(clause_1)
        c2 = deepcopy(clause_2)
        if (poshash[pname][2] == 1):
            del c1.pos_literals[poshash[pname][1]]
        else:
            del c2.pos_literals[poshash[pname][1]]
        if (neghash[nname][2] == 1):
            del c1.neg_literals[neghash[nname][1]]
        else:
            del c2.neg_literals[neghash[nname][1]]

        temp = substitute(c1, c2, subst)
        if(len(temp[0])==1 and len(temp[1])==0 and temp[0][0].getName()=='Answer'):
            return True,temp[0]
        if len(temp[0]) == 0 and len(temp[1]) == 0:
            return True, []
        new_clauses.append(clause(cls_no, temp[0], temp[1]))

    return False, new_clauses

def resolution():
    global cls_no
    outer_loop_start = len(KB)
    total_clauses = KB + conclusions
    cls_no = total_clauses[-1].clause_no + 1

    i = 0
    while (i < outer_loop_start):
        solved, new_clause = resolve(total_clauses[i], total_clauses[outer_loop_start])
        if solved:
            print "FALSE",
            print "from Clause " + str(total_clauses[i].getClauseNumber()) + " and " + "Clause " + str(
                total_clauses[outer_loop_start].getClauseNumber())
            #print "Answer="+new_clause[0].getVariables()[0].getName()
            print "Hence, Proved"
            break
        if new_clause != None:
            for cls in new_clause:
                print str(cls.getClauseNumber())+" "+str(cls.getName()),
                print "from Clause "+str(total_clauses[i].getClauseNumber())+" and "+"Clause "+str(total_clauses[outer_loop_start].getClauseNumber())
                total_clauses=add_new_clause(total_clauses,cls)
        i+= 1
        if i == outer_loop_start:

            outer_loop_start += 1
            i = 0

        pass

#First Question
c1 = clause(1,[function('HOWL',[var('X')])],[function('HOUND',[var('X')])])
c2 = clause(2,[],[function('HAVE',[var('X'),var('Y')]), function('CAT',[var('Y')]), function('HAVE',[var('X'), var('Z')]),
                  function('MOUSE',[var('Z')])])
c3 = clause(3,[],[function('LS',[var('W')]), function('HAVE',[var('W'), var('V')]), function('HOWL',[var('V')])])
c4 = clause(4,[function('HAVE',[cons('John'),cons('a')])], [])
c5 = clause(5, [function('CAT',[cons('a')]), function('HOUND',[cons('a')])], [])
g6 = clause(6, [function('MOUSE',[cons('b')])], [])
g7 = clause(7, [function('LS',[cons('John')])], [])
g8 = clause(8, [function('HAVE',[cons('John'), cons('b')])], [])
KnowledgeBase([c1,c2,c3,c4,c5],[g6,g7,g8])

#Second Question
'''c1 = clause(1, [function('rr',[cons('a')])], [function('coyote',[var('y')])])
c2 = clause(2, [function('chase',[var('z'), cons('a')])], [function('coyote',[var('z')])])
c3 = clause(3, [function('smart',[var('x')])], [function('rr',[var('x')]), function('beep',[var('x')])])
c4 = clause(4, [], [function('coyote',[var('w')]), function('rr',[var('u')]), function('catch',[var('w'), var('u')]), function('smart',[var('u')])])
c5 = clause(5, [function('frustrated',[var('s')]), function('catch',[var('s'), var('t')])], [function('coyote',[var('s')]), function('rr',[var('t')]), function('chase',[var('s'), var('t')])])
c6 = clause(6, [function('beep',[var('r')])], [function('rr',[var('r')])])

g1 = clause(7, [function('coyote',[cons('b')])], [])
g2 = clause(8, [], [function('frustrated',[cons('b')])])

KnowledgeBase([c1,c2,c3,c4,c5,c6],[g1,g2])'''


#ThirdQuestion
'''c1 = clause(1, [function('v',[var('x')]), function('s',[var('x'), function('f',[var('x')])])], [function('e',[var('x')])])
c2 = clause(2, [function('v',[var('y')]), function('c',[function('f', [var('y')])])], [function('e',[var('y')])])
c3 = clause(3, [function('e', [cons('a')])], [])
c4 = clause(4, [function('d', [cons('a')])], [])
c5 = clause(5, [function('d',[var('z')])], [function('s',[cons('a'), var('z')])])
c6 = clause(6, [], [function('d',[var('w')]), function('v',[var('w')])])
g1 = clause(7, [], [function('d',[var('r')]), function('c',[var('r')])])

KnowledgeBase([c1,c2,c3,c4,c5,c6],[g1])'''

'''c1=clause(1,[function('GRANDPARENT',[var('X'),var('Y')])],[function('PARENT',[var('X'),var('Z')]),function('PARENT',[var('X'),var('Y')])])
c2=clause(2,[function('PARENT',[var('X'),var('Y')])],[function('MOTHER',[var('X'),var('Y')])])
c3=clause(3,[function('PARENT',[var('X'),var('Y')])],[function('FATHER',[var('X'),var('Y')])])
c4=clause(4,[function('FATHER',[cons('ZEUS'),cons('ARES')])],[])
c5=clause(5,[function('MOTHER',[cons('HERA'),cons('ARES')])],[])
c6=clause(6,[function('FATHER',[cons('ARES'),cons('HARMONIA')])],[])
g1 = clause(7,[function('Answer',[var('X')])],[function('GRANDPARENT',[var('X'),cons('HARMONIA')])])
KnowledgeBase([c1,c2,c3,c4,c5,c6],[g1])'''
'''q4 = [["GRANDPARENT x y", "-PARENT x z", "-PARENT z y"], ["PARENT x y", "-MOTHER x y"], ["PARENT x y", "-FATHER x y"],
          ["FATHER (ZEUS) (ARES)"], ["MOTHER (HERA) (ARES)"], ["FATHER (ARES) (HARMONIA)"], ["-GRANDPARENT x HARMONIA", "ANSWER x"]]'''
resolution()
