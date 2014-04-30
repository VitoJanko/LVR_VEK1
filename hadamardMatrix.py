from bool import *

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
    index = str(lst[0])
    for l in lst[1:]:
        index+="."+str(l)
    return Var(index)

def EQ(f1,f2):
    #ekvivalenca
    return Or([And([f1,f2]),And([Not(f1),Not(f2)])])

def XOR(f1,f2):
    return Or([And([f1,Not(f2)]),And([Not(f1),f2])])

def transform(b):
    if b:
        return " 1"
    else:
        return "-1"

def visualiseHadamard(square,size):
    for i in range(size):
        s = ""
        for j in range(size):
            if "x."+str(i)+"."+str(j) in square:
                s+= transform(square["x."+str(i)+"."+str(j)])+" "
            else: s+= "   "
        print s
    print 

##    for i in range(size/2*(size-1)):
##        s = ""
##        for j in range(size):
##            if "c."+str(i)+"."+str(j) in square:
##                s+= transform(square["c."+str(i)+"."+str(j)])+" "
##            else: s+= "   "
##        print s
##    print 
##
##    C = [k for (k,v) in square.items() if v and k[0]=="C"]
##    #print C
##    positions = {} 
##    for s in C:
##        positions[(s[2],s[4])] = s[6]
##    #print positions
##    for i in range(size/2*(size-1)):
##        s = ""
##        for j in range(size):
##            if (str(i),str(j+1)) in positions:
##                s+=  " "+positions[(str(i),str(j+1))]+" "
##            else:
##                s+= "   "
##        print s
##    print 
    


