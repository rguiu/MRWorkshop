import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier'

"""
Calcular el total de partidos jugados por cada equipo y mostrar los que han jugado el maximo 
numero posible o lo que es lo mismo, encuentra los equipos que han estado estas 4 temporadas
permanentemente en la premier league.
"""

def mapfn(k, v):
    """
    rellenar el codigo que falta
    """
    for row in v:
        # rellenar el codigo
        pass

def reducefn(k, vs):
    return sum(vs)

def display(results):
    # obtiene el numero de partidos jugados maximo
    max_matches = max(results.items(),key=lambda t: t[1])[1]
    # podria poner max_matches == team[1], pero por si a 1 equipo le
    # falta jugar un partido de la jornada pongo  max_matches - team[1] < 1
    results_top = [team[0] for team in results.items() if max_matches - team[1] < 1]
    print results_top

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

