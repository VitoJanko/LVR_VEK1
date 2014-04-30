from random import *
from bool import *
from sat_solver import *

seznam = ["nnf", "nnf2", "spl", "cnf"]
n = 0
def Test(izraz):
    exec("c="+izraz)
    print str(izraz)
    print "Poenostavljeno: "+str(simplify(c))
    print "V cnf obliki:   "+str(cnf(c))
    
    for i in range(len(seznam)):
        exec("b="+izraz+"."+seznam[i]+"()")
        print seznam[i]+": "+str(b)
    print resi(b)
    print

f=open("primeri.txt",'r')
primeri = []
for line in f:
    if line!="\n":
        primeri.append(line.strip("\n"))
        n+=1
        Test(line.strip("\n"))
    
m = randint(0, n)
Test(primeri[m])

