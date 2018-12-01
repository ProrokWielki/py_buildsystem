import json

class Compiler:
    def __init__(self, config_json_file):      
        
        self.__is_configured = False
                 
        self.read_config_file(config_json_file)
        
    def read_config_file(self, config_json_file):
        try:
            with open(config_json_file) as config_file:
                configuration = json.load(config_file)
        except:
            raise Exception('Given configuration file does not exist.')
        
        try:
            
            self.__compiler_path = configuration["compiler_path"]            
            self.__compiler_name = configuration["compiler_name"]            
            self.__linker_name   = configuration["linker_name"]        

            self.__define_flag  = configuration["define_flag"]
            self.__output_flag  = configuration["output_flag"]
            self.__compile_flag = configuration["compile_flag"]
            self.__include_flag = configuration["include_flag"]            
                   
        except:
            raise Exception('Given configuration file is incorrect.')
                    
        assert isinstance(self.__compiler_path, str), "'compiler_path' must be a string"
        assert isinstance(self.__compiler_name, str), "'compiler_name' must be a string"
        assert isinstance(self.__linker_name, str),   "'linker_name' must be a string"

        assert isinstance(self.__define_flag, str),  "'define_flag' must be a string"
        assert isinstance(self.__output_flag , str), "'output_flag' must be a string"  
        assert isinstance(self.__compile_flag, str), "'compile_flag' must be a string"         
        assert isinstance(self.__include_flag, str), "'include_flag' must be a string" 
        
        self.__is_configured = True        

    def get_compiler_path(self):
        self.__assert_not_configured()   
                
        return self.__compiler_path 
    
    def get_compiler_name(self):
        self.__assert_not_configured()   
        
        return self.__compiler_name 
    
    def get_linker_name(self):
        self.__assert_not_configured()   
        
        return self.__linker_name 
    
    def compile(self):
        pass
    
    def __assert_not_configured(self):
        assert self.__is_configured is True, "Load configuration file first."
       