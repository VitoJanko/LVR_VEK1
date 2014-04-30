from bool import *
from sat_solver import *
#==========================================================================================

#PROGRAM ZA PREVAJANJE LATINSKIH KVADRATOV IN SUDOKA NA SAT PROBLEM

#==========================================================================================

#Prevajanje problemov iz razumljivih na grde


def makeLatinSquare(n):
    #MAKELATINESQUARE(n) program, ki prevede Latinski kvadrat na SAT problem
    formule = []
    #Vsi pogoji za izponjena polja
    for i in range(n):
        for j in range(n):
            formule.append(Or([Var(str(i)+str(j)+"_"+str(k+1)) for k in range(n)]))
    #Na istem mestu nista dve razlicni vrednosti.
    for i in range(n):
        for j in range(n):
             for k in range(n):
                 for l in range(k+1,n):
                     formule.append(Not(And(
                         [Var(str(i)+str(j)+"_"+str(k+1)),
                          Var(str(i)+str(j)+"_"+str(l+1))])))
    #Vrstica vsebuje vsako vrednost najvec enkrat.
    for row in range(n):
        for e1 in range(n):
            for e2 in range(e1+1,n):
                for c in range(1,n+1):
                    formule.append(Not(And([Var(str(row)+str(e1)+"_"+str(c)),Var(str(row)+str(e2)+"_"+str(c))])))
    #Stolpec vsebuje vsako vrednost najvec enkrat.
    for column in range(n):
        for e1 in range(n):
            for e2 in range(e1+1,n):
                for c in range(1,n+1):
                    formule.append(Not(And([Var(str(e1)+str(column)+"_"+str(c)),Var(str(e2)+str(column)+"_"+str(c))])))

    return And(formule)

def visualiseSquare(square,size):
    #VISUALISESQUARE(square,size) je funkcija za lep izpis resitve Latinskega kvadrata.
    truths = [k for (k,v) in square.items() if v]
    positions = {} 
    for s in truths:
        positions[(s[0],s[1])] = s[3]
    for i in range(size):
        s = ""
        for j in range(size):
            s+= positions[(str(i),str(j))]+" "
        print s
    print
 
def makeSudoku(template):
    #MAKESUDOKU(template) je funkcija, ki sudoku prevede na SAT problem.
    formule = []
    for (i,row) in enumerate(template):
        for (j,value) in enumerate(row):
            if value != 0:
                #Vsi pogoji za izpoljena polja
                formule.append(Var(str(i)+str(j)+str(value)))
            #Pogoji da so vsa polja izpoljnena
            formule.append(Or([Var(str(i)+str(j)+str(k+1)) for k in range(9)]))
    #Na vsakem polju je samo ena vrednost
    for row in range(9):
        for column in range(9):
             for i in range(9):
                 for j in range(i+1,9):
                     formule.append(Not(And([Var(str(row)+str(column)+str(i+1)),
                                             Var(str(row)+str(column)+str(j+1))])))
    #Pogoji da so vse vrstice razlicne
    for row in range(9):
        for column1 in range(9):
            for column2 in range(column1+1,9):
                for c in range(1,10):                   #Vrednost na mestu
                    formule.append(Not(And([Var(str(row)+str(column1)+str(c)),
                                            Var(str(row)+str(column2)+str(c))])))
    #Pogoji da so stolpci razlicni
    for column in range(9):
        for row1 in range(9):
            for row2 in range(row1+1,9):
                for c in range(1,10):
                    formule.append(Not(And([Var(str(row1)+str(column)+str(c)),
                                            Var(str(row2)+str(column)+str(c))])))
    #Pogoji da so kvadrati razlicni
    for row in range(3):
        for column in range(3):
            for e1 in range(row*3,(row+1)*3):
                for e2 in range(column*3,(column+1)*3):
                    for e3 in range (e1+1,(row+1)*3):
                        for e4 in range(e2+1,(column+1)*3):
                            for c in range(1,10):
                                formule.append(Not(And([Var(str(e1)+str(e2)+str(c)),
                                                        Var(str(e3)+str(e4)+str(c))])))
    #Pogoji da ima vsak samo stevilko
    for row in range(9):
        for column in range(9):
            for c1 in range(1,10):
                for c2 in range(c1+1,10):
                    formule.append(Not(And([Var(str(row)+str(column)+str(c1)),
                                            Var(str(row)+str(column)+str(c2))])))
    #print len(formule)
    return And(formule)

def visualiseSudoku(square):
    #VISUALISESUDOKU(square) je funkcija, ki lapo izpise resen sedoku.
    truths = [k for (k,v) in square.items() if v]
    positions = {} 
    for s in truths:
        positions[(s[0],s[1])] = s[2]
    for i in range(9):
        s = ""
        if i%3 == 0 and i!=0:
            print "---------------------"
        for j in range(9):
            if j%3==0 and j!=0:
                s+="| "
            s+= positions[(str(i),str(j))]+" "
        print s
    print

def visualiseTemplate(n1):
    #VISUALISETEMPLATE(square) je funkcija, ki lapo izpise neresen sedoku.
    for i in range(9):
        if i%3==0 and i!=0:
            print "----------------------"
        for j in range(9):
            if j%3==0 and j!=0:
                print "|",
            if n1[i][j]==0:
                print " ",
            else:
                print n1[i][j],
        print
    print

#..................................................................................................
