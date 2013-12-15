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
        # la tupla tiene como primer campo la media de goles
        # en un solo partido. Casualmente es el total de goles 
        # de un solo partido. El segundo campo es el total
        # de partidos, 1 en este caso
        yield row[2], (int(row[4]), 1)
        yield row[3], (int(row[5]), 1)

def reducefn(k, vs):
    total_num_matches = sum(v[1] for v in vs)
    goals             = sum(v[0] * v[1] for v in vs)
    return (goals/float(total_num_matches), total_num_matches) 

def display(results):
    # los ordeno por la media y
    # lo presento un poco mas bonito.
    list_of_teams = sorted(results.items(), key=lambda team: team[1], reverse=True)
    for team in list_of_teams: 
        print "%20s: %s" % (team[0],team[1][0])

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

