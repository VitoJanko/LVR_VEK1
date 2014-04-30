# -*- coding: cp1250 -*-
#================================================================================

#PROGRAM ZA PISENJE LOGIČNIH IZRAZOV

#================================================================================

def simplify(formula):
    #SIMPLIFY(formula) je funkcija za poenostavljanje izjavne formule, na podlagi
    #enacn Boolove algebre. Klice metodi nnf in spl znotraj posameznih razredov.
    return formula.nnf().spl()

def cnf(formula):
    #CNF(formula) je funkcija, ki logicni izraz pretvori v CNF obliko.
    #Funkcija klice metodo cnf znotraj posameznih razredov. 
    return simplify(formula).cnf()

#================================================================================
#RAZREDI ZA DELO Z LOGIČNIMI VEZNIKI

#----------------------------------------------------------------------
#OPIS METOD ZNOTRAJ RAZREDOV:
#nnf():
#   funkcija, ki izraz prevede v "negation normal form", ce ni negiran.
#
#nnf2():
#   funkcija, ki izraz prevede v "negation normal form", ce je negiran.
#
#spl():
#   funkcija, ki izraz poenostavi.
#
#cnf():
#   funkcija, ki izraz prevede v CNF obliko.
#-------------------------------------------------------------------------

class Fls():
    #FLS() je razred, ki predstavlja boolovo vrednost False.
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
    #TRU() je razred, ki predstavlja boolovo vrednost True.
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
    #VAR() je razred, ki predstavlja boolovo spremenljivko.
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
    #NOT() je razred, ki predstavlja negacijo logicnega izraza.
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
    #AND() je razred, ki predstavlja konjunkcijo, sprejme seznam
    #logicnih izrazov, ki jih povezuje.
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
                                    #Notranje in zunanji AND() poenostavimo in zdruzimo v en sam seznam.
        temp = self.formula                 #seznam izrazov, ki nastopajo v AND()
        while True:
            lst = []                        #seznam, ki bo hranil razsirjen seznam
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
                                    #Zavrzemo podovjene spremenljivke in vrednosti Tru().
        s=sorted([p.spl() for p in temp], key = str)
        lst=[]
        for p in s:
            if str(p)!= "True":
                if len(lst)==0:
                    lst.append(p)
                elif str(p)!=str(lst[-1]):
                   lst.append(p)
                                   #Celoten izraz spremenimo v Fls(), ce v seznamu lst nastopa vsaj en Fls(). 
        for p in lst:
            if str(p)=="False" or str(p)=="(False)":
                return Fls()
        if len(lst)==0:
            return Tru()
        if len(lst)==1:
            return lst[0].spl()
                                    #Upostevamo funkcije za negacijo.
        for i in range(len(lst)):
            for j in range(i):
                if str(simplify(Not(lst[i])))==str(lst[j]):
                    return Fls()
                                    #Upostevamo absorpcijo na elementarni ravni.
        karmen = []                         #prazen seznam, spremenljivk, ki jih bomo zavrgli zaradi absorpcije
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
                print "Neki je slo zelo narobe."
        return And(nove)
        
class Or():
    #OR() je razred, ki predstavlja disjunkcijo, sprejme seznam
    #logicnih izrazov, ki jih povezuje.
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
                                    #Notranje in zunanji OR() poenostavimo in zdruzimo v en sam seznam.                    
        temp = self.formula                 #seznam izazov, ki nastopajo v OR()
        while True:
            lst = []                        #seznam, ki bo hranil razsirjeni seznam
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
                                    #Zavrzemo podvojene spremenljivke in vrednosti Fls().
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
                                    #Upostevamo funkcije za negacijo.
        for i in range(len(lst)):
            for j in range(i):
                if str(simplify(Not(lst[i])))==str(lst[j]):
                    return Tru()
                                    #Upostevamo absorbcijo na elementarni ravni.
        eva = []                            #prazen seznam, spremenljivk, ki jih bomo zavrgli zaradi absorpcije
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
            vito = self.formula[0].cnf()        #prvi izraz v formuli
            rep = Or(self.formula[1:]).cnf()
            cleni = []
            for f in vito.formula:
                for f2 in rep.formula:
                    cleni.append(Or(f.formula+f2.formula))
            return And(cleni)
                        
    
        

