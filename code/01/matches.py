import sys
sys.path.append('code/common')
from basemr import *

data_dir = 'data/premier'

# Now the real deal
def mapfn(k, v):
    for row in v:
        yield 'total number of games', 1

def reducefn(k, vs):
    return sum(vs)

def display(results):
    print results

if __name__ == "__main__":
  	mr = BaseMR(data_dir, mapfn, reducefn)
  	mr.start(display)

