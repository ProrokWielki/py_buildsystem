import json

class Compiler:
    def __init__(self, config_json_file = 0):      
        
        self.__is_configured = False
         
        if config_json_file is not 0:
            self.read_config_file(config_json_file)
        
    def read_config_file(self, config_json_file):
        with open(config_json_file) as config_file:
            configuration = json.load(config_file)
        
        self.__compiler_path = configuration["compiler_path"]
        self.__compiler_name = configuration["compiler_name"]
        self.__linker_name   = configuration["linker_name"]
        
        self.__is_configured = True

    def get_compiler_path(self):
        self.__check_is_configured()   
                
        return self.__compiler_path 
    
    def get_compiler_name(self):
        self.__check_is_configured()   
        
        return self.__compiler_name 
    
    def get_linker_name(self):
        self.__check_is_configured()   
        
        return self.__linker_name 
    
    def compile(self, list_of_files):
        pass
    
    def __check_is_configured(self):
        assert self.__is_configured is True, "Load configuration file first."
       