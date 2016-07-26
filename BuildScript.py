print("Starting Build")

import os
import re
import shutil
import zipfile

version = "1.0.0"

##comple list of files to not include
regexList = [".*\.lua", ".*\.json", "README.md", "LICENSE"]
zipFolder = "StartingSpotsPlus_" + version

if os.path.exists(zipFolder):
    shutil.rmtree(zipFolder)
os.mkdir(zipFolder)

for i in os.listdir(os.getcwd()):
    
    addFile = False
    for j in regexList:      
        match = re.search(j,i)
        if match:  
            addFile = True
    if addFile:
        shutil.copyfile(i,zipFolder + "\\" + i)
        print("Include: " + i)  
    else:
        print("Exclude: " + i)

zipf = zipfile.ZipFile(zipFolder + ".zip", 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(zipFolder):
    for file in files:
        zipf.write(os.path.join(root, file))
zipf.close()

shutil.rmtree(zipFolder)