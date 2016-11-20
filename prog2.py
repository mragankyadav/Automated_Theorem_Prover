import copy
class TheoremProver:

    def solver(self,KnowledgeBase):
        clauses_count = len(KnowledgeBase)
        second = clauses_count-1
        first = 0
        provedflag=0
        #To control the mail question solver loop. Will terminate only if answer is/is-not found.
        while(True):
            while(first<second):
                #Run for all clauses in KB from first pointer to second pointer
                for i in range(first+1,second+1):
                    resolve_results=self.resolve(KnowledgeBase[first],KnowledgeBase[i])
                    #resolve_results = self.resolve(KnowledgeBase[0], KnowledgeBase[2])
                    if  resolve_results!=None:
                        print resolve_results
                        for i in resolve_results:
                            if len(i)==0:
                                print "Theorem Proved"
                                provedflag=1
                                break
                            else:
                            #print (resolve_results)
                            #Append all new resolved clauses to KnowledgeBase
                            #self.add_new_resolvents(KnowledgeBase,resolve_results)

                                KnowledgeBase.append(i)
                    if(provedflag==1):
                        break

                if(provedflag==1):
                    break

                first+=1
            if (provedflag == 1):
                break
            else:
                if(second+1<len(KnowledgeBase)):
                    second+=1
                    first=0
                else:
                    print "Theorem cannot be Proved"
                    break


    #Add new resolvents to KB after checking the duplication issue
    #def add_new_resolvents(self,KnowledgeBase,resolve_results):

    def isVariable(self,literal):




    #Returns a boolean result if two clauses are same or not
    #def duplicate(self,clause1,clause2):

    #Resolves the two clauses and returns the new resolvent list
    def resolve(self,clause1,clause2):
        func_count={}
        for i in clause1:
            if (i[0] == '-'):
                #print 'here'
                f1 = '-'+str(i[1])
                #print f1
            else:
                f1 = i[0]
            for j in clause2:
                if(j[0]=='-'):
                    f2='-'+str(j[1])
                else:
                    f2=j[0]
                #print f1+" "+f2
                if(self.negate(f1)==f2 or self.negate(f2)==f1):
                    func_count[f1]=i
                    func_count[f2]=j
        #print func_count
        if(len(func_count)==2):
            #call unify
            #generate 2 new clauses clause1 and clause2
            resolvent_set=set()
            for i in clause1:
                resolvent_set.add(i)
            for j in clause2:
                resolvent_set.add(j)
            resolvent=list(resolvent_set)
            resolvent_list=[]
            resolved_flag=0
            for i in range(len(resolvent)):
                for j in range(i,len(resolvent)):
                    if(self.negate(resolvent[i])==resolvent[j] or self.negate(resolvent[j])==resolvent[i]):
                        temp=copy.deepcopy(resolvent)
                        temp.remove(resolvent[i])
                        temp.remove(resolvent[j])
                        resolvent=temp
                        resolved_flag=1
                        #print resolvent
                        break
                if(resolved_flag==1):
                    break
            resolvent_list.append(resolvent)
            return resolvent_list
        else:
            return None



    def negate(self,s):
        s='-'+s
        return s

    def unify(self):



def main():

    #question = [[1, ["P X Y", "R (F X)"], ["Q X (A)"]], [2, ["R (F Z)"], ["P Z (A)"]], [3, ["Q W V"], []]]

    #[Future Task] Adding clause to KB using duplicate checker
    clause1=['P(x)','Q(x)','Z(x)']
    clause2=['R(x)','-Q(x)']
    clause3=['-P(x)']
    clause4 = ['-R(x)']
    conclusion=['-Z(x)']
    '''clause1=['P(x)','R(x)']
    clause2=['-P(x)']
    conclusion=['-R(x)'''
    KB=[]
    KB.append(clause1)
    KB.append(clause2)
    KB.append(clause3)
    KB.append(clause4)
    KB.append(conclusion)

    solution=TheoremProver()
    solution.solver(KB)




if __name__ == "__main__":
    main()