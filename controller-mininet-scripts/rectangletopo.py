# there would be 4 switch
switch_ids = [self.id_gen(1, 0, 1).name_str(), self.id_gen(1, 0, 2).name_str(), self.id_gen(1, 0, 3).name_str(), self.id_gen(1, 0, 4).name_str()]
switch_options = [self.def_nopts(self.LAYER_EDGE, switch_ids[0]), self.def_nopts(self.LAYER_EDGE, switch_ids[1]), self.def_nopts(self.LAYER_EDGE, switch_ids[2]), self.def_nopts(self.LAYER_EDGE, switch_ids[3])]

for i in range(4):
    print "adding switch ", switch_ids[i], switch_options[i]
    self.switchList.append(switch_ids[i])
    self.addSwitch(switch_ids[i], **switch_options[i])

host_ids = [self.id_gen(0, 0, 1).name_str(), self.id_gen(0, 0, 2).name_str(), self.id_gen(0, 0, 3).name_str(), self.id_gen(0, 0, 4).name_str(), self.id_gen(0, 0, 5).name_str()]
host_options = [self.def_nopts(self.LAYER_HOST, host_ids[0]), self.def_nopts(self.LAYER_HOST, host_ids[1]), self.def_nopts(self.LAYER_HOST, host_ids[2]), self.def_nopts(self.LAYER_HOST, host_ids[3]), self.def_nopts(self.LAYER_HOST, host_ids[4])]

for i in range(5):
    print "Host: ", host_ids[i], " Options: ", host_options[i]
    self.hostList.append(host_ids[i])
    self.addHost(host_ids[i], **host_options[i])

# addLink ( s1, s3, 4, 1 )
# addLink (node1, node2, port of node1, port of node2)
self.addLink(host_ids[0], switch_ids[0], 1, 1)
self.addLink(host_ids[1], switch_ids[0], 1, 2)
self.addLink(switch_ids[0], switch_ids[1], 3, 1)
self.addLink(switch_ids[0], switch_ids[2], 4, 1)
self.addLink(switch_ids[1], switch_ids[3], 2, 3)
self.addLink(switch_ids[2], switch_ids[3], 2, 4)
self.addLink(host_ids[2], switch_ids[3], 1, 1)
self.addLink(host_ids[3], switch_ids[3], 1, 2)
self.addLink(host_ids[4], switch_ids[1], 1, 3)
