import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/'

"""
Encontrar el mejor precio que podria haber sido pagado por un partido 
victoria local (columna 23), empate(24) y victoria visitante(25). 
Es irrelevante en este caso si se pago o no.
"""

def mapfn(k, v):
    """
    rellenar el codigo que falta
    en notes.txt pone que el campo 9 es:
    campos 23, 24 y 25:
    B365H = Bet365 home win odds
    B365D = Bet365 draw odds 
    B365A = Bet365 away win odds
    """
    for row in v:
        yield 'best price', max([float(row[23]),float(row[24]),float(row[25])]) 

def reducefn(k, vs):
    """
    rellenar el codigo que falta
    """    
    return max(vs)

def display(results):
    print results
if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

