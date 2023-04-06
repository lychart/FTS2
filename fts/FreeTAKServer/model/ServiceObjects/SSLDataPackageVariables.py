from FreeTAKServer.controllers.configuration.MainConfig import MainConfig

class SSLDataPackageVariables:
    def __init__(self):
        self.SSLDataPackageIP = MainConfig.DataPackageServiceDefaultIP
        self.SSLDataPackagePort = 15580
        self.SSLDataPackageStatus = ""
