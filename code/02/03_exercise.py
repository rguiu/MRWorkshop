import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/'

"""
Considerando las columnas con los precios de una casa de apuestas, victoria 
local (columna 23), empate(24) y victoria visitante(25). Encontrar la posible
apuesta que habria generado mas dinero.
"""

def mapfn(k, v):
    """
    en notes.txt pone que el campo 6 es:
    FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
    campos 23, 24 y 25:
    B365H = Bet365 home win odds
    B365D = Bet365 draw odds 
    B365A = Bet365 away win odds
    """
    for row in v:
        # completar
        pass

def reducefn(k, vs):
    # completar
    pass

def display(results):
    print results
if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

