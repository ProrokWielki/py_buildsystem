"""
process
    -get list of headers                       --files finde
    -get list of sources                       --files finde
    -get list of object files                  --files finde
    
    -get old MD5 of header files               --file read
    -get old MD5 of source files               --file read
       
    -calculate MD5 of header files             --list2dict
    -calculate MD5 of source files             --list2dict
    
    -get list of changed headers               --dict_diff
    -get list of changed sources               --dict_diff
        
    -get dependencies                          --file read   
    -get dependencies based on changed sources --list2dict
    -update dependecies                        --dict combine
    
    -get list of files needed to be recompiled due to change of headers --dict_diff
    -get list of uncompiled files                                       --list_diff
    
    -combine lists  -- list combiner
    
"""

"""
pre_compilation
    get all headers
    get changed headers

step

"""

"""
    Find Files 
    
"""

import argparse

import Compiler.Compiler as Compiler

parser = argparse.ArgumentParser(description='Python based build system.')

parser.add_argument('compiler_config', metavar='CC', type=str, nargs=1,
                    help='Compiler configuration file')

args = parser.parse_args()


print(args.compiler_config[0])

compiler = Compiler.Compiler(args.compiler_config[0])

print(compiler.get_compiler_path())




    
