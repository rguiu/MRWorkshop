import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/12-13/'

"""
Calcular la clasificacion final de la liga 12-13.
"""

def mapfn(k, v):
    """
    rellenar el codigo que falta
    en notes.txt pone que el campo 6 es:
    FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
    campos 4 y 5:
    FTHG = Full Time Home Team Goals
    FTAG = Full Time Away Team Goals

    Aqui podeis verificar si el resultado esta bien:
    http://www.statto.com/football/stats/england/premier-league/2012-2013
    """
    for row in v:
        if row[6]=='H':            
            yield row[2], (3, 1, 0, 0, int(row[4]), int(row[5]))
            yield row[3], (0, 0, 0, 1, int(row[5]), int(row[4]))
        elif row[6]=='D':
            yield row[2], (1, 0, 1, 0, int(row[4]), int(row[5]))
            yield row[3], (1, 0, 1, 0, int(row[5]), int(row[4]))
        elif row[6]=='A':
            yield row[3], (3, 1, 0, 0, int(row[5]), int(row[4]))
            yield row[2], (0, 0, 0, 1, int(row[4]), int(row[5]))

def reducefn(k, vs):
    """
    rellenar el codigo que falta
    """    
    return map(sum,zip(*vs))

def display(results):
    # ordernamos la clasificacion
    print sorted(results.items(), key=lambda team: team[1],
            reverse=True)

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

