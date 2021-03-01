#leesgedichten.py
import os
import string
from rijmwoord import hulprijmwoordenboek as wb
import itertools

filenames = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f[:9] == 'gedicht_p']

alle_rijmen = {}


for f in filenames:
    with open(f,'r') as gedicht:
        text = gedicht.readlines()
        clean_text = []
        for t in text:
            if  '--' in t: break
            else: 
                try: clean_text.append(t.strip().strip(string.punctuation).split()[-1])
                except: pass
        rijmlijst = {}
        for c in clean_text:
            if c in wb:
                if  wb[c] in rijmlijst:
                    rijmlijst[wb[c]].append(c)
                else: rijmlijst[wb[c]] = [c]
        for r in rijmlijst: 
            if len(rijmlijst[r]) > 1:
                combinatie_lijst = ([list(f) for f in (itertools.combinations(rijmlijst[r], 2))])

                for c in combinatie_lijst: 
                    hash_list = tuple(sorted(c))
                    if hash_list[0] != hash_list[1]:
                        if hash_list in alle_rijmen:
                            alle_rijmen[hash_list] += 1
                        else: alle_rijmen[hash_list] = 1
                
geordende_rijmen = {k: v for k, v in sorted(alle_rijmen.items(), key=lambda item: item[1])}

with open('geordende_rijmen_p.txt', 'wt') as of:
    for gr in geordende_rijmen:
        of.write(f'{gr[0]}-{gr[1]}: {geordende_rijmen[gr]}\n')
        #of.write(f'{geordende_rijmen[gr]}, ')
