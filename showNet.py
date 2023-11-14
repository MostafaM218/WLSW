from pywifi import *
class shownetworks():
    def __init__(self):
        self.col_pwf = PyWiFi()
        self.wln_adp = self.col_pwf.interfaces()[0]
    def show_av_network(self):
        self.wln_adp.scan()
        sh_wln = self.wln_adp.scan_results()
        return sh_wln

