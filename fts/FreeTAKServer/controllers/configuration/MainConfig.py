import os
import sys
import re
import yaml
currentPath = os.path.dirname(os.path.abspath(__file__))
from pathlib import Path
from kivy.utils import platform

#print(str(platform))

if platform == 'android':
    from android.storage import app_storage_path
    the_path = app_storage_path() + '/app'
elif platform in ('macosx', 'win', 'linux'):
    the_path = os.path.dirname(os.path.realpath('__main__.py'))        
else:
    raise NotImplementedError("FTS service not implemented on this platform")
    
app_path = the_path

MAINPATH =  str(Path(rf"{app_path}/FTS"))
PERSISTENCE_PATH = str(Path(rf"{MAINPATH}/PS"))

class MainConfig:
    """
    this is the main configuration file and is the only one which
    should need to be changed
    """

    # the version information of the server (recommended to leave as default)
    version = 'FTS-1.9'
    #
    yaml_path = str(Path(fr'{MAINPATH}/FTSConfig.yaml'))

    python_version = 'python3.8'
    
    APP_PATH = app_path

    #userpath = '/usr/local/lib/'

    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "0.0.0.0"
        
    # create the main path if it doesn't exist
    if not os.path.exists(MAINPATH):
        try:
            os.mkdir(MAINPATH)
        except Exception as e:
            print(f"failed to create the fts main directory at {MAINPATH} with error: {e}")
            sys.exit(1)
    
    # create the persistence path if it doesn't exist
    if not os.path.exists(PERSISTENCE_PATH):
        try:
            os.mkdir(PERSISTENCE_PATH)
        except Exception as e:
            print(f"failed to create the fts persistence directory at {PERSISTENCE_PATH} with error: {e}")
            sys.exit(1)

    if not os.path.exists(yaml_path):

        SecretKey = str('vnkdjnfjknfl1232#')

        OptimizeAPI = True

        DataReceptionBuffer = int(1024)

        MaxReceptionTime = int(4)

        MainLoopDelay = int(100)

        # this is the port to which clients will connect
        CoTServicePort = int(15280)

        SSLCoTServicePort = int(15480)

        # this needs to be changed for private data packages to work
        DataPackageServiceDefaultIP = str('0.0.0.0')

        # User Connection package IP needs to be set to the IP which is used when creating the connection in your tak device
        UserConnectionIP = str('0.0.0.0')

        # api port
        APIPort = int(19023)

        # Federation port
        FederationPort = int(9000)

        # api IP
        APIIP = str('0.0.0.0')

        # whether or not to save CoT's to the DB
        SaveCoTToDB = bool(True)

        # this should be set before startup
        DBFilePath = str(Path(fr'{PERSISTENCE_PATH}/FTSDataBase.db'))

        MainPath = str(Path(MAINPATH))

        certsPath = str(Path(fr'{MAINPATH}/certs'))

        ExCheckMainPath = str(Path(fr'{MAINPATH}/ExCheck'))

        ExCheckFilePath = str(Path(fr'{MAINPATH}/ExCheck/template'))

        ExCheckChecklistFilePath = str(Path(fr'{MAINPATH}/ExCheck/checklist'))

        DataPackageFilePath = str(Path(fr'{MAINPATH}/FTSDPFolder'))

        LogFilePath = str(Path(fr'{MAINPATH}/Logs'))

        federationKeyPassword = str('defaultpass')

        keyDir = str(Path(fr'{certsPath}/server.key'))

        pemDir = str(Path(fr'{certsPath}/server.pem')) # or crt

        testPem = str(pemDir)

        testKey = str(keyDir)

        unencryptedKey = str(Path(fr'{certsPath}/server.key.unencrypted'))

        p12Dir = str(Path(fr'{certsPath}/server.p12'))

        CA = str(Path(fr'{certsPath}/ca.pem'))

        CAkey = str(Path(fr'{certsPath}/ca.key'))

        federationCert = str(Path(fr'{certsPath}/server.pem'))

        federationKey = str(Path(fr'{certsPath}/server.key'))

        federationKeyPassword = str('defaultpass')

        password = str('supersecret')

        websocketkey = str("YourWebsocketKey")

        CRLFile = str(fr"{certsPath}/FTS_CRL.json")

        # set to None if you don't want a message sent
        ConnectionMessage = f'{version}'

        DataBaseType = str("SQLite")

    else:
        content = open(yaml_path).read()
        yamlConfig = yaml.safe_load(content)

        # number of milliseconds to wait between each iteration of main loop
        # decreasing will increase CPU usage and server performance
        # increasing will decrease CPU usage and server performance
        DataBaseType = str(yamlConfig["System"]["FTS_DATABASE_TYPE"])
        # set to None if you don't want a message sent
        ConnectionMessage = str(yamlConfig["System"]["FTS_CONNECTION_MESSAGE"])
        MainLoopDelay = int(yamlConfig["System"]["FTS_MAINLOOP_DELAY"])
        OptimizeAPI = bool(yamlConfig["System"]["FTS_OPTIMIZE_API"])
        SecretKey = str( yamlConfig["System"]["FTS_SECRET_KEY"])
        DataReceptionBuffer = int(yamlConfig["System"]["FTS_DATA_RECEPTION_BUFFER"])
        MaxReceptionTime = int(yamlConfig["System"]["FTS_MAX_RECEPTION_TIME"])

        # this is the port to which clients will connect
        CoTServicePort = int(yamlConfig["Addresses"]["FTS_COT_PORT"])

        SSLCoTServicePort = int(yamlConfig["Addresses"]["FTS_SSLCOT_PORT"])

        # this needs to be changed for private data packages to work
        DataPackageServiceDefaultIP = str(yamlConfig["Addresses"]["FTS_DP_ADDRESS"])

        # User Connection package IP needs to be set to the IP which is used when creating the connection in your tak device
        UserConnectionIP = str(yamlConfig["Addresses"]["FTS_USER_ADDRESS"])

        # api port
        APIPort = int(yamlConfig["Addresses"]["FTS_API_PORT"])

        # Federation port
        FederationPort = int(yamlConfig["Addresses"]["FTS_FED_PORT"])

        # api IP
        APIIP = str(yamlConfig["Addresses"]["FTS_API_ADDRESS"])
       

        DBFilePath = str(yamlConfig["FileSystem"]["FTS_DB_PATH"])

        # whether or not to save CoT's to the DB
        SaveCoTToDB = bool(yamlConfig["FileSystem"]["FTS_COT_TO_DB"])

        MainPath = str(yamlConfig["FileSystem"]["FTS_MAINPATH"])

        certsPath = str(yamlConfig["FileSystem"]["FTS_CERTS_PATH"])

        ExCheckMainPath = str(yamlConfig["FileSystem"]["FTS_EXCHECK_PATH"])

        ExCheckFilePath = str(yamlConfig["FileSystem"]["FTS_EXCHECK_TEMPLATE_PATH"])

        ExCheckChecklistFilePath = str(yamlConfig["FileSystem"]["FTS_EXCHECK_CHECKLIST_PATH"])

        DataPackageFilePath = str(yamlConfig["FileSystem"]["FTS_DATAPACKAGE_PATH"])

        LogFilePath = str(yamlConfig["FileSystem"]["FTS_LOGFILE_PATH"])


        keyDir = str(yamlConfig["Certs"]["FTS_SERVER_KEYDIR"])

        pemDir = str(yamlConfig["Certs"]["FTS_SERVER_PEMDIR"]) # or crt

        testPem = str(yamlConfig["Certs"]["FTS_TESTCLIENT_PEMDIR"])

        testKey = str(yamlConfig["Certs"]["FTS_TESTCLIENT_KEYDIR"])

        unencryptedKey = str(yamlConfig["Certs"]["FTS_UNENCRYPTED_KEYDIR"])

        p12Dir = str(yamlConfig["Certs"]["FTS_SERVER_P12DIR"])

        CA = str(yamlConfig["Certs"]["FTS_CADIR"])

        CAkey = str(yamlConfig["Certs"]["FTS_CAKEYDIR"])

        federationCert = str(yamlConfig["Certs"]["FTS_FEDERATION_CERTDIR"])

        federationKey = str( yamlConfig["Certs"]["FTS_FEDERATION_KEYDIR"])

        federationKeyPassword = str(yamlConfig["Certs"]["FTS_FEDERATION_KEYPASS"])

        password = str(yamlConfig["Certs"]["FTS_CLIENT_CERT_PASSWORD"])

        websocketkey = str(yamlConfig["Certs"]["FTS_WEBSOCKET_KEY"])

        CRLFile = str(yamlConfig["Certs"]["FTS_CRLDIR"])



    # allowed ip's to access CLI commands
    AllowedCLIIPs = ['127.0.0.1']

    # IP for CLI to access
    CLIIP = '127.0.0.1'

    APIVersion = "1.9.5"

    # format of API message header should be {Authentication: Bearer 'TOKEN'}
    from uuid import uuid4
    id = str(uuid4())

    nodeID = f"FreeTAKServer-{id}"

    # location to backup client packages
    clientPackages = str(Path(fr'{MAINPATH}/certs/ClientPackages'))

    first_start = True
