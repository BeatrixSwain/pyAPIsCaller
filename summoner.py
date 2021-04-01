import json

class Summoner:
    def __init__(self, nombre = '', id = '', level = '', champions = {}, mostMasteryChamp = {}):
        self._name =  nombre
        self._id = id
        self._level = level
        self._champions = champions
        self._mostMasteryChamp = mostMasteryChamp

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, val):
        self._level = val

    @property
    def champions(self):
        return self._champions
    
    @champions.setter
    def champions(self, val):
        self._champions = val
    
    @property
    def mostMasteryChamp(self):
        return self._mostMasteryChamp
    
    @mostMasteryChamp.setter
    def mostMasteryChamp(self, val):
        self._mostMasteryChamp = val    

    def __str__(self):
        return json.dumps(self.__dict__)