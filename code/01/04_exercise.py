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
        home_price = float(row[23])
        draw_price = float(row[24])
        away_price = float(row[25])

        if (home_price < away_price) and (row[6]=='H'):
            yield 'total', home_price - 1.0
        elif(home_price > away_price and row[6]=='A'):
            yield 'total', away_price - 1.0
        else:
            yield 'total', -1.0

def reducefn(k, vs):
    """
    rellenar el codigo que falta
    """    
    return sum(vs)

def display(results):
    print results
if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

