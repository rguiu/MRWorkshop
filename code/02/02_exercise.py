import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/'

"""
Extender la solucion anterior y listar en que fecha y entre que equipos
y por que resultado fue. Hint: Aunque no sea lo mas optimo, podriamos 
emitir en el mapper los tres posibles resultados como una tupla del valor,
y una cadena de texto con la descripcion del partido (fecha y quienes
jugaban y porque resultado se pagaba ese precio).
"""

def mapfn(k, v):
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

