import json
import hashlib

def ReadJSONFile(jsonFile):
    
    assert isinstance(jsonFile, str), "File name should be a string"
    
    try:
        with open(jsonFile) as file:
            jsonData = json.load(file)
            return jsonData
    except:
        return False
    
def WriteJSONFile(jsonFile, dictData):
    
    assert isinstance(jsonFile, str), "File name should be a string"
    
    assert isinstance(dictData, dict), "Data should be a dictionary"
    
    with open(jsonFile, 'w') as file:
        json.dump(dictData, file)

def CalculateFilesMD5(listFiles):
    
    assert isinstance(listFiles, list), "Files should be in a list."
    
    dictFilesHashes = {}
    
    for file in listFiles:
        dictFilesHashes[file] = hashlib.md5(open(file, 'rb').read()).hexdigest()
        
    return dictFilesHashes

def UpdateJSONFile(jsonFile, dictFilesHashes):
    
    assert isinstance(jsonFile, str), "File name should be a string"
    
    assert isinstance(dictFilesHashes, dict), "Data should be a dictionary"
    
    
    if ReadJSONFile(jsonFile) == False:
        WriteJSONFile(jsonFile, dictFilesHashes)
    else:
        dictHashesFromFile = ReadJSONFile(jsonFile)
        
        WriteJSONFile(jsonFile, {**dictHashesFromFile, **dictFilesHashes})
        
def GetChangedFiles(jsonFile, listFiles):
    
    assert isinstance(jsonFile, str), "File name should be a string"
    
    assert isinstance(listFiles, list), "Files should be in a list."
    
    tmpListFiles = listFiles[:]
    
    dictHashesFromFile = ReadJSONFile(jsonFile)
    dictHasedFileList = CalculateFilesMD5(listFiles)
    
    
    if dictHashesFromFile == False:
        return listFiles
    else:
        for file in listFiles:
            if file in dictHashesFromFile:
                if dictHasedFileList[file] == dictHashesFromFile[file]:
                    tmpListFiles.remove(file)
    
    return tmpListFiles
    
    
