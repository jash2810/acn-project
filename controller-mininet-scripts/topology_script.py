#!/usr/bin/python

'''
Fat tree topology for data center networking

 based on riplpox
'''

from mininet.topo import Topo


class Node(object):
    def __init__(self, pod = 0, sw = 0, host = 0, dpid = None, name = None):
        '''Create NodeID object from custom params.

        Either (pod, sw, host) or dpid must be passed in.

        @param pod pod ID
        @param sw switch ID
        @param host host ID
        @param dpid optional dpid
        @param name optional name
        '''
        if dpid:
            self.pod = (dpid & 0xff0000) >> 16
            self.sw = (dpid & 0xff00) >> 8
            self.host = (dpid & 0xff)
            self.dpid = dpid
        elif name:
            pod, sw, host = [int(s) for s in name.split('_')]
            self.pod = pod
            self.sw = sw
            self.host = host
            self.dpid = (pod << 16) + (sw << 8) + host
        else:
            self.pod = pod
            self.sw = sw
            self.host = host
            self.dpid = (pod << 16) + (sw << 8) + host

    def __str__(self):
        return "(%i, %i, %i)" % (self.pod, self.sw, self.host)

    def name_str(self):
        '''Return name string'''
        return "%i_%i_%i" % (self.pod, self.sw, self.host)

    def mac_str(self):
        '''Return MAC string'''
        return "00:00:00:%02x:%02x:%02x" % (self.pod, self.sw, self.host)

    def ip_str(self):
        '''Return IP string'''
        return "10.%i.%i.%i" % (self.pod, self.sw, self.host)

class MyTopo(Topo):
    LAYER_CORE = 0
    LAYER_AGG = 1
    LAYER_EDGE = 2
    LAYER_HOST = 3



    def def_nopts(self, layer, name = None):
        '''Return default dict for a FatTree topo.

        @param layer layer of node
        @param name name of node
        @return d dict with layer key/val pair, plus anything else (later)
        '''
        d = {'layer': layer}
        if name:
            id = self.id_gen(name = name)
            # For hosts only, set the IP
            if layer == self.LAYER_HOST:
                d.update({'ip': id.ip_str()})
                d.update({'mac': id.mac_str()})
            d.update({'dpid': "%016x" % id.dpid})
        # print d
        return d

    def __init__(self, speed = 1.0):
        super(MyTopo, self).__init__()

        self.id_gen = Node
        self.hostList = []
        self.switchList = []
        self.aggList = []
        self.coreList = []

        switch_ids = [
            self.id_gen(1, 0, 1).name_str(),
            self.id_gen(1, 0, 2).name_str(),
            self.id_gen(1, 0, 3).name_str(),
            self.id_gen(1, 0, 4).name_str(),
            self.id_gen(1, 0, 5).name_str(),
            self.id_gen(1, 0, 6).name_str()
        ]
        switch_options = [
            self.def_nopts(self.LAYER_EDGE, switch_ids[0]),
            self.def_nopts(self.LAYER_EDGE, switch_ids[1]),
            self.def_nopts(self.LAYER_EDGE, switch_ids[2]),
            self.def_nopts(self.LAYER_EDGE, switch_ids[3]),
            self.def_nopts(self.LAYER_EDGE, switch_ids[4]),
            self.def_nopts(self.LAYER_EDGE, switch_ids[5]),
        ]

        for i in range(6):
            print "adding switch ", switch_ids[i]
            self.switchList.append(switch_ids[i])
            self.addSwitch(switch_ids[i], **switch_options[i])

        host_ids = [
            self.id_gen(0, 0, 1).name_str(),
            self.id_gen(0, 0, 2).name_str(),
            self.id_gen(0, 0, 3).name_str(),
            self.id_gen(0, 0, 4).name_str(),
            self.id_gen(0, 0, 5).name_str(),
            self.id_gen(0, 0, 6).name_str(),
            self.id_gen(0, 0, 7).name_str(),
            self.id_gen(0, 0, 8).name_str(),
            self.id_gen(0, 0, 9).name_str(),
            self.id_gen(0, 0, 10).name_str(),
            self.id_gen(0, 0, 11).name_str()
        ]
        host_options = [
            self.def_nopts(self.LAYER_HOST, host_ids[0]),
            self.def_nopts(self.LAYER_HOST, host_ids[1]),
            self.def_nopts(self.LAYER_HOST, host_ids[2]),
            self.def_nopts(self.LAYER_HOST, host_ids[3]),
            self.def_nopts(self.LAYER_HOST, host_ids[4]),
            self.def_nopts(self.LAYER_HOST, host_ids[5]),
            self.def_nopts(self.LAYER_HOST, host_ids[6]),
            self.def_nopts(self.LAYER_HOST, host_ids[7]),
            self.def_nopts(self.LAYER_HOST, host_ids[8]),
            self.def_nopts(self.LAYER_HOST, host_ids[9]),
            self.def_nopts(self.LAYER_HOST, host_ids[10])
        ]

        for i in range(11):
            print "Adding Host: ", host_ids[i], " options: ", host_options[i]
            self.hostList.append(host_ids[i])
            self.addHost(host_ids[i], **host_options[i])

        # THIS IS THE DEMO LINKS (BELOW 2 LINKS)
        # self.addLink(host_ids[0], switch_ids[0], 1, 1)
        # self.addLink(host_ids[1], switch_ids[0], 1, 2)
        # self.addLink(node1, node2, port of node1, port of node 2)  ---- node can be= host/switch


        # write the link code here - careful with the port numbers
        # go here.. self.addLink... .... ...
        self.addLink(host_ids[0], switch_ids[0], 1, 1) # h1, s1
        self.addLink(host_ids[1], switch_ids[0], 1, 2) # h2, s1
        self.addLink(switch_ids[0], switch_ids[1], 3, 3) #s1, s2
        self.addLink(switch_ids[0], switch_ids[2], 4, 3) #s1, s3

        self.addLink(host_ids[2], switch_ids[1], 1, 1) # h3, s2
        self.addLink(host_ids[3], switch_ids[1], 1, 2) # h4, s2
        self.addLink(switch_ids[1], switch_ids[2], 4, 4) # s2, s3
        self.addLink(switch_ids[1], switch_ids[3], 6, 3) # s2, s4
        self.addLink(switch_ids[1], switch_ids[4], 5, 3) # s2, s5

        self.addLink(host_ids[4], switch_ids[2], 1, 1) # h5, s3
        self.addLink(host_ids[5], switch_ids[2], 1, 2) # h6, s3
        # self.addLink(switch_ids[2], switch_ids[1], 4,4) -----
        self.addLink(switch_ids[2], switch_ids[4], 6,2) # s3, s5
        self.addLink(switch_ids[2], switch_ids[5], 5,4) # s3, s6

        self.addLink(host_ids[6], switch_ids[3], 1, 1) # h7, s4
        self.addLink(host_ids[7], switch_ids[3], 1, 2) # h8, s4
        # self.addLink(switch_ids[3], switch_ids[1], 3,6) -----
        self.addLink(switch_ids[3], switch_ids[4], 4,4) # s4, s5
        self.addLink(switch_ids[3], switch_ids[5], 5,5) # s4, s6

        self.addLink(host_ids[8], switch_ids[4], 1, 1) # h9, s5
        # self.addLink(host_ids[4], switch_ids[1], 2, 6) -----
        self.addLink(switch_ids[4], switch_ids[5], 5, 3) # s5, s6
        # self.addLink(host_ids[4], switch_ids[3], 4, 4)
        # self.addLink(host_ids[4], switch_ids[5], 5, 3)

        self.addLink(host_ids[9], switch_ids[5], 1, 1) # h10, s6
        self.addLink(host_ids[10], switch_ids[5], 1, 2) # h11, s6


    def layer_nodes(self, layer):
    #return list of node names in specified layer
        if(layer == self.LAYER_CORE):
            return self.coreList
        if(layer == self.LAYER_AGG):
            return self.aggList
        if(layer == self.LAYER_EDGE):
            return self.switchList
        if(layer == self.LAYER_HOST):
            return self.hostList



topos = {"mytopo" : ( lambda: MyTopo() )}
