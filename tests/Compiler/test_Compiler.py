import os
import json
import shutil

import unittest

from py_buildsystem.Compiler.Compiler import Compiler

script_file_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

test_files_dir_name = "test_files"
test_config_file_name = "test_file.json"
corrupted_test_config_file_name = "corrupted_test_file.json"
test_compiler_dir_name = "test_compier" 
test_compiler_name = "test_compiler.exe"
test_linker_name   = "test_linker.exe" 

test_files_path = os.path.join(script_file_path, test_files_dir_name).replace("\\", "/")

test_config_file_with_path = os.path.join(test_files_path, test_config_file_name).replace("\\", "/")
corrupted_test_config_file_with_path = os.path.join(test_files_path, corrupted_test_config_file_name).replace("\\", "/")
test_compiler_path =  os.path.join(test_files_path, test_files_dir_name).replace("\\", "/")

test_linker_exe_path = os.path.join(test_compiler_path, test_linker_name).replace("\\", "/")
test_compiler_exe_path = os.path.join(test_compiler_path, test_compiler_name).replace("\\", "/")

compiler_test_configuration = {
                              "compiler_path": test_compiler_path,
                              "compiler_name": test_compiler_name,
                              "linker_name":   test_linker_name,
                              
                              "define_flag": "-D",
                              "output_flag": "-o",
                              "compile_flag": "-c",
                              "include_flag": "-I"     
                              }

class TestCompiler(unittest.TestCase):        
    @classmethod
    def setUpClass(cls):      
        os.makedirs(test_files_path, exist_ok=True)
        
        with open(test_config_file_with_path, "w") as test_file:
            json.dump(compiler_test_configuration, test_file, indent=2)
            
        with open(corrupted_test_config_file_with_path, "w") as corrupted_test_file:
            json.dump(dict(list(compiler_test_configuration.items())[2:]), corrupted_test_file, indent=2) #corrpting the json file, by taking only part of the dictionary.
            
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
    
    def test_read_config_file(self):
        
        with self.assertRaises(Exception):
            Compiler("random_text")
            
        with self.assertRaises(Exception):
            Compiler(corrupted_test_config_file_with_path)
            
        compiler = Compiler(test_config_file_with_path)    

        self.assertEqual(compiler.get_compiler_path(), compiler_test_configuration["compiler_path"])
        self.assertEqual(compiler.get_compiler_name(), compiler_test_configuration["compiler_name"])
        self.assertEqual(compiler.get_linker_name(), compiler_test_configuration["linker_name"])
    
    def test_compile(self):
        pass

        
        