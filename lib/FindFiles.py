import os

def Find(listSearchedDirectories, listFileTypes):

    assert len(listSearchedDirectories) > 0, "There should be some directoris to search."
    assert isinstance(listSearchedDirectories, list), "Directories should be in a list." 
    
    assert len(listFileTypes) > 0, "There should be some file types in the list."
    assert isinstance(listFileTypes, list), "File types should be in a list." 
    
    listFoundFiles = []
    
    
    for directory in listSearchedDirectories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                for type in listFileTypes:
                    if file.endswith(type):
                        listFoundFiles.append(os.path.join(root,file))

    return listFoundFiles

def Exclude(listFiles, listExcludedDirectories):
    
    assert isinstance(listFiles, list), "Directories should be in a list." 
    
    assert len(listExcludedDirectories) > 0, "There should be some directories to exclude."
    assert isinstance(listExcludedDirectories, list), "Directories should be in a list." 
    
    tmpListFiles = listFiles[:]
    
    for excludedDirectory in listExcludedDirectories:
        for file in listFiles:
            if excludedDirectory in file:
                tmpListFiles.remove(file)
                
    return tmpListFiles
                