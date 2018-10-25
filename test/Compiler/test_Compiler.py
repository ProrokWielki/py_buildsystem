import os
import json
import shutil

import unittest

from lib.Compiler.Compiler import Compiler

script_file_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

test_files_dir_name = "test_files"
test_config_file_name = "test_file.json"
test_compiler_dir_name = "test_compier" 
test_compiler_name = "test_compiler.exe"
test_linker_name   = "test_linker.exe" 

test_files_path = os.path.join(script_file_path, test_files_dir_name).replace("\\", "/")

test_config_file_with_path = os.path.join(test_files_path, test_config_file_name).replace("\\", "/")
test_compiler_path =  os.path.join(test_files_path, test_files_dir_name).replace("\\", "/")

test_linker_exe_path = os.path.join(test_compiler_path, test_linker_name).replace("\\", "/")
test_compiler_exe_path = os.path.join(test_compiler_path, test_compiler_name).replace("\\", "/")

compiler_test_configuration = {
                              "compiler_path": test_compiler_path,
                              "compiler_name": test_compiler_name,
                              "linker_name":   test_linker_name     
                              }

class TestCompiler(unittest.TestCase):        
    @classmethod
    def setUpClass(cls):      
        os.makedirs(test_files_path, exist_ok=True)
        
        with open(test_config_file_with_path, "w") as test_file:
            json.dump(compiler_test_configuration, test_file, indent=4)
            
        os.makedirs(test_compiler_path, exist_ok=True)
        
        with open(test_linker_exe_path, "wb") as test_file:
            pass
            
        with open(test_compiler_exe_path, "wb") as test_file:
            pass                 
                    
    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree(test_files_path)
        except:
            pass  
    
    def test_read_config(self):
        
        pass
    
    def test_Compile(self):
        pass

        
        