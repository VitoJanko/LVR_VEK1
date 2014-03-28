# -*- coding: cp1250 -*-
from bool import *
#===============================================================================

#SAT solver

#===============================================================================

def SAT(cnf,spr,cs):
    #SAT(cnf, spr, cs) je funkcija, ki re�i SAT za podan slovar spremenljivk z �e dolo�enimi vrednostmi in seznam spremenljivk, ki �e nimajo dolo�enih vrednosti.
    #spr=spremenljivke, cs=seznam spremenljivk, ki nimajo se vrednosti
    found = True
                                #Najprej re�imo izraze v cnf z eno spremenljivko z dolo�eno vrednostjo ali z ni� spremenljivkami.
    while found: 
        cnf = vstavi(cnf,spr,cs)
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
                        
                                #Dolo�imo vrednost spremenljivk, ki �e nimajo dolo�enih vrednosti. 
    if len(cnf)==0:
        return spr
    else:
        neReseno = cs[0]
        cs = cs[1:]
        spr[neReseno] = True
        resitev = SAT(cnf, spr, cs)
        if resitev:
           return resitev
        else:
            spr[neReseno] = False
            resitev = SAT(cnf, spr, cs)
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
            if f in spr.keys():             #spremenlivka je �e v slovarju spr
                if spr[f]:              
                    found =  True
                    isTrue = True
                else:
                    found= True
            if f[1:] in spr.keys():         #spremenljivka brez negacije je �e v slovarju spr
                if spr[f[1:]]:
                    found =  True
                else:
                    isTrue = True
                    found= True
            if not found:                   #podsez je seznam vseh spremenljivk, ki �e nimajo dolo�ene vrednosti
                podsez.append(f)
        if not isTrue:                  
            sez.append(podsez)
    return sez
    
def resi(izraz):
    #RESI(izraz) je funkcija, ki re�i SAT s pomo�jo funkcije SAT(cnf,spr,cs), in vrne seznam vrednosti spremenljivk, za katere je izraz resni�en.
    izraz = cnf(izraz)
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
            
                
            
    
        
        
