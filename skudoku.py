from bool import *
from sat_solver import *
#Prevajanje problemov iz razumljivih na grde

def makeLatinSquare(n):
    formule = []
    for i in range(n):
        for j in range(n):
            formule.append(Or([Var(str(i)+str(j)+"_"+str(k+1)) for k in range(n)]))
    for i in range(n):
        for j in range(n):
             for k in range(n):
                 for l in range(k+1,n):
                     formule.append(Not(And(
                         [Var(str(i)+str(j)+"_"+str(k+1)),
                          Var(str(i)+str(j)+"_"+str(l+1))])))
    for row in range(n):
        for e1 in range(n):
            for e2 in range(e1+1,n):
                for c in range(1,n+1):
                    formule.append(Not(And([Var(str(row)+str(e1)+"_"+str(c)),Var(str(row)+str(e2)+"_"+str(c))])))

    for column in range(n):
        for e1 in range(n):
            for e2 in range(e1+1,n):
                for c in range(1,n+1):
                    formule.append(Not(And([Var(str(e1)+str(column)+"_"+str(c)),Var(str(e2)+str(column)+"_"+str(c))])))

    return And(formule)

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
            formule.append(Or([Var(str(i)+str(j)+str(k+1)) for k in range(9)]))
    #Na vsakem polju je samo ena vrednost
    for i in range(9):
        for j in range(9):
             for k in range(9):
                 for l in range(k+1,9):
                     formule.append(Not(And(
                         [Var(str(i)+str(j)+str(k+1)),
                          Var(str(i)+str(j)+str(l+1))])))
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
