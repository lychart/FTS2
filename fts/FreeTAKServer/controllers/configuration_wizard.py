from typing import List
import os
from FreeTAKServer.controllers.configuration.MainConfig import MainConfig
#from ruamel.yaml import YAML
#yaml = YAML()
import yaml
import pathlib
from pathlib import Path
from kivy.utils import platform



# TODO: refactor this
def get_user_input(*, question: str, default: str = None, options: list = None):
    input_string = question
    if default:
        input_string += f" [{default}]: "
        choice = input(input_string)
        if not choice:
            return default
        else:
            return choice
    """else:
        print(question+f" [{default}]: "+"\n")
        for option in range(0, len(options)):
            print(option)"""

def add_to_config(path: List[str], data: str, source: dict):
    for index in range(0, len(path)):
        entry = path[index]
        if index == len(path) - 1:
            source[entry] = data
            break
        if source.get(entry):
            source = source[entry]
        else:
            source[entry] = {}
            source = source[entry]

    print(data)

def ask_user_for_config():
    yaml_path = MainConfig.yaml_path
    yaml_config = yaml.safe_load(default_yaml_file)
    
    """
    with open(pathlib.PurePath(Path(fr'{MainConfig.APP_PATH}/FreeTAKServer/controllers/configuration/MainConfig.py')), mode="r+") as file:
        data = file.readlines()
        data[-1] = "    first_start = False"
    with open(pathlib.PurePath(Path(fr'{MainConfig.APP_PATH}/FreeTAKServer/controllers/configuration/MainConfig.py')), mode="w+") as file:
        file.writelines(data)
    """
    
    file = open(yaml_path, mode="w+")
    yaml.dump(yaml_config, file)
    file.close()


default_yaml_file = f"""
System:
  FTS_DATABASE_TYPE: SQLite
  FTS_CONNECTION_MESSAGE: {MainConfig.version}
  FTS_OPTIMIZE_API: True
  FTS_MAINLOOP_DELAY: 100
  FTS_SECRET_KEY: vnkdjnfjknfl1232#
  FTS_DATA_RECEPTION_BUFFER: 1024
  FTS_MAX_RECEPTION_TIME: 4
Addresses:
  FTS_COT_PORT: 15280
  FTS_SSLCOT_PORT: 15480
  FTS_DP_ADDRESS: 0.0.0.0
  FTS_USER_ADDRESS: 0.0.0.0
  FTS_API_PORT: 19023
  FTS_FED_PORT: 9000
  FTS_API_ADDRESS: 0.0.0.0
FileSystem:
  FTS_DB_PATH: {MainConfig.DBFilePath}
  FTS_COT_TO_DB: True
  FTS_MAINPATH: {MainConfig.MainPath}
  FTS_CERTS_PATH: {MainConfig.MainPath}/certs
  FTS_EXCHECK_PATH: {MainConfig.MainPath}/ExCheck
  FTS_EXCHECK_TEMPLATE_PATH: {MainConfig.MainPath}/ExCheck/template
  FTS_EXCHECK_CHECKLIST_PATH: {MainConfig.MainPath}/ExCheck/checklist
  FTS_DATAPACKAGE_PATH: {MainConfig.MainPath}/FTSDPFolder
  FTS_LOGFILE_PATH: {MainConfig.MainPath}/Logs
Certs:
  FTS_SERVER_KEYDIR: {MainConfig.MainPath}/certs/server.key
  FTS_SERVER_PEMDIR: {MainConfig.MainPath}/certs/server.pem
  FTS_TESTCLIENT_PEMDIR: {MainConfig.MainPath}/certs/Client.pem
  FTS_TESTCLIENT_KEYDIR: {MainConfig.MainPath}/certs/Client.key
  FTS_UNENCRYPTED_KEYDIR: {MainConfig.MainPath}/certs/server.key.unencrypted
  FTS_SERVER_P12DIR: {MainConfig.MainPath}/certs/server.p12
  FTS_CADIR: {MainConfig.MainPath}/certs/ca.pem
  FTS_CAKEYDIR: {MainConfig.MainPath}/certs/ca.key
  FTS_FEDERATION_CERTDIR: {MainConfig.MainPath}/certs/server.pem
  FTS_FEDERATION_KEYDIR: {MainConfig.MainPath}/certs/server.key
  FTS_FEDERATION_KEYPASS: demopassfed
  FTS_CLIENT_CERT_PASSWORD: demopasscert
  FTS_WEBSOCKET_KEY: YourWebsocketKey
  FTS_CRLDIR: {MainConfig.MainPath}/certs/FTS_CRL.json
"""
