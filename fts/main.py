from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.utils import platform
from FreeTAKServer.controllers.services import FTS
import threading
from os import environ

if platform == 'android':
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
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions(['android.permission.READ_EXTERNAL_STORAGE', 'android.permission.WRITE_EXTERNAL_STORAGE', 'android.permission.POST_NOTIFICATIONS'])
            context =  mActivity.getApplicationContext()
            service_name = str(context.getPackageName()) + '.ServiceMyfts'
            self.service = autoclass(service_name)
        #self.service = None
        return Builder.load_string(kv)

    def start_service(self):        
        #service_name = 'org.fts.ftsapp.Service' + name
        #context =  mActivity.getApplicationContext()
        #service_name = str(context.getPackageName()) + '.Service' + name
        #self.service = autoclass(service_name)
        #service = autoclass('org.fts.ftsapp.ServiceFts')
        #mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        #argument = environ.get('PYTHON_SERVICE_ARGUMENT', '')
        if platform == 'android':
            self.service.start(mActivity,'')   
            return self.service

    def control_fts(self):        
        if self.root.ids.switch.text == 'ON':
            label = self.root.ids.switch
            label.text = "OFF"
            #self.service.stop(self.mActivity)
            #mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            #self.start_service('Myfts').stop(mActivity)
            if platform == 'android':
                self.start_service().stop(mActivity)
        else:
            label = self.root.ids.switch
            label.text = "ON"
            ex = threading.Event()
            FTS.start(ex)            
            #self.service.start(self.mActivity, 'small_icon', 'title', 'content' , self.argument)
            #self.start_service('Myfts')
            if platform == 'android':
                self.start_service()
         
     
Main().run()
