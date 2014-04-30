from bool import *
#====================================================================================

#HADAMARDOVA OBLIKA ZA SAT solver

#====================================================================================
#Prevajanje problemov iz razumljivih na grde

#V spomin na Cabellota, posvecamo ime funkcije
def makeHadamardovaMatrika(n):
    #MAKEHADEMARDOVAMATRIKA(n) je funkcija, ki problem Hadamardove matrike prevede
    #v obliko za SAT_SOLEVER
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
            formule.append(EQ(makeVar(["C",counter,1,0]),Not(makeVar(["c",counter,0]))))
            formule.append(EQ(makeVar(["C",counter,1,1]),makeVar(["c",counter,0])))
            for m in range (2,n+1):
                formule.append(Not(makeVar(["C",counter,1,m])))
            for k in range (2,n+1):
                C = makeVar(["C",counter,k,0])
                C2 = makeVar(["C",counter,k-1,0])
                c = makeVar(["c",counter,k-1])
                formule.append(EQ(C,And([C2, Not(c)])))
                for m in range(n):
                    C = makeVar(["C",counter,k,m+1])
                    left = And([makeVar(["C",counter,k-1,m+1]),Not(makeVar(["c",counter,k-1]))])
                    right = And([makeVar(["C",counter,k-1,m]),makeVar(["c",counter,k-1])])
                    formule.append(EQ(C,Or([left,right])))
            counter+=1
    return And(formule)

def makeVar(lst):
    #MAKEVAR(lst) je funkvija, ki vrne spremenljivko, ki jo sestavi z lst
    index = str(lst[0])
    for l in lst[1:]:
        index+="."+str(l)
    return Var(index)

def EQ(f1,f2):
    #EQ(f1,f2) je funkcija, ki iz izrazov f1 in f2 naredi izraz za ekvivalenco
    return Or([And([f1,f2]),And([Not(f1),Not(f2)])])

def XOR(f1,f2):
    #XOR(f1,f2) naredi XOR izraz iz izrazov f1 in f2 
    return Or([And([f1,Not(f2)]),And([Not(f1),f2])])

def transform(b):
    #TRANSFORM(b) spremeni boolean spremenljivko v 1 oz -1
    if b:
        return " 1"
    else:
        return "-1"

def visualiseHadamard(square,size):
    #VISUALISEHADEMARD(square,size) je funkcija, ki lepo izpise hademardovo matriko
    for i in range(size):
        s = ""
        for j in range(size):
            if "x."+str(i)+"."+str(j) in square:
                s+= transform(square["x."+str(i)+"."+str(j)])+" "
            else: s+= "   "
        print s
    print 

