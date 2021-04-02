import datetime
from configparser import ConfigParser
import json

def getKey():
    try:
        with open("key.key", 'r') as f:
            k = f.read()
            return k
        return None
    except Exception as ex:
        print(f"Except: {ex}")
        return None

def parseMiliSecondsToDateTime(ms):
    try:
        print(f"{ms} ms")    
        segundos = ms / 1000.0
        return datetime.datetime.fromtimestamp(segundos).strftime('%d/%m/%Y %H:%M:%S')
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def getAllServers():
    try:
        servers = dict()
        with open("servers.json", 'r') as f:
            strr = f.read()
            servers = json.loads(strr)        
        return servers
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def getServer():
    try:
        config = ConfigParser()
        config.read("conf.ini")
        servidores = getAllServers()
        if servidores == None:
            return None
        servidor = servidores[config['RIOTAPI']['SERVER']]
        return servidor     
    except Exception as ex:        
        print(f"{ex}")
        return None


def getLang():
    try:
        config = ConfigParser()
        config.read("conf.ini")
        return config['RIOTAPI']['LANG']     
    except Exception as ex:        
        print(f"{ex}")
        return None

def getDdragonPath():
    try:
        config = ConfigParser()
        config.read("conf.ini")
        return f"{config['RIOTAPI']['DDRAGONROOT']}{config['RIOTAPI']['DDRAGONVER']}"
    except Exception as ex:        
        print(f"{ex}")
        return None


def rootPokeApi():
    try:
        config = ConfigParser()
        config.read("conf.ini")
        return config['POKEAPI']['PATHROOT']
    except Exception as ex:        
        print(f"{ex}")
        return None        

def gettingSecretsSHH():
    try:
        config = ConfigParser()
        config.read("auth.key")
        return config['HUBBY']['client'], config['HUBBY']['secret']
    except Exception as ex:        
        print(f"{ex}")
        return None, None   

def getTokenTEMP():
    try:
        config = ConfigParser()
        config.read("auth.key")
        return config['HUBBY']['token']
    except Exception as ex:        
        print(f"{ex}")
        return None   