import os
from FreeTAKServer.controllers.services.FTS import FTS
from FreeTAKServer.controllers.configuration.OrchestratorConstants import OrchestratorConstants
from FreeTAKServer.model.ServiceObjects.FTS import FTS as FTSObj
from FreeTAKServer.controllers.configuration.MainConfig import MainConfig
from FreeTAKServer.controllers.configuration_wizard import ask_user_for_config
from FreeTAKServer.controllers.certificate_generation import AtakOfTheCerts
import argparse

try:
    parser = argparse.ArgumentParser(description=OrchestratorConstants().FULLDESC)
    parser.add_argument('-CoTPort', type=int, help=OrchestratorConstants().COTPORTDESC,
                        default=FTSObj().CoTService.CoTServicePort)
    parser.add_argument('-CoTIP', type=str, help=OrchestratorConstants().COTIPDESC,
                        default=FTSObj().CoTService.CoTServiceIP)
    parser.add_argument('-SSLCoTPort', type=int, help=OrchestratorConstants().SSLCOTPORTDESC,
                        default=FTSObj().SSLCoTService.SSLCoTServicePort)
    parser.add_argument('-SSLCoTIP', type=str, help=OrchestratorConstants().SSLCOTIPDESC,
                        default=FTSObj().SSLCoTService.SSLCoTServiceIP)
    parser.add_argument('-DataPackagePort', type=int, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().TCPDataPackageService.TCPDataPackageServicePort)
    parser.add_argument('-DataPackageIP', type=str, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().TCPDataPackageService.TCPDataPackageServiceIP)
    parser.add_argument('-SSLDataPackagePort', type=int, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().SSLDataPackageService.SSLDataPackageServicePort)
    parser.add_argument('-SSLDataPackageIP', type=str, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().SSLDataPackageService.SSLDataPackageServiceIP)
    parser.add_argument('-RestAPIPort', type=int, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().RestAPIService.RestAPIServicePort)
    parser.add_argument('-RestAPIIP', type=str, help=OrchestratorConstants().APIPORTDESC,
                        default=FTSObj().RestAPIService.RestAPIServiceIP)
    parser.add_argument('-d', type=bool)
    parser.add_argument('-AutoStart', type=str,
                        help='whether or not you want all services to start or only the root service and the RestAPI service',
                        default='True')
    parser.add_argument('-UI', type=str, help="set to true if you would like to start UI on server startup")
    args = parser.parse_args()
    
    #if MainConfig.first_start:
    yaml_path = MainConfig.yaml_path
    if not os.path.exists(yaml_path):
        ask_user_for_config()
    else:
        pass

    aotc = AtakOfTheCerts()
    aotc.generate_ca(expiry_time_secs=31536000)
    aotc.bake(common_name="server", cert="server", expiry_time_secs=31536000)
    aotc.bake(common_name="Client", cert="user", expiry_time_secs=31536000)
    #import os
    
    
    FTS().startup(args.CoTPort, args.CoTIP, args.DataPackagePort, args.DataPackageIP, args.SSLDataPackagePort,
                  args.SSLDataPackageIP, args.RestAPIPort, args.RestAPIIP, args.SSLCoTPort, args.SSLCoTIP,
                  args.AutoStart, True, args.UI)
except Exception as e:
    print(e)     
