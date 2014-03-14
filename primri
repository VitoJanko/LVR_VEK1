[str(i) for i in range(n)]

And([Not(Var('p')), Var('p')])          #-p A q
And([Not(Var('p')), Var('p'),Var('q')]) #-p A p A q
And([Var('p'),Var('q')])                #p A q
And([Var('r'), Var('p'),Var('q')])      #r A p A q
And([Or([Var('p'),Var('q')]),Or([Var('p'),Var('q'))]) #(p V q) A (p V q)
And([Var("p"), And([Var("q"), Var("p")]), Or([Var("r"), Var("q")])]) #p A (q A p) A (r V q) --> izpolnljiva za p=T,q=T
And([Not(Var("p")),Or([And([Var("p"),Var("q"),Var("r")]), Not(Var("q"))])]) #-p A ((p A q A r) V -q) --> poenostavljeno=(-p A -q), izpolnljiva za p=F,q=F   
And([Not(Var("p")),Or([And([Var("q"),Var("r"),Var("s")]), Not(Var("r"))]), Var("p")]) #-p A ((q A r A s) V -q) A p --> neizpolnljiva

Or([Not(Var('p')), Var('p')])           #-p V q
Or([Not(Var('p')), Var('p'),Var('q')])  #-p V p V q
Or([Var('p'),Var('q')])                 #p V q
Or([Var('r'), Var('p'),Var('q')])       #r V p V q
Or([Var("p"), And([Var("q"), Var("p")]), And([Var("r"), Var("q")])])    #p V (q A p) V (r A q)
Or([Not(Var("p")),And([Or([Var("p"),Var("q"),Var("r")]), Not(Var("q"))])]) #-p V ((p V q V r) A -q) -->poenostavljeno=(-p V -q)
    



