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
    the_path = app_storage_path()
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
        CoTServicePort = int(8087)

        SSLCoTServicePort = int(8089)

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
        if yamlConfig.get("System"):
            MainLoopDelay = int(yamlConfig["System"].get("FTS_MAINLOOP_DELAY", 1))
            # set to None if you don't want a message sent
            ConnectionMessage = str(yamlConfig["System"].get("FTS_CONNECTION_MESSAGE", f'{version}'))
            DataBaseType = str(yamlConfig["System"].get("FTS_DATABASE_TYPE", "SQLite"))
            OptimizeAPI = bool(yamlConfig["System"].get("FTS_OPTIMIZE_API", True))
            SecretKey = str( yamlConfig["System"].get("FTS_SECRET_KEY", 'vnkdjnfjknfl1232#'))
            DataReceptionBuffer = int(yamlConfig["System"].get("FTS_DATA_RECEPTION_BUFFER", 1024))
            MaxReceptionTime = int(yamlConfig["System"].get("FTS_MAX_RECEPTION_TIME", 4))

        else:
            MainLoopDelay = int(1)
            ConnectionMessage = str(f'{version}')
            DataBaseType = str("SQLite")
            OptimizeAPI = bool(True)

        if yamlConfig.get("Addresses"):
            # this is the port to which clients will connect
            CoTServicePort = int(yamlConfig["Addresses"].get('FTS_COT_PORT', 8087))

            SSLCoTServicePort = int(yamlConfig["Addresses"].get('FTS_SSLCOT_PORT', 8089))

            # this needs to be changed for private data packages to work
            DataPackageServiceDefaultIP = str(yamlConfig["Addresses"].get('FTS_DP_ADDRESS', '0.0.0.0'))

            # User Connection package IP needs to be set to the IP which is used when creating the connection in your tak device
            UserConnectionIP = str(yamlConfig["Addresses"].get("FTS_USER_ADDRESS", '0.0.0.0'))

            # api port
            APIPort = int(yamlConfig["Addresses"].get("FTS_API_PORT", 19023))

            # Federation port
            FederationPort = int(yamlConfig["Addresses"].get("FTS_FED_PORT", 9000))

            # api IP
            APIIP = str(yamlConfig["Addresses"].get("FTS_API_ADDRESS", "0.0.0.0"))
        else:

            # this is the port to which clients will connect
            CoTServicePort = int(8087)

            SSLCoTServicePort = int(8089)

            # this needs to be changed for private data packages to work
            DataPackageServiceDefaultIP = str("0.0.0.0")

            # User Connection package IP needs to be set to the IP which is used when creating the connection in your tak device
            UserConnectionIP = str("0.0.0.0")

            # api port
            APIPort = int(19023)

            # Federation port
            FederationPort = int(9000)

            # api IP
            APIIP = str('0.0.0.0')

        if yamlConfig.get("FileSystem"):

            DBFilePath = str(yamlConfig["FileSystem"].get("FTS_DB_PATH", str(Path(fr'{PERSISTENCE_PATH}/FTSDataBase.db'))))

            # whether or not to save CoT's to the DB
            SaveCoTToDB = bool(yamlConfig["FileSystem"].get("FTS_COT_TO_DB"))

            MainPath = str(yamlConfig["FileSystem"].get("FTS_MAINPATH", str(Path(MAINPATH))))

            certsPath = str(yamlConfig["FileSystem"].get("FTS_CERTS_PATH", fr'{MAINPATH}/certs'))

            ExCheckMainPath = str(yamlConfig["FileSystem"].get("FTS_EXCHECK_PATH",Path(fr'{MAINPATH}/ExCheck')))

            ExCheckFilePath = str(yamlConfig["FileSystem"].get("FTS_EXCHECK_TEMPLATE_PATH", Path(fr'{MAINPATH}/ExCheck/template')))

            ExCheckChecklistFilePath = str( yamlConfig["FileSystem"].get("FTS_EXCHECK_CHECKLIST_PATH", Path(fr'{MAINPATH}/ExCheck/checklist')))

            DataPackageFilePath = str(yamlConfig["FileSystem"].get("FTS_DATAPACKAGE_PATH", Path(fr'{MAINPATH}/FTSDPFolder')))

            LogFilePath = str(yamlConfig["FileSystem"].get("FTS_LOGFILE_PATH", Path(fr"{MAINPATH}/Logs")))

        else:
            # whether or not to save CoT's to the DB
            SaveCoTToDB = bool(True)

            # this should be set before startup
            DBFilePath = str(Path(fr'{PERSISTENCE_PATH}/FTSDataBase.db'))

            MainPath = str(Path(MAINPATH))

            certsPath = str(fr'{MAINPATH}/certs')

            ExCheckMainPath = str(Path(fr'{MAINPATH}/ExCheck'))

            ExCheckFilePath = str(Path(fr'{MAINPATH}/ExCheck/template'))

            ExCheckChecklistFilePath = str(Path(fr'{MAINPATH}/ExCheck/checklist'))

            DataPackageFilePath = str(Path(fr'{MAINPATH}/FTSDPFolder'))

            LogFilePath = str(Path(fr"{MAINPATH}/Logs"))


        if yamlConfig.get("Certs"):
            keyDir = str(yamlConfig["Certs"].get("FTS_SERVER_KEYDIR", Path(fr'{certsPath}/server.key')))

            pemDir = str(yamlConfig["Certs"].get("FTS_SERVER_PEMDIR", Path(fr'{certsPath}/server.pem'))) # or crt

            testPem = str(yamlConfig["Certs"].get("FTS_TESTCLIENT_PEMDIR", fr'{certsPath}/Client.pem'))

            testKey = str(yamlConfig["Certs"].get("FTS_TESTCLIENT_KEYDIR", fr'{certsPath}/Client.key'))

            unencryptedKey = str(yamlConfig["Certs"].get("FTS_UNENCRYPTED_KEYDIR", Path(fr'{certsPath}/server.key.unencrypted')))

            p12Dir = str(yamlConfig["Certs"].get("FTS_SERVER_P12DIR", Path(fr'{certsPath}/server.p12')))

            CA = str(yamlConfig["Certs"].get("FTS_CADIR",Path(fr'{certsPath}/ca.pem')))

            CAkey = str(yamlConfig["Certs"].get("FTS_CAKEYDIR",Path(fr'{certsPath}/ca.key')))

            federationCert = str(yamlConfig["Certs"].get("FTS_FEDERATION_CERTDIR", Path(fr'{certsPath}/server.pem')))

            federationKey = str( yamlConfig["Certs"].get("FTS_FEDERATION_KEYDIR", Path(fr'{certsPath}/server.key')))

            federationKeyPassword = str(yamlConfig["Certs"].get("FTS_FEDERATION_KEYPASS", None))

            password = str(yamlConfig["Certs"].get("FTS_CLIENT_CERT_PASSWORD", 'supersecret'))

            websocketkey = str(yamlConfig["Certs"].get("FTS_WEBSOCKET_KEY", "YourWebsocketKey"))

            CRLFile = str(yamlConfig["Certs"].get("FTS_CRLDIR", fr"{certsPath}/FTS_CRL.json"))
        else:
            federationKeyPassword = str('defaultpass')

            keyDir = str(Path(fr'{certsPath}/server.key'))

            pemDir = str(Path(fr'{certsPath}/server.pem'))  # or crt

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

    first_start = False
