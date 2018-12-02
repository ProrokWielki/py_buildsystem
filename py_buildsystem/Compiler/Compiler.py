import os
import sys
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

from ConfigReader.ConfigReader import ConfigReader 

class Compiler(ConfigReader):

    def get_compiler_path(self):
        return self.__compiler_path 
    
    def _check_config(self):
        try:
            
            self.__compiler_path = self.configuration["compiler_path"]            
            self.__compiler_name = self.configuration["compiler_name"]            
            self.__linker_name   = self.configuration["linker_name"]        

            self.__define_flag  = self.configuration["define_flag"]
            self.__output_flag  = self.configuration["output_flag"]
            self.__compile_flag = self.configuration["compile_flag"]
            self.__include_flag = self.configuration["include_flag"]            
                   
        except:
            raise Exception('Given configuration file is incorrect.')
                    
        assert isinstance(self.__compiler_path, str), "'compiler_path' must be a string"
        assert isinstance(self.__compiler_name, str), "'compiler_name' must be a string"
        assert isinstance(self.__linker_name, str),   "'linker_name' must be a string"

        assert isinstance(self.__define_flag, str),  "'define_flag' must be a string"
        assert isinstance(self.__output_flag , str), "'output_flag' must be a string"  
        assert isinstance(self.__compile_flag, str), "'compile_flag' must be a string"         
        assert isinstance(self.__include_flag, str), "'include_flag' must be a string" 
    
    def get_compiler_name(self):
        return self.__compiler_name 
    
    def get_linker_name(self):
        return self.__linker_name 
    
    def compile(self, list_of_files, project_cofiguration):
        pass
    

       