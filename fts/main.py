import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.utils import platform
from FreeTAKServer.controllers.services.FTS import FTS
from FreeTAKServer.controllers.configuration.OrchestratorConstants import OrchestratorConstants
from FreeTAKServer.model.ServiceObjects.FTS import FTS as FTSObj
from FreeTAKServer.controllers.configuration.MainConfig import MainConfig
from FreeTAKServer.controllers.configuration_wizard import ask_user_for_config
from FreeTAKServer.controllers.certificate_generation import AtakOfTheCerts
import argparse
import threading
from os import environ

"""
if platform == 'android':
    from jnius import autoclass
    from android import mActivity
"""
from jnius import autoclass
from android import mActivity

kv = """
#:import Thread threading.Thread

Screen:
    #in_class: s1
    MDLabel:
        text: 'FTS App'
        font_style: 'H2'
        pos_hint: {'center_x': 0.6, 'center_y': 0.8}
 
        
    MDRectangleFlatButton:
        text: 'OFF'
        id: switch
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            Thread(target=app.control_fts).start()
            #app.auth()
           

"""
    
class Main(MDApp):
    in_class = ObjectProperty(None)
    
    def build(self):
        """
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions(['android.permission.READ_EXTERNAL_STORAGE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.POST_NOTIFICATIONS'])
            context =  mActivity.getApplicationContext()
            service_name = str(context.getPackageName()) + '.ServiceMyfts'
            self.service = autoclass(service_name)
        """
        from android.permissions import request_permissions, Permission
        request_permissions(['android.permission.READ_EXTERNAL_STORAGE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.POST_NOTIFICATIONS'])
        #context =  mActivity.getApplicationContext()
        #service_name = str(context.getPackageName()) + '.ServiceMyfts'
        #self.service = autoclass(service_name)
        return Builder.load_string(kv)

    def start_service(self):        
        #service_name = 'org.fts.ftsapp.Service' + name
        #context =  mActivity.getApplicationContext()
        #service_name = str(context.getPackageName()) + '.Service' + name
        #self.service = autoclass(service_name)
        #service = autoclass('org.fts.ftsapp.ServiceFts')
        #mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        #argument = environ.get('PYTHON_SERVICE_ARGUMENT', '')
        """
        if platform == 'android':
            self.service.start(mActivity,'')   
            return self.service
        """
        #self.service.start(mActivity,'')   
        #return self.service
        pass

    def control_fts(self):        
        if self.root.ids.switch.text == 'ON':
            label = self.root.ids.switch
            label.text = "OFF"
            #self.service.stop(self.mActivity)
            #mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            #self.start_service('Myfts').stop(mActivity)
            """
            if platform == 'android':
                self.start_service().stop(mActivity)
            """
            #self.start_service().stop(mActivity)
        else:
            label = self.root.ids.switch
            label.text = "ON"
            #ex = threading.Event()
            #FTS.start(ex)
            self.start_fts()            
            #self.service.start(self.mActivity, 'small_icon', 'title', 'content' , self.argument)
            #self.start_service('Myfts')
            """
            if platform == 'android':
                self.start_service()
            """
            #self.start_service()
    
    def start_fts(self):
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
            
            if MainConfig.first_start:
                ask_user_for_config()
            else:
                pass

            aotc = AtakOfTheCerts()
            aotc.generate_ca(expiry_time_secs=31536000)
            aotc.bake(common_name="server", cert="server", expiry_time_secs=31536000)
            aotc.bake(common_name="Client", cert="user", expiry_time_secs=31536000)
            import os
            
            
            FTS().startup(args.CoTPort, args.CoTIP, args.DataPackagePort, args.DataPackageIP, args.SSLDataPackagePort,
                          args.SSLDataPackageIP, args.RestAPIPort, args.RestAPIIP, args.SSLCoTPort, args.SSLCoTIP,
                          args.AutoStart, True, args.UI)
        except Exception as e:
            print(e)     
     
Main().run()
