import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier/'

# Now the real deal
def mapfn(k, v):
    """
    Los campos 2 y 3 son los nombres de los equipos
    Los campos 4 y 5 son los goles
    """
    for row in v:
        # completar
        pass

def reducefn(k, vs):
    # completar
    pass

def display(results):
    list_of_months = sorted(results.items())
    for month in list_of_months: 
        print "%20s: %s" % (month[0],month[1][0])

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

