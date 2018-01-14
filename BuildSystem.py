import os
import lib.FindFiles as Files
import lib.CheckSum as CheckSum

listFoundFiles = Files.Find([ "..\\..\\" ], [ ".py" ])
print(listFoundFiles)


listFoundFiles = Files.Exclude(listFoundFiles, [ "lib" ])
print(listFoundFiles)


listFoundFiles = CheckSum.GetChangedFiles("..\\..\\jsonFiles\\file.json", listFoundFiles)
print(listFoundFiles)

CheckSum.UpdateJSONFile("..\\..\\jsonFiles\\file.json", CheckSum.CalculateFilesMD5(listFoundFiles))
    