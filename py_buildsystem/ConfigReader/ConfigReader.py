import json

from abc import ABC, abstractmethod

class ConfigReader(ABC):
    def __init__(self, config_json_file):      
        self.read_config_file(config_json_file)
        
        self._check_config()
        
    def read_config_file(self, config_json_file):
        try:
            with open(config_json_file) as config_file:
                self.configuration = json.load(config_file)
        except:
            raise Exception('Given configuration file does not exist.')
        
        @abstractmethod
        def _check_config(self):
            pass        
