import nmap;
class NmapOperations:
    def __init__(self):
        self.ns = nmap.PortScanner();
    def scan(self,adressRange):
        return self.ns.scan('127.0.0.1')



nm=NmapOperations()
print(nm.scan(''))