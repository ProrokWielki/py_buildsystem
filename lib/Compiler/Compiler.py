import json

class Compiler:
    def __init__(self, config_json_file):
        
        with open(config_json_file) as config_file:
            configuration = json.load(config_file)
        
        self.compiler_path = configuration.compiler_path
        self.compiler_name = configuration.compiler_name
        self.linker_name   = configuration.linker_name
        self.
        
    def compile(self, list_of_files):
        pass
    
       