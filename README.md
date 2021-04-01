# pyAPIsCaller  :pushpin:
### 01.04.2021 - 
- TESTING RIOT GAMES API :newspaper::
    - https://developer.riotgames.com/apis
        - You must login with your Riot Games account on their developer portal. This action also generates a basic development API key that is associated with your account and you can test the API.
        - In this project that key have to be in a file called key.key
    
    - Usage :computer:
        - python main.py -c "Swain" | Return extra information about Swain.
        - python main.py -s "SummonerName" | Return information about that summoner(In game name). 
    
    - Both create a file .json with the data.
    - Summoner method create a resume in .txt :information_desk_person:
       
        [+]Name: 
       
            Level: 
       
            champ with mastery: 
       
        [+]Champ with most mastery:
       
            Name: 
       
            Level: 
       
            Points: 
       
            Chest?: 
       
            Last time played: 
       
            [+]Info extra:
       
                Title: 
       
                Blurb: 
       
                Tags: 
       
                Partype: 
       
                Stats: 
    
    - Summoner file :ok_woman:
        
        {
        
            "_name": ,
        
            "_id": ,
        
            "_level": ,
        
            "_champions": [
        
                    {}
        
                ],
        
            "_mostMasteryChamp": {
        
                 "id": ,
        
                "level": ,
        
                "points": ,
        
                "chest": ,
        
                "lastTimePlayed": ,
        
                "name": ,
        
        
                "infoExtra": {}
        
            }
        }

    - Champion file: :baby_chick:
       
        "type": ,
       
        "format": ,
       
        "version": ,
       
        "data": {


       
        }

- apiCaller.py :speech_balloon:
    - Simple get and post.