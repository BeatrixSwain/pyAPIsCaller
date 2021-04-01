import requests
import json
from summoner import Summoner
import datetime
import LOLAPICaller as lol
import utils
import sys


##        
if __name__ == "__main__":
    try:
        params = sys.argv[1:] 
        numParam =  len(params)
        print("{0} parameters received: {1}".format(numParam, params))
        if numParam<=1:
            print("Parameters missing")
            print("Format:\n\t-c ChampName (Use quotation marks)")
            print("       \n\t-s SummonerName  (Use quotation marks)")
        else:
            prev = ''
            for x in params:
                if len(prev.strip()) == 0:
                    prev = x
                else:
                    if prev == "-s":
                        lol. getInfoSummoner(x)
                    elif prev == "-c":
                        lol.getMoreInfoChamp(x)
                    else:
                        print(f"Unknow param: {prev}")
                        break
    except:
        print("{0}{1}".format(sys.exc_info()[0], sys.exc_info()[1]))
