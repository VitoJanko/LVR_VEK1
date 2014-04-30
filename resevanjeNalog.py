from sudoku import *
from sat_solver import *
from hadamardMatrix import *

#================================================================================

#PROGRAM Z PRIMERI na katerih uporabilo SAT solver

#================================================================================

#Primer uporabe latinskega kvadrata

print "LATINSKI KVADRAT 3*3\n"
l3 = makeLatinSquare(3)                    #nastavi problem
solution = resi(l3)                        #resi problem
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacija spremenljivk\n"
visualiseSquare(solution,3)                #narise reistev

print "LATINSKI KVADRAT 4*4\n"
l4 = makeLatinSquare(4)
solution = resi(l4)
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacija spremenljivk\n"
visualiseSquare(solution,4)

#Primer uporabe sudokuja

print "SUDOKU LAHEK\n"
s1=[[2,0,3,0,5,0,4,9,6],                    #zacetna konfiguracija
    [7,6,0,2,0,4,0,3,0],
    [9,4,0,6,0,3,0,7,5],
    [0,3,6,0,0,1,0,0,7],
    [0,0,7,0,6,0,1,8,0],
    [1,5,0,4,0,7,0,6,0],
    [3,0,2,0,0,6,0,5,0],
    [0,8,4,5,7,0,9,1,3],
    [0,7,1,0,0,9,6,0,4]]
print "Naloga\n"
visualiseTemplate(s1)                       #narise problem
sudoku = makeSudoku(s1)                     #nastavi problem
solution = resi(sudoku,simplify = False)    #resi problem
#resevanje je hitrejse s to zastavico, ki problema ne simplificira,
#temvec direktno resuje
print "Resitev\n"
visualiseSudoku(solution)                   #narise reistev

print "SUDOKU ZELO TEZEK"
print "Resevanje lahko traja nekaj minut.\n"
s2=[[1,0,0,0,0,0,0,0,0],
   [0,7,0,0,0,0,3,0,0],
   [4,9,6,8,0,0,0,0,0],
   [6,5,9,7,0,0,0,0,4],
   [0,0,4,0,9,0,2,8,0],
   [0,0,0,5,4,0,0,0,0],
   [8,0,0,0,3,0,0,1,9],
   [0,0,0,0,0,4,0,0,7],
   [9,0,0,0,5,0,0,6,0]]
print "Naloga\n"
visualiseTemplate(s2)        
sudoku = makeSudoku(s2)
solution = resi(sudoku,simplify = False)
print "Resitev\n"
visualiseSudoku(solution)

#Primer uporabe Hadamardove matrike

print "HADAMARDOVA MATRIKA 2*2\n"
r = resi(makeHadamardovaMatrika(2))         #resi problem
visualiseHadamard(r,2)                      #narise reistev

print "HADAMARDOVA MATRIKA 4*4"
print "Resevanje lahko traja nekaj minut.\n"
r = resi(makeHadamardovaMatrika(4))
visualiseHadamard(r,4)
