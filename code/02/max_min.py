import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/12-13'

# Now the real deal
def mapfn(k, v):
    """
    Los campos 2 y 3 son los nombres de los equipos
    Los campos 4 y 5 son los goles
    """
    for row in v:
        yield row[2], (int(row[4]), int(row[5]))
        yield row[3], (int(row[5]), int(row[4]))

def reducefn(k, vs):
    return map(max,zip(*vs))

def display(results):
    print results

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

