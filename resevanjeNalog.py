from sudoku import *
from sat_solver import *


print "LATINSKI KVADRAT 3*3\n"
l3 = makeLatinSquare(3)
solution = resi(l3)
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacije spremenljivk\n"
visualiseSquare(solution,3)

print "LATINSKI KVADRAT 4*4\n"
l4 = makeLatinSquare(4)
solution = resi(l4)
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacije spremenljivk\n"
visualiseSquare(solution,4)
