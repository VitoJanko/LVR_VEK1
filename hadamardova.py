#Prevajanje problemov iz razumljivih na grde

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
            
                
            
    
        
        
