# -*- coding: cp1250 -*-
# True je True
# False je False

def simplify(formula):
    return formula.nnf().spl()

def cnf(formula):
    return simplify(formula).cnf()

class Fls():
    def __init__(self):
        pass
    def __repr__(self,priority = 5):
        return "False"
    def vrednost(self,v):
        return False
    def nnf(self):
        return Fls()
    def nnf2(self):
        return Tru()
    def spl(self):
        return Fls()
    def cnf(self):
        return And([Or([Fls()])])
    
    
class Tru():
    def __init__(self):
        pass
    def __repr__(self,priority = 5):
        return "True"
    def vrednost(self,v):
        return True
    def nnf(self):
        return Tru()
    def nnf2(self):
        return Fls()
    def spl(self):
        return Tru()
    def cnf(self):
        return And([Or([Tru()])])


class Var():
    def __init__(self,ime):
        self.ime=ime
    def __repr__(self,priority = 5):
        return str(self.ime)
    def vrednost(self,v):
        return v[self.ime]
    def nnf(self):
        return Var(self.ime)
    def nnf2(self):
        return Not(Var(self.ime))
    def spl(self):
        return Var(self.ime)
    def cnf(self):
        return And([Or([Var(self.ime)])])

class Not():
    def __init__(self,p):
        self.formula=p
    def __repr__(self,priority = 4):
        return "-" + self.formula.__repr__(priority=4)
    def vrednost(self,v):
        return not (self.formula.vrednost(v))
    def nnf(self):
        return self.formula.nnf2()
    def nnf2(self):
        return self.formula.nnf()
    def spl(self):
        return Not(self.formula)
    def cnf(self):
        return And([Or([Not(self.formula)])])

class And():
    def __init__(self,ps):
        self.formula=ps
    def __repr__(self, priority = 1.5):
        s=""
        b=False
        if len(self.formula)==0:
            return "True"
        for p in self.formula:
            if not b:
                s=s+p.__repr__(priority=2)
                b= True
            else:
                s=s+" And "+p.__repr__(priority=2)
        if priority>=2:
            return "("+s+")"
        else:
            return s
    def vrednost(self,v):
        b = True
        for p in self.formula:
            b = b and p.vrednost(v)
        return b
    def nnf(self):
        return And([p.nnf() for p in self.formula])
    def nnf2(self):
        return Or([Not(p).nnf() for p in self.formula])
    def spl(self):
        temp = self.formula
        while True:
            lst = []
            found = False;
            for p in temp:
                if isinstance(p,And):
                    found = True
                    lst = lst + p.formula
                else:
                    lst.append(p)
            temp = lst
            if not found:
                break
        s=sorted([p.spl() for p in temp], key = str)
        lst=[]
        for p in s:
            if str(p)!= "True":
                if len(lst)==0:
                    lst.append(p)
                elif str(p)!=str(lst[-1]):
                   lst.append(p)
        for p in lst:
            if str(p)=="False" or str(p)=="(False)":
                return Fls()
        if len(lst)==0:
            return Tru()
        if len(lst)==1:
            return lst[0].spl()
        #negacija
        for i in range(len(lst)):
            for j in range(i):
                if str(simplify(Not(lst[i])))==str(lst[j]):
                    return False
        #absorpcija
        karmen = []
        for p in lst:
            if isinstance(p,Or):
                removed = False
                for q in p.formula:
                    for p2 in lst:
                        if str(p2)==str(q) and  not removed:
                            karmen.append(p)
                            removed = True
        for p in karmen:
            lst.remove(p)
        return And(lst)

    def cnf(self):
        nove = []
        if len(self.formula)==0:
            return And(Or([Tru()]))
        for f in self.formula:
            c = f.cnf()
            if isinstance(c,And):
                nove+=c.formula
            else:
                print "Neki je slo zelo narobe"
        return And(nove)
        
class Or():
    def __init__(self,ps):
        self.formula=ps
    def __repr__(self,priority=1.5):
        s=""
        b=False
        if len(self.formula)==0:
            return "False"
        for p in self.formula:
            if not b:
                s=s+p.__repr__(priority=2)
                b= True
            else:
                s=s+" Or "+p.__repr__(priority=2)
        if priority>=2:
            return "("+s+")"
        else:
            return s
    def vrednost(self,v):
        b = False
        for p in self.formula:
            b = b or p.vrednost(v)
        return b
    def nnf(self):
        return Or([p.nnf() for p in self.formula])
    def nnf2(self):
        return And([Not(p).nnf() for p in self.formula])
    def spl(self):
        temp = self.formula
        while True:
            lst = []
            found = False;
            for p in temp:
                if isinstance(p,Or):
                    found = True
                    lst = lst + p.formula
                else:
                    lst.append(p)
            temp = lst
            if not found:
                break
        s=sorted([p.spl() for p in temp],key =str)
        lst=[]
        for p in s:
            if str(p)!= "False":
                if len(lst)==0:
                    lst.append(p)
                elif str(p)!=str(lst[-1]):
                   lst.append(p)
        for p in lst:
            if str(p)=="True" or str(p)=="(True)":
                return Tru()
        if len(lst)==0:
            return Fls()
        if len(lst)==1:
            return lst[0].spl()
        #negacija
        for i in range(len(lst)):
            for j in range(i):
                if str(simplify(Not(lst[i])))==str(lst[j]):
                    return True
        #absorpcija
        eva = []
        for p in lst:
            if isinstance(p,And):
                removed = False
                for q in p.formula:
                    for p2 in lst:
                        if str(p2)==str(q) and  not removed:
                            eva.append(p)
                            removed = True
        for p in eva:
            lst.remove(p)
        return Or(lst)

    def cnf(self):
        if len(self.formula)==0:
            return And(Or([]))
        elif len(self.formula)==1:
            return self.formula[0].cnf()
        else:
            vito = self.formula[0].cnf()
            rep = Or(self.formula[1:]).cnf()
            cleni = []
            for f in vito.formula:
                for f2 in rep.formula:
                    cleni.append(Or(f.formula+f2.formula))
            return And(cleni)
                        
    
        

# Vaje 2 #
#==============================================================================
#Prevajanje problemov iz razumljivih na grde

##REPR TUKI NE DELA##


def makeSudoku(template):
    formule = []
    #Vsi pogoji za izpoljena polja 
    for (i,row) in enumerate(template):
        for (j,value) in enumerate(row):
            if value != 0:
                name = str(i)+str(j)+str(value)
                formule.append(Var(name))
    #Pogoji da so vsa polja izpoljnena
    for i in range(9):
        for j in range(9):
            formule.append(Or([str(i)+str(j)+str(k+1) for k in range(9)]))
    #Pogoji da so vse vrstice razlicne
    for row in range(9):
        for e1 in range(9):
            for e2 in range(e1+1,9):
                for c in range(1,10):
                    formule.append(Not(And([Var(str(row)+str(e1)+str(c)),Var(str(row)+str(e2)+str(c))])))
    #Pogoji da so stolpci razlicni
    for column in range(9):
        for e1 in range(9):
            for e2 in range(e1+1,9):
                for c in range(1,10):
                    formule.append(Not(And([Var(str(e1)+str(column)+str(c)),Var(str(e2)+str(column)+str(c))])))
    #Pogoji da so kvadrati razlicni
    for i in range(3):
        for j in range(3):
            for e1 in range(i*3,(i+1)*3):
                for e2 in range(j*3,(j+1)*3):
                    for e3 in range (e1+1,(i+1)*3):
                        for e4 in range(e2+1,(j+1)*3):
                            for c in range(1,10):
                                formule.append(Not(And([Var(str(e1)+str(e2)+str(c)),Var(str(e3)+str(e4)+str(c))])))
    #Pogoji da ima vsak samo stevilko
    for i in range(9):
        for j in range(9):
            for c1 in range(1,10):
                for c2 in range(c1+1,10):
                    formule.append(Not(And([Var(str(i)+str(j)+str(c1)),Var(str(i)+str(j)+str(c2))])))
    return And(formule)

#..................................................................................................

#V spomin na Cabellota, posvecamo ime funkcije
def makeHadamardovaMatrika(n):
    counter = 0
    formule = []
    #Primerjamo vsake dve vrstici
    for i in range(n):
        for j in range(i+1,n):
            #Definiramo spremenljivke tipa c, tako da naredimo XOR med izbranima vrsticama
            for k in range (n):
                c = makeVar(["c",counter,k])
                xor = XOR(makeVar(["x",i,k]),makeVar(["x",j,k]))
                formule.append(EQ(c,xor))
            #Cilj je imeti polovico ujemajocih spremenjlivk
            formule.append(makeVar(["C",counter,n,n/2]))
            #Definiramo omejitve za spremenljivke tipa C
            formule.append(EQ(makeVar(["C",counter,1,0]),Not(makeVar(["c",counter,1]))))
            formule.append(EQ(makeVar(["C",counter,1,1]),makeVar(["c",counter,1])))
            for k in range (n):
                C = makeVar(["C",counter,k,0])
                C2 = makeVar(["C",counter,k-1,0])
                c = makeVar(["c",counter,k])
                formule.append(EQ(C,And([C2, Not(c)])))               
                for m in range(n):
                    C = makeVar(["C",counter,k,m+1])
                    left = And([makeVar(["C",counter,k-1,m+1]),Not(makeVar(["c",counter,k]))])
                    right = And([makeVar(["C",counter,k-1,m]),makeVar(["c",counter,k])])
                    formule.append(EQ(C,Or([left,right])))  
            counter+=1
    return And(formule)

def makeVar(lst):
    index = str(lst[0])
    for l in lst[1:]:
        index+="."+str(l)
    return Var(index)

def EQ(f1,f2):
    #ekvivalenca
    return Or([And([f1,f2]),And([Not(f1),Not(f2)])])

def XOR(f1,f2):
    return Or([And([f1,Not(f2)]),And([Not(f1),f2])])

#===============================================================================
#SAT
def SAT(cnf,spr,cs):
    #spr=spremenljivke, cs=seznam spremenljivk, ki nimajo se vrednosti
    found = True
    while found: 
        cnf = vstavi(cnf,spr,cs)
        found =False
        for formula in cnf:
            if len(formula)==0:
                return False
            if len(formula)==1:
                found = True
                if formula[0][0]=='-':
                    spr[formula[0][1:]]=False
                    if formula[0][1:] in cs:
                        cs.remove(formula[0][1:])
                else:
                    spr[formula[0]]=True
                    if formula[0] in cs:
                        cs.remove(formula[0])
    if len(cnf)==0:
        return spr
    else:
        neReseno = cs[0]
        cs = cs[1:]
        spr[neReseno] = True
        resitev = SAT(cnf, spr, cs)
        if resitev:
           return resitev
        else:
            spr[neReseno] = False
            resitev = SAT(cnf, spr, cs)
            if resitev:
                return resitev
            else:
                return False
        
        

def vstavi(cnf, spr, cd):
    sez=[]
    for formula in cnf:
        podsez=[]
        isTrue = False
        for f in formula:
            found = False
            if f in spr.keys():
                if spr[f]:
                    found =  True
                    isTrue = True
                else:
                    found= True
            if f[1:] in spr.keys():
                if spr[f[1:]]:
                    found =  True
                else:
                    isTrue = True
                    found= True
            if not found:
                podsez.append(f)
        if not isTrue:
            sez.append(podsez)
    return sez
    
def resi(izraz):
    izraz = cnf(izraz)
    cnf1 = [f.formula for f in izraz.formula]
    cs = []
    cnF = []
    for f in cnf1:
        s=[]
        for ff in f:
            if isinstance(ff,Var):
                s.append(ff.ime)
                if ff.ime not in cs:
                    cs.append(ff.ime)
            elif isinstance(ff,Not):
                if isinstance(ff.formula,Var):
                    s.append('-'+ff.formula.ime)
                    if ff.formula.ime not in cs:
                        cs.append(ff.formula.ime)
        cnF.append(s)
    return SAT(cnF, {}, cs)
            
                
            
    
        
        
