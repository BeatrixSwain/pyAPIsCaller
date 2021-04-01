import requests
import json
from summoner import Summoner
import utils

# API caller using RIOT API.
# Only get data of an player using his summoner name


def getSummonerInfoByName(name, key):
    try:
        server = utils.getServer()
        if server == None:
            print("Something went wrong getting server name.")
            return None, None
        url = f'https://{server}/lol/summoner/v4/summoners/by-name/{name}'
        headers = {
            "X-Riot-Token": key
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            print("Status response: Ok!")
            j = res.json()
            # print(f"Info summoner: {j}") 
            return j['id'], j['summonerLevel']
        else:
            print(f"Error[{res.status_code}]: {res.text}")
            return None, None
    except Exception as ex:
        print(f"Exception: {ex}")
        return None, None
  
def getChampsMastery(idSum, key):
    try:
        server = utils.getServer()
        if server == None:
            print("Something went wrong getting server name.")
            return None, None

        url = f'https://{server}/lol/champion-mastery/v4/champion-masteries/by-summoner/{idSum}'
        headers = {
            "X-Riot-Token": key
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            print(f"Error[{res.status_code}]: {res.text}")
            return None, None
    except Exception as ex:
        print(f"Exception: {ex}")
        return None, None

def processChampRecord(champ):
    try:
        champion = dict()
        champion['id'] = champ['championId']
        champion['level'] = champ['championLevel']
        champion['points'] = champ['championPoints']
        champion['chest'] = champ['chestGranted']
        champion['lastTimePlayed'] = utils.parseMiliSecondsToDateTime(champ['lastPlayTime']) #API return it on Unix milliseconds time format.
        infoChamp = getChampFromddragonJson(str(champ['championId']))
        if(infoChamp==None):
            print("Something went wrong getting the champion's data")
            return None
        champion['name'] = infoChamp['name']
        champion['infoExtra'] = infoChamp
        return champion
    except Exception as ex:
        print(f"Exception: {ex}")
        return None

def getChampFromddragonJson(id):
    try:
        pathRoot = utils.getDdragonPath()
        lang = utils.getLang()
        if pathRoot==None or lang==None:
            print("Something went wrong getting the data.")
            return None

        url = f'{pathRoot}{lang}/champion.json'
        res = requests.get(url)
        if res.status_code == 200:
            print("Response Status: Ok")
            listChampions = res.json()
            print(f"Resume: {listChampions['type']}, {listChampions['version']}")
            data = listChampions['data']
            print(f"{len(data)} number of champions returned")
            nameChamp = ''
            for name, datas in data.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if datas['key'] == id:
                    nameChamp = name
            if len(nameChamp.strip()) > 0:
                # print(f"Champ found: {nameChamp}")    
                # print(f"{nameChamp}'s info:")
                # print(data[nameChamp])
                return data[nameChamp]
            else:
                print(f"Champ not found.")    
                return None
        else:
            print("Something went wrong!")
            print(f"Error[{res.status_code}]: {res.text}")
            return None

    except Exception as ex:
        print(f"Exception: {ex}")
        return None

###############################################################
def getInfoSummoner(name):
    try:
        summ = Summoner()
        summ.name = name
        k = utils.getKey()
        id, level = getSummonerInfoByName(name, k)
        if id!=None and level !=None:
            # print(f"Id recuperado: {id}") 
            summ.id = id
            summ.level = level

            #Obtener los champs con puntos de maestría.            
            summ.champions = getChampsMastery(summ.id, k) 
            # print(summ.champions)
            mostMastery = summ.champions[0]
            recordChamp = processChampRecord(mostMastery)
            if recordChamp != None:
                summ.mostMasteryChamp = recordChamp

            with open(f"test_{name}.json", "w") as f:
              f.write(str(summ))
           
            resume = f"[+]Name: {summ.name}\n\tLevel: {summ.level}\n\tchamp with mastery: {len(summ.champions)}.\n[+]Champ with most mastery:\n\tName: {summ.mostMasteryChamp['name']}\n\tLevel: {summ.mostMasteryChamp['level']}"
            resume += f"\n\tPoints: {summ.mostMasteryChamp['points']}\n\tChest?: {summ.mostMasteryChamp['chest']}\n\tLast time played: {summ.mostMasteryChamp['lastTimePlayed']}"
            resume += "\n\t[+]Info extra:"
            resume += f"\n\t\tTitle: {summ.mostMasteryChamp['infoExtra']['title']}\n\t\tBlurb: {summ.mostMasteryChamp['infoExtra']['blurb']}\n\t\tTags: {summ.mostMasteryChamp['infoExtra']['tags']}"
            resume += f"\n\t\tPartype: {summ.mostMasteryChamp['infoExtra']['partype']}\n\t\tStats: {summ.mostMasteryChamp['infoExtra']['stats']}"

            print(resume)
            with open(f"test_{name}.txt", "w") as f:
              f.write(resume)
            print("Information Saved!")
            print("File: "+f"test_{name}.txt")
        else:
            print("Something went wrong getting the data.") 

    except Exception as ex:
        print(f"Except: {ex}")

def getMoreInfoChamp(nameChamp):
    try:
        # print(f"Id:{id} ")
        pathRoot = utils.getDdragonPath()
        lang = utils.getLang()
        if pathRoot==None or lang==None:
            print("Something went wrong getting the data.")
            return None

        url = f'{pathRoot}{lang}/champion/{nameChamp}.json'
        print(url)
        res = requests.get(url)
        if res.status_code == 200:
            print("Response Status: Ok")
            info = res.json()
            with open(f"test_{nameChamp}.json", 'w') as f:
                f.write(json.dumps(info))
            # print(info)
            print("Information Saved!")
            print("File: "+f"test_{nameChamp}.json")

        else:
            print(f"Error[{res.status_code}]: {res.text}")
            return None

    except Exception as ex:
        print(f"Exception: {ex}")
        return None