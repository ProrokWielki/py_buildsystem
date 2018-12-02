import os
import sys
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from ConfigReader.ConfigReader import ConfigReader 

class ProjectConfig(ConfigReader):
    def _check_config(self):
        try:
            self.__project_name            = self.configuration["project_name"]
            self.__sources_root_directory  = self.configuration["sources_root_directory"]
            self.__output_directory        = self.configuration["output_directory"]
            
            self.__defines  = self.configuration["defines"]            
            self.__flags    = self.configuration["flags"]            
            self.__includes = self.configuration["includes"]                
                   
        except:
            raise Exception('Given configuration file is incorrect.')
                    
        assert isinstance(self.__project_name, str),           "'project_name' must be a string"
        assert isinstance(self.__sources_root_directory, str), "'sources_root_directory' must be a string"
        assert isinstance(self.__output_directory, str),       "'output_directory' must be a string"

        assert isinstance(self.__defines, list),  "'defines' must be a string"
        assert isinstance(self.__flags , list),   "'flags' must be a string"  
        assert isinstance(self.__includes, list), "'includes' must be a string"         
    
    def get_project_name(self):
        return self.__project_name
        
    def get_sources_root_directory(self):
        return  self.__sources_root_directory
    
    def get_output_directory(self):
        return self.__output_directory
    
    def get_defines(self):
        return self.__defines
    
    def get_flags(self):
        return self.__flags
    
    def get_includes(self):
        return self.__includes