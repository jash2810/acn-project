import sys
sys.path.append(".")

from mininet.topo import Topo
from mininet.node import Controller, RemoteController, OVSKernelSwitch, CPULimitedHost
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import custom
from mininet.log import setLogLevel, info, warn, error, debug

from topology_script import MyTopo
from routing_dijkstra import Routing

from subprocess import Popen, PIPE
from argparse import ArgumentParser
import multiprocessing
from time import sleep
import os

# Queue Size
QUEUE_SIZE = 100

# Link capacity (Mbps)
BW = 10

parser = ArgumentParser(description="minient_fattree")

parser.add_argument('-d', '--dir', dest='output_dir', default='log',
        help='Output directory')

parser.add_argument('-i', '--input', dest='input_file',
        default='inputs/all_to_all_data',
        help='Traffic generator input file')

parser.add_argument('-t', '--time', dest='time', type=int, default=30,
        help='Duration (sec) to run the experiment')

parser.add_argument('-p', '--cpu', dest='cpu', type=float, default=-1,
        help='cpu fraction to allocate to each host')

parser.add_argument('--iperf', dest='iperf', default=False, action='store_true',
        help='Use iperf to generate traffics')

parser.add_argument('--ecmp',dest='ECMP',default=False,
        action='store_true',help='Run the experiment with ECMP routing')

parser.add_argument('--tlr',dest='tlr', default=False,
        action='store_true', help='Run the experiment with Fat-Tree two-level routing')

parser.add_argument('--dijkstra',dest='dij',default=False,
        action='store_true',help='Run the experiment with dijkstra routing')

args = parser.parse_args()



def NetCreator(args, bw=10, cpu=-1, queue=100, controller='Controller'):
    
    info('*** Creating the topology')
    topo = MyTopo()
    host = custom(CPULimitedHost, cpu=cpu)
    link = custom(TCLink, bw=bw, max_queue_size=queue)

    net = Mininet(topo, host=host, link=link, switch=OVSKernelSwitch,
            controller=RemoteController, autoStaticArp=True)

    return net

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i


def iperfTrafficGen(args, hosts, net):
    '''
    Traffic Generator
    '''
    num_lines = file_len(args.input_file)
    print "Total Pings: ", num_lines
    f = open(args.input_file, 'r')

    t = args.time/(num_lines-1)
    info("Starting Experiment\n")
    for line in f:
        l = line.split(" ")

        if len(l) < 2:
            continue

        src = l[0]
        dest = l[1]
        s = src.split('.')
        d = dest.split('.')


        if len(s) is not 4:
            continue

        h1 = s[1] + '_' + s[2] + '_' + s[3]
        h2 = d[1] + '_' + d[2] + '_' + d[3]

        src_host, dest_host = net.get(h1, h2)
        d_out = dest_host.cmd("iperf -s -p 12345 -t " + str(t) + " &")
        s_out = src_host.cmd("iperf -c "+ dest +" -p 12345 -t " + str(t))
        dest_host.cmd("pkill iperf")
        src_host.cmd("pkill iperf")
        print s_out
        print "\n"
        # output.write(s_out+'\n')
        print h1, h2
    info("Finished\n")
    f.close()


def ExecuteNet(args,controller):
    net = NetCreator(args, cpu=args.cpu, bw=BW, queue=QUEUE_SIZE,
            controller=controller)
    net.start()

    # wait for the switches to connect to the controller
    info('** Waiting for switches to connect to the controller...\n')
    sleep(4)

    hosts = net.hosts
    print "NET"
    iperfTrafficGen(args, hosts, net)
    CLI(net)
    net.stop()

def clean():
    ''' Clean any the running instances of POX '''

    p = Popen("ps aux | grep 'pox' | awk '{print $2}'",
            stdout=PIPE, shell=True)
    p.wait()
    procs = (p.communicate()[0]).split('\n')
    for pid in procs:
        try:
            pid = int(pid)
            Popen('kill %d' % pid, shell=True).wait()
        except:
            pass

if __name__ == '__main__':

    setLogLevel( 'info' )
    if not os.path.exists(args.output_dir):
        print args.output_dir
        os.makedirs(args.output_dir)

    #clean()
    if args.dij:
        ExecuteNet(args,controller='Controller')
    else:
        info('**error** please specify either ecmp, dijkstra or tlr\n')

    Popen("killall -9 top bwm-ng", shell=True).wait()
    #os.system('sudo mn -c')
