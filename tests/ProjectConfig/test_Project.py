import os
import json
import shutil

import unittest

from py_buildsystem.ProjectConfig.ProjectConfig import ProjectConfig

script_file_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

test_files_dir_name = "test_files"
test_config_file_name = "test_file.json"
corrupted_test_config_file_name = "corrupted_test_file.json"

test_files_path = os.path.join(script_file_path, test_files_dir_name).replace("\\", "/")

test_config_file_with_path = os.path.join(test_files_path, test_config_file_name).replace("\\", "/")
corrupted_test_config_file_with_path = os.path.join(test_files_path, corrupted_test_config_file_name).replace("\\", "/")

project_test_configuration = {
                              "defines": ["STM32L452xx"],

                              "flags": ["-g", 
                                        "-T ../../MCU/STM32L452RETx_FLASH.ld", 
                                        "-mcpu=cortex-m4", 
                                        "--specs=nosys.specs" ],
    
                              "includes": ["../../LIB/CMSIS/Device/ST/STM32L4xx/Include",
                                           "../../LIB/CMSIS/Include" ],

                              "project_name": "Wooden_Clock",
  
                              "sources_root_directory": "../../woodenClock/Software",
                              "output_directory": "../../Output" 
                              }

class TestProjectConfig(unittest.TestCase):        
    @classmethod
    def setUpClass(cls):      
        os.makedirs(test_files_path, exist_ok=True)
        
        with open(test_config_file_with_path, "w") as test_file:
            json.dump(project_test_configuration, test_file, indent=2)
            
        with open(corrupted_test_config_file_with_path, "w") as corrupted_test_file:
            json.dump(dict(list(project_test_configuration.items())[2:]), corrupted_test_file, indent=2) #corrpting the json file, by taking only part of the dictionary.
                    
                    
    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree(test_files_path)
        except:
            pass  
    
    def test_read_config_file(self):
        
        with self.assertRaises(Exception):
            ProjectConfig("random_text")
            
        with self.assertRaises(Exception):
            ProjectConfig(corrupted_test_config_file_with_path)
            
        project_config = ProjectConfig(test_config_file_with_path)    

        self.assertEqual(project_config.get_project_name(), project_test_configuration["project_name"])
        self.assertEqual(project_config.get_sources_root_directory(), project_test_configuration["sources_root_directory"])
        self.assertEqual(project_config.get_output_directory(), project_test_configuration["output_directory"])
    
    def test_compile(self):
        pass

        
        