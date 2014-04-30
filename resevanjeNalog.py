from sudoku import *
from sat_solver import *
from hadamardMatrix import *

print "LATINSKI KVADRAT 3*3\n"
l3 = makeLatinSquare(3)
solution = resi(l3)
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacija spremenljivk\n"
visualiseSquare(solution,3)

print "LATINSKI KVADRAT 4*4\n"
l4 = makeLatinSquare(4)
solution = resi(l4)
print "Vrenosti spremenljivk\n"
print solution
print "\nInterpretacija spremenljivk\n"
visualiseSquare(solution,4)


print "HADAMARDOVA MATRIKA 2*2\n"
r = resi(makeHadamardovaMatrika(2))
visualiseHadamard(r,2)

print "HADAMARDOVA MATRIKA 4*4"
print "Resevanje lahko traja nekaj minut\n"
r = resi(makeHadamardovaMatrika(4))
visualiseHadamard(r,4)
