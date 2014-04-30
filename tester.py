from random import *
from bool import *
from sat_solver import *

seznam = ["nnf", "cnf"]
n = 0
def Test(izraz_in):
    izraz=izraz_in.split(":")
    exec("c="+izraz[1])
    print str(izraz[0])
    print str(izraz[1])
    print
    for i in range(len(seznam)):
        exec("b="+izraz[1]+"."+seznam[i]+"()")
        print seznam[i].upper()+": "+str(b)
    print "Poenostavljena CNF oblika:   "+str(cnf(c))
    print "Poenostavljeno: "+str(simplify(c)) 
    print "Resitev SAT-a: ",resi(b)
    
    print "______________________________________________________________________"

f=open("primeri.txt",'r')
primeri = []
for line in f:
    if line.find(":")>0 and line.split(":")[0]!="Primer":
        Test(line.strip("\n"))
    if line.split(":")[0]=="Primer":
        primeri.append(line.strip("\n"))
        n+=1
        

#Test("And([Not(Var('p')), Var('p'),Var('q')])")  
m = randint(0, n)
Test(primeri[-1])

