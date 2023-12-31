from scapy.all import ARP, Ether, srp
from socket import getfqdn
import time,subprocess as sp

class Divice_MAC_Find():

    def __init__(self):
        pass

    def device_mac_finder(self,target_ip="192.168.1.0/24"):
        # create ARP packet
        arp = ARP(pdst=target_ip)
        # create the Ether broadcast packet
        # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # stack them
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        # a list of clients, we will fill this in the upcoming loop
        clients = []

        for sent, received in result:
            # for each response, append ip and mac address to `clients` list
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        return clients



if __name__=='__main__':
    # IP Address for the destination
    target_ip = "192.168.1.0/24"
    DMC = Divice_MAC_Find()
    clients = DMC.device_mac_finder(target_ip)
    # print clients
    print("Available devices in the network:")
    print("IP" + " " * 18 + "MAC" + " " * 18 + "NAME")
    for client in clients:
        print("{:16}    {}    {}".format(client['ip'], client['mac'], getfqdn(client['ip'])))
