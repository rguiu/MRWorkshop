#!/usr/bin/env python
import mincemeat
import os
import fnmatch
import operator
import csv

class BaseMR:

    def __init__(self, data_dir, mapfn, reducefn):
        league_files = []
        
        for root, dirnames, filenames in os.walk(data_dir):
            for filename in fnmatch.filter(filenames, '*.csv'):
                league_files.append(os.path.join(root, filename))

        def file_contents(file_name):
            re = csv.reader(open(file_name, 'rb'), delimiter=',')
            next(re) #eliminate header
            return [line for line in re]

        self.source = dict((file_name, file_contents(file_name))
            for file_name in league_files)

        self.mapfn = mapfn
        self.reducefn = reducefn


    def start(self, display):
        # start the server
        s = mincemeat.Server()
        s.datasource = self.source
        s.mapfn = self.mapfn
        s.reducefn = self.reducefn

        results = s.run_server(password="changeme")
        display(results)


