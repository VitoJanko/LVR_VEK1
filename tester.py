from random import *
from bool import *
from sat_solver import *
#===============================================================================

#PROGRAM ZA TESTIRANJE programov bool.py in progarma sat_solver.py

#===============================================================================
seznam = ["nnf", "cnf"]
def Test(izraz_in):
    #TEST(izraz_in) dobi string, ki ima ime primera in ukaz, locen z : in ukaz
    #izpise v NNF, CNF, poenostavljeni CNF in resen problem z SAT-om
    izraz=izraz_in.split(":")
    #spremeni strig v ukaz
    exec("c="+izraz[1])
    #ime izraza potem pa ukaz
    print str(izraz[0])
    print str(izraz[1])
    print
    for i in range(len(seznam)):
        #spremeni string v ukaz ter uporabi funkcije razreda
        exec("b="+izraz[1]+"."+seznam[i]+"()")
        print seznam[i].upper()+": "+str(b)
    print "Poenostavljena CNF oblika:   "+str(cnf(c))
    print "Poenostavljeno: "+str(simplify(c)) 
    print "Resitev SAT-a: ",resi(b)
    
    print "______________________________________________________________________"

#====================================================================================
#Preberi primer z datoteke primeri.txt, izpisi vse, posebne primere (tisti, ki imajo
#ime), ter enega izmed naklucno izbranih poimenovanih Primer.
f=open("primeri.txt",'r')
n = 0
primeri = []
for line in f:
    if line.find(":")>0 and line.split(":")[0]!="Primer":
        Test(line.strip("\n"))
    if line.split(":")[0]=="Primer":
        primeri.append(line.strip("\n"))
        n+=1
        
m = randint(0, n)
Test(primeri[m])

