import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/13-14'

"""
Calcular la clasificacion final de la liga 12-13.
"""

def mapfn(k, v):
    """
    rellenar el codigo que falta
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

