import logging
from copy import copy
from Dijkstras import dijkstraHelperFunction

class Routing(object):

    def __init__(self, topo):
        self.topo = topo


    def get_route(self, src, dst):
        raise NotImplementedError

class DijkstraRouting(Routing):
    ''' Dijkstra routing algorithm caller'''

    def __init__(self, topo):
        self.topo = topo
        self.count = 0

    def get_route(self, src, dst):
        print "SRC: ", src, " DST: ", dst, "\n" 
        return dijkstraHelperFunction(self.topo,src,dst)
