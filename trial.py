from copy import deepcopy
cls_no = 0
is_a = isinstance
class variable(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class constant(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '('+self.name+')'

class predicate(object):
    def __init__(self, name, members):
        self.name = name
        self.members = members
    def __str__(self):
        tostr = ''
        if len(self.members) > 0:
            tostr = ' '.join([m.__str__() for m in self.members])
        return '('+self.name+' '+tostr+')'

class UnifyError(Exception):
    pass

class clauses(object):
    def __init__(self, clause_no, pos_clauses, neg_clauses):
        self.clause_no = clause_no
        self.pos_clauses = pos_clauses
        self.neg_clauses = neg_clauses

    def __str__(self):
        pos_cls = ''
        neg_cls = ''
        for fnc in self.pos_clauses:
            pos_cls += fnc.__str__()
        for fnc in self.neg_clauses:
            neg_cls += fnc.__str__()
        return '('+str(self.clause_no)+' ('+pos_cls+') ('+neg_cls+') )'

class task(object):
    def __init__(self, all_clauses, goal_clauses):
        self.all_clauses = all_clauses
        self.goal_clauses = goal_clauses

    def __str__(self):
        print "-----------------Given Clauses------------------"
        for elem in self.all_clauses:
            print elem
        print "-------------------Goal Clauses-----------------"
        for elem in self.goal_clauses:
            print elem
        return "-------------Resolution starts here-------------"

    def unify(self, x, y, substitution):
        if is_a(x, constant) and is_a(y, constant) and x == y:
            return substitution
        elif is_a(x, variable):
            return self.unify_var(x, y, substitution)
        elif is_a(y, variable):
            return self.unify_var(y, x, substitution)
        elif is_a(x, predicate) and is_a(y, predicate):
            if x.name != y.name:
                raise UnifyError(x, y, substitution)
            else:
                return self.unify_predicate(x.members, y.members, substitution)
        elif is_a(x, list) and is_a(y, list):
            return self.unify_predicate(x, y, substitution)
        else:
            raise UnifyError(x, y, substitution)

    def unify_var(self, var, x, substitution):
        if substitution.has_key(var):
            return self.unify(substitution[var], x, substitution)
        else:
            self.occurs_check(var, x)
            substitution[var] = x
            return substitution

    def occurs_check(self, var, x):
        if is_a(x, variable):
            if var == x:
                raise UnifyError
        elif is_a(x, predicate):
            for elem in x.members:
                self.occurs_check(var, elem)
        else:
            pass

    def unify_predicate(self, x, y, substitution):
        if len(x) != len(y):
            raise UnifyError
        else:
            for i in range(len(x)):
                subst = self.unify(x[i],y[i], substitution)
            return subst

    def apply_substitution(self, clause_1, clause_2, subst):
        pos_pred = clause_1.pos_clauses+clause_2.pos_clauses
        neg_pred = clause_1.neg_clauses+clause_2.neg_clauses
        for key in subst:
            for pos in clause_1.pos_clauses: #pos--predicate
                pos_pred = [subst[key] if elem == key else elem for elem in pos_pred]
                neg_pred = [subst[key] if elem == key else elem for elem in neg_pred]
        return pos_pred, neg_pred

    def resolve(self, clause_1, clause_2):
        global cls_no
        new_clauses = []
        ans = set()
        for p,pos in enumerate(clause_2.pos_clauses):
            for n,neg in enumerate(clause_1.neg_clauses):
                if pos.name == neg.name:
                    subst = self.unify(pos, neg,{})
                    if len(subst):
                        cls_no += 1
                        c1 = deepcopy(clause_1)
                        c2 = deepcopy(clause_2)
                        del c1.neg_clauses[n]
                        del c2.pos_clauses[p]
                        temp = self.apply_substitution(c1, c2, subst)
                        if len(temp[0]) == 0 and len(temp[1]) == 0:
                            return True, []
                        new_clauses.append(clauses(cls_no, temp[0], temp[1]))
        for p,pos in enumerate(clause_1.pos_clauses):
            for n,neg in enumerate(clause_2.neg_clauses):
                if pos.name == neg.name:
                    subst = self.unify(pos, neg,{})
                    if len(subst):
                        cls_no += 1
                        c1 = deepcopy(clause_1)
                        c2 = deepcopy(clause_2)
                        del c1.pos_clauses[p]
                        del c2.neg_clauses[n]
                        temp = self.apply_substitution(c1, c2, subst)
                        if len(temp[0]) == 0 and len(temp[1]) == 0:
                            return True, []
                        new_clauses.append(clauses(cls_no, temp[0], temp[1]))
        return False, new_clauses

    def resolution(self):
        global cls_no
        outer_loop_start = len(self.all_clauses)
        total_clauses = self.all_clauses + self.goal_clauses
        cls_no = total_clauses[-1].clause_no + 1
        print self
        i = 0
        while (i < outer_loop_start):
            solved, new_clause = self.resolve(total_clauses[i], total_clauses[outer_loop_start])
            if solved:
                print "FALSE"
                print "Hence, Proved"
                break
            if new_clause != None:
                for cls in new_clause:
                    print cls
                    total_clauses.append(cls)
            i+= 1
            if i == outer_loop_start:
                outer_loop_start += 1
                i = 0
        pass

c1 = clauses(1,[predicate('HOWL',[variable('X')])],[predicate('HOUND',[variable('X')])])
c2 = clauses(2,[],[predicate('HAVE',[variable('X'),variable('Y')]), predicate('CAT',[variable('Y')]), predicate('HAVE',[variable('X'), variable('Z')]),
                   predicate('MOUSE',[variable('Z')])])
c3 = clauses(3,[],[predicate('LS',[variable('W')]), predicate('HAVE',[variable('W'), variable('V')]), predicate('HOWL',[variable('V')])])
c4 = clauses(4, [predicate('HAVE',[constant('John'),constant('a')])], [])
c5 = clauses(5, [predicate('CAT',[constant('a')]), predicate('HOUND',[constant('a')])], [])
g6 = clauses(6, [predicate('MOUSE',[constant('b')])], [])
g7 = clauses(7, [predicate('LS',[constant('John')])], [])
g8 = clauses(8, [predicate('HAVE',[constant('John'), constant('b')])], [])

t = task([c1,c2,c3,c4,c5],[g6,g7,g8])
print t
t.resolution()

