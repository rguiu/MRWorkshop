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
        date_as_list = row[1].split
        yield "%s%s" % (date_as_list[2], date_as_list[1]), (int(row[4])+int(row[5]), 1)

def reducefn(k, vs):
    total_num_matches = sum(v[1] for v in vs)
    goals             = sum(v[0] * v[1] for v in vs)
    return (goals/float(total_num_matches), total_num_matches) 

def display(results):
    list_of_months = sorted(results.items())
    for month in list_of_months: 
        print "%20s: %s" % (month[0],month[1][0])

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

