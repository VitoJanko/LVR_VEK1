LVR_VEK1
========

V tem projektu smo implemetirali orodja za delanje z logi�nimi izrazi (predvsem njihovo izpisovanje, poenostavljanje in 
pretvarjanje med raznimi oblikami). Narejen je tudi algoritem za re�evanje SAT problema. Za demonstracijo le tega 
smo probleme sudoku-ja, latinskega kvadrata in hadamardove matrike prevedli na SAT probleme in jih nato re�ili. 

V projektu so naslednje datoteke: 

-- bool.py
Skripta za delo z logi�nimi izrazi. Sledijo primeri uporabe.

* a = Tru()  			**Vrednost True, na volje je tudi Fls() za vrednost False **

* b = Var("n")	    **nova spremenljivka z imenom "n"** 

* c = Neg(Var("n")) 	**negacija spremenljivke z imenom "n"**

* d = And([b,c,Tru(),Fls()])  **Veznik Ali izvedemo z seznamom elementov v konjunkciji enako za disjunkcijo**

####Naslednje metode so na voljo za spremembo iz ene oblike v drugo
* d.nnf()  			**spremeni v "negation normal form"**

* cnf(d)				**spremeni v "conjuctive normal form"**

* simplify(d)			**poenostavi izraz**

- tester.py
Demonstrira zgoraj navedene spremembe oblik na razli�nih primerih. Deluje kot tester za te osnovne opracije.
Primere tudi re�i z SAT algoritmom. 

- primeri.txt
Vsebuje primere, ki jih tester.py re�uje. 

- sat_solver.py
Algoritem za re�evanje SAT problema. Gre za DPLL algoritem (http://en.wikipedia.org/wiki/DPLL_algorithm), ki ima implementirano 
tako eliminacijo samostojnih literalov, kot eliminacijo �istih literalov. Za vhod sprejme poljuben logi�en izraz, vrne pa slovar
spremenljivkin njihovih vrednosti. V primeru da je vrednost neke spremenljivke nepomembna za pravilnost izraza, jo v slovarju ni. 
V primeru, da re�itev ne obstaja, algoritem vrne False. 
Dodatno im algoritem mo�nost zastavice "simplify = False", ki izraz re�uje direktno, brez prej�nje poenastavitve. To je koristno, 
kadar je kraj�anje izraza zamudno in brez �elenega u�inka. Primer tega se pojavi pri re�evanju sudoku-ja. 
Primer uporabe:  resi(Neg(Var("n")) ) oziroma resi(Neg(Var("n")), simplify = False)

- sudoku.py
Naredi (spremeni problem v SAT problem) in vizualizira sudoku ter latinski kvadrat (poljubne dimenzije).

- HadamardMatrix.py
Naredi in vizualizira Hadamardovo matriko. 

- resevanjeNalog.py
V tej datoteki so primeri uporabe SAT algoritma na sudoku, latinskem kvadratu ter Hadamardovi matriki. 
V njej je pokazana in komentirana uporaba vseh relevantnih funkcij v zgornjih treh datotekah. 
Nove teste se lahko enostavno dodaja in po�ene na tem mestu. 
