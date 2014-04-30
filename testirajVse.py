from bool import *
seznam = [".nnf", ".nnf2", ".spl", ".cnf"]

def Test(izraz):
    for i in range(len(seznam)):
        exec("b="+izraz+seznam[i]+"()")
        print str(b)+"   "+seznam[i]
        
