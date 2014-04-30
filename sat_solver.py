# -*- coding: cp1250 -*-
from bool import *
#===============================================================================

#SAT solver

#===============================================================================

def SAT(cnf,spr,cs,pureLiteral="True"):
    #SAT(cnf, spr, cs) je funkcija, ki resi SAT za podan slovar spremenljivk z ze dolocenimi vrednostmi in seznam spremenljivk, ki se nimajo dolocenih vrednosti.
    #spr=spremenljivke, cs=seznam spremenljivk, ki nimajo se vrednosti
    found = True
    #Najprej resimo izraze v cnf z eno spremenljivko z doloceno vrednostjo ali z nic spremenljivkami.
    while found:
        cnf = vstavi(cnf,spr,cs)
        pure = {}
        found =False
        for formula in cnf:
            if len(formula)==0:
                return False
            if len(formula)==1:
                found = True
                if formula[0][0]=='-':
                    spr[formula[0][1:]]=False
                    if formula[0][1:] in cs:
                        cs.remove(formula[0][1:])
                else:
                    spr[formula[0]]=True
                    if formula[0] in cs:
                        cs.remove(formula[0])
            if pureLiteral:
                for literal in formula:
                    if literal[0]=='-':
                        if literal[1:] in pure:
                            if pure[literal[1:]]=="Positive":
                                pure[literal[1:]] = "Conflicted"
                        else:
                            pure[literal[1:]]="Negative"
                    else:
                        if literal in pure:
                            if pure[literal]=="Negative":
                                pure[literal] = "Conflicted"
                        else:
                            pure[literal]="Positive"
        if pureLiteral:
            positive = [k for (k,v) in pure.items() if v =="Positive"]
            negative = [k for (k,v) in pure.items() if v =="Negative"]
            if len(positive)>0:
                found=True
                for literal in positive:
                    if not literal in spr:
                        print "Found one"
                    spr[literal]=True
                    if literal in cs:
                        cs.remove(literal)
            if len(negative)>0:
                found=True
                for literal in negative:
                    if not literal in spr:
                        print "Found one"
                    spr[literal]=False
                    if literal in cs:
                        cs.remove(literal)
                
    
    #Dolocimo vrednost spremenljivk, ki se nimajo dolocenih vrednosti. 
    if len(cnf)==0:
        return spr
    else:
        neReseno = cs[0]
        cs = cs[1:]
        sprCopy = spr.copy()
        sprCopy[neReseno] = True
        resitev = SAT(cnf, sprCopy, list(cs),pureLiteral=pureLiteral)
        if resitev:
           return resitev
        else:
            sprCopy = spr.copy()
            sprCopy[neReseno] = False
            resitev = SAT(cnf, sprCopy, list(cs),pureLiteral=pureLiteral)
            if resitev:
                return resitev
            else:
                return False
        
        

def vstavi(cnf, spr, cd):
    #VSTAVI(cnf,spr,cd) je funkcija, ki vrne poenostavljen cnf.
    #spr=slover spremenljivk, cs=seznam spremenljivk, ki nimajo se vrednosti
    sez=[]
    for formula in cnf:
        podsez=[]
        isTrue = False
                                    #Odstranimo notranje elemente, ki so False in vrne prazen seznam, ko najde element True.
        for f in formula:
            found = False
            if f in spr.keys():             #spremenlivka je ze v slovarju spr
                if spr[f]:              
                    found =  True
                    isTrue = True
                else:
                    found= True
            if f[1:] in spr.keys():         #spremenljivka brez negacije je ze v slovarju spr
                if spr[f[1:]]:
                    found =  True
                else:
                    isTrue = True
                    found= True
            if not found:                   #podsez je seznam vseh spremenljivk, ki se nimajo dolocene vrednosti
                podsez.append(f)
        if not isTrue:                  
            sez.append(podsez)
    return sez
    
def resi(izraz,simplify = True):
    #RESI(izraz) je funkcija, ki resi SAT s pomocjo funkcije SAT(cnf,spr,cs), in vrne seznam vrednosti spremenljivk, za katere je izraz resnicen.
    if simplify:
        izraz = cnf(izraz)
    else:
        izraz = cnfUnsimplified(izraz)
    cnf1 = [f.formula for f in izraz.formula]
    cs = []
    cnF = []
    #Sestavimo seznam vseh spremenljivk, ki v izrazu nastopajo.
    for f in cnf1:
        s=[]
        for ff in f:
            if isinstance(ff,Var):
                s.append(ff.ime)
                if ff.ime not in cs:
                    cs.append(ff.ime)
            elif isinstance(ff,Not):
                if isinstance(ff.formula,Var):
                    s.append('-'+ff.formula.ime)
                    if ff.formula.ime not in cs:
                        cs.append(ff.formula.ime)
        cnF.append(s)
    return SAT(cnF, {}, cs)
            
                
            
    
        
        
