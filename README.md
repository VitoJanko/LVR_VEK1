LVR_VEK1
========

V tem projektu smo implemetirali orodja za delanje z logiènimi izrazi (predvsem njihovo izpisovanje, poenostavljanje in 
pretvarjanje med raznimi oblikami). Narejen je tudi algoritem za reševanje SAT problema. Za demonstracijo le tega 
smo probleme sudoku-ja, latinskega kvadrata in hadamardove matrike prevedli na SAT probleme in jih nato rešili. 

V projektu so naslednje datoteke: 

- bool.py
Skripta za delo z logiènimi izrazi. Sledijo primeri uporabe.
a = Tru()  			**Vrednost True, na volje je tudi Fls() za vrednost False **

b = Var("n")	    **nova spremenljivka z imenom "n"**

c = Neg(Var("n")) 	**negacija spremenljivke z imenom "n"**

d = And([b,c,Tru(),Fls()])  **Veznik Ali izvedemo z seznamom elementov v konjunkciji enako za disjunkcijo**

#####Naslednje metode so na voljo za spremembo iz ene oblike v drugo
d.nnf()  			**spremeni v "negation normal form"**

cnf(d)				**spremeni v "conjuctive normal form"**

simplify(d)			**poenostavi izraz**

- tester.py
Demonstrira zgoraj navedene spremembe oblik na razliènih primerih. Deluje kot tester za te osnovne opracije.
Primere tudi reši z SAT algoritmom. 

- primeri.txt
Vsebuje primere, ki jih tester.py rešuje. 

- sat_solver.py
Algoritem za reševanje SAT problema. Gre za DPLL algoritem (http://en.wikipedia.org/wiki/DPLL_algorithm), ki ima implementirano 
tako eliminacijo samostojnih literalov, kot eliminacijo èistih literalov. Za vhod sprejme poljuben logièen izraz, vrne pa slovar
spremenljivkin njihovih vrednosti. V primeru da je vrednost neke spremenljivke nepomembna za pravilnost izraza, jo v slovarju ni. 
V primeru, da rešitev ne obstaja, algoritem vrne False. 
Dodatno im algoritem možnost zastavice "simplify = False", ki izraz rešuje direktno, brez prejšnje poenastavitve. To je koristno, 
kadar je krajšanje izraza zamudno in brez želenega uèinka. Primer tega se pojavi pri reševanju sudoku-ja. 
Primer uporabe:  resi(Neg(Var("n")) ) oziroma resi(Neg(Var("n")), simplify = False)

- sudoku.py
Naredi (spremeni problem v SAT problem) in vizualizira sudoku ter latinski kvadrat (poljubne dimenzije).

- HadamardMatrix.py
Naredi in vizualizira Hadamardovo matriko. 

- resevanjeNalog.py
V tej datoteki so primeri uporabe SAT algoritma na sudoku, latinskem kvadratu ter Hadamardovi matriki. 
V njej je pokazana in komentirana uporaba vseh relevantnih funkcij v zgornjih treh datotekah. 
Nove teste se lahko enostavno dodaja in požene na tem mestu. 