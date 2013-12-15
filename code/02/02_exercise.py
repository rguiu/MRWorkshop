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
    """
    rellenar el codigo que falta
    """
    for row in v:
        yield 'max price', (float(row[23]),' '.join([row[1],row[2],row[3],'H']))
        yield 'max price', (float(row[24]),' '.join([row[1],row[2],row[3],'D']))
        yield 'max price', (float(row[25]),' '.join([row[1],row[2],row[3],'A']))

def reducefn(k, vs):
    """
    rellenar el codigo que falta
    """    
    return max(vs,key=lambda x: x[0])

def display(results):
    print results
if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

