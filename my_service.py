from FreeTAKServer.controllers.services import FTS
import threading

ex = threading.Event()
FTS.start(ex)  
