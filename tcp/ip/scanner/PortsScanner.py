class PortScanner :
    def __init__(self,operations,adressRange):
        self.operations = operations
        self.operations.scan(adressRange)
    def getOpnedPorts(self):
        return self.operations.getOpnedPorts()
