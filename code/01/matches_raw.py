import mincemeat
import os
import fnmatch
import operator
import csv

# the following lines are for loading the input files.
league_files = []
for root, dirnames, filenames in os.walk('data/premier/'):
  for filename in fnmatch.filter(filenames, '*.csv'):
      league_files.append(os.path.join(root, filename))

def file_contents(file_name):
    re = csv.reader(open(file_name, 'rb'), delimiter=',')
    next(re) #eliminate header
    return [line for line in re]

source = dict((file_name, file_contents(file_name))
    for file_name in league_files)

# Now the real deal
def mapfn(k, v):
    for row in v:
        yield 'total number of games', 1

def reducefn(k, vs):
    return sum(vs)


# start the server
s = mincemeat.Server()
s.datasource = source
s.mapfn    = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

# Now display the results the results
print results
