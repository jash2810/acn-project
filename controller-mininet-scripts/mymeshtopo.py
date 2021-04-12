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

for i in range(5):
    print "Adding Host: ", host_ids[i], " options: ", host_options[i]
    self.hostList.append(host_ids[i])
    self.addHost(host_ids[i], **host_options[i])

# THIS IS THE DEMO LINKS (BELOW 2 LINKS)
# self.addLink(host_ids[0], switch_ids[0], 1, 1)
# self.addLink(host_ids[1], switch_ids[0], 1, 2)
# self.addLink(node1, node2, port of node1, port of node 2)  ---- node can be= host/switch


# write the link code here - careful with the port numbers
# go here.. self.addLink... .... ...
self.addLink(host_ids[0], switch_ids[0], 1, 1)
self.addLink(host_ids[1], switch_ids[0], 1, 2)
self.addLink(switch_ids[0], switch_ids[1], 3, 3)
self.addLink(switch_ids[0], switch_ids[2], 4, 3)

self.addLink(host_ids[2], switch_ids[1], 1, 1)
self.addLink(host_ids[3], switch_ids[1], 1, 2)
self.addLink(switch_ids[1], switch_ids[2], 4, 4)
self.addLink(switch_ids[1], switch_ids[3], 6, 3)
self.addLink(switch_ids[1], switch_ids[4], 5, 3)

self.addLink(host_ids[4], switch_ids[2], 1, 1)
self.addLink(host_ids[5], switch_ids[2], 1, 2)
# self.addLink(switch_ids[2], switch_ids[1], 4,4) -----
self.addLink(switch_ids[2], switch_ids[4], 6,2)
self.addLink(switch_ids[2], switch_ids[5], 5,4)

self.addLink(host_ids[6], switch_ids[3], 1, 1)
self.addLink(host_ids[7], switch_ids[3], 1, 2)
# self.addLink(switch_ids[3], switch_ids[1], 3,6) -----
self.addLink(switch_ids[3], switch_ids[4], 4,4)
self.addLink(switch_ids[3], switch_ids[5], 5,5)

self.addLink(host_ids[8], switch_ids[4], 1, 1)
# self.addLink(host_ids[4], switch_ids[1], 2, 6) -----
self.addLink(host_ids[4], switch_ids[3], 4, 4)
self.addLink(host_ids[4], switch_ids[3], 4, 4)
self.addLink(host_ids[4], switch_ids[5], 5, 3)

self.addLink(host_ids[9], switch_ids[5], 1, 1)
self.addLink(host_ids[10], switch_ids[5], 1, 2)
# self.addLink(switch_ids[5], switch_ids[2], 4,5) -----
self.addLink(switch_ids[5], switch_ids[3], 5,5)
self.addLink(switch_ids[5], switch_ids[4], 3,5)
