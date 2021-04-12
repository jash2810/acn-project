from topology_script import MyTopo
from routing_dijkstra import DijkstraRouting

TOPOS = {'mytopo': MyTopo}
ROUTING = {'dij' : DijkstraRouting}

def buildTopo(topo):
    return TOPOS[topo]()

def getRouting(routing, topo):
    return ROUTING[routing](topo)
