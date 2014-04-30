from bool import *
seznam = ["nnf", "nnf2", "spl", "cnf"]

def Test(izraz):
    exec("c="+izraz)
    print str(izraz)
    print str(simplify(c))+ "  _______ poenostavljeno"
    print str(cnf(c))+ "  ________cnf"
    
    for i in range(len(seznam)):
        exec("b="+izraz+"."+seznam[i]+"()")
        print seznam[i]+": "+str(b)
    

#izraz = "Tru()"
#izraz = "Fls()"
#izraz = "Not(Var('m'))"

#izraz = "And([(Var('n')),Var('m')])"
#izraz = "And([Not(Var('n')),Var('m')])"
#izraz = "And([Not(Var('n')),Var('m'),Not(Tru())])"
#izraz = "And([Not(Not((Var('n')))),Var('m'),Not(Tru())])"
#izraz = "And([Not(Not((Var('n')))),Var('m'),Not(Tru()),Var('m')])"

#izraz = "Or([(Var('n')),Var('m')])"
#izraz = "Or([Not(Var('n')),Var('m')])"
#izraz = "Or([Not(Var('n')),Var('m'),Not(Tru())])"
#izraz = "Or([Not(Not((Var('n')))),Var('m'),Not(Tru())])"
#izraz = "Or([Not(Not((Var('n')))),Var('m'),Not(Tru()),Var('m')])"

#izraz = "And([Or([Not((Var('n'))),Var('m')]),Var('m')])"
#izraz = "And([Or([Not((Var('n'))),Var('m')]),Var('o')])"
#izraz = "Or([And([Not((Var('n'))),Var('m')]),Var('m')])"
#izraz = "Or([And([Not((Var('n'))),Var('m')]),Var('o')])"
izraz = "Or([And([Not((Var('n'))),Var('m')]),Var('o'),And([Not((Var('n'))),Var('m')]),Var('o')])"


Test(izraz)   
