import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/12-13/'

"""
Calcular la clasificacion final de la liga 12-13.
"""

def mapfn(k, v):
    """
    en notes.txt pone que el campo 6 es:
    FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
    campos 4 y 5:
    FTHG = Full Time Home Team Goals
    FTAG = Full Time Away Team Goals

    Aqui podeis verificar si el resultado esta bien:
    http://www.statto.com/football/stats/england/premier-league/2012-2013
    """
    for row in v:
       # completar
       pass

def reducefn(k, vs):
    # completar
    pass

def display(results):
    # ordernamos la clasificacion
    print sorted(results.items(), key=lambda team: team[1],
            reverse=True)

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

