import filecmp
import os
import re
from typing import AnyStr
 
file_dir1 = r'E:\work\old\CONTENT_3'
file_dir2 = r'E:\work\new\newnewCONTENT_3'
 
directoryFiles: list[str] = os.listdir(file_dir1)
compiledChangeRegex = re.compile(r'"M":\[([/|\w|,|\"|\s]*)\]')

for fileName in directoryFiles:
    fullFilePathOld: str = file_dir1 + os.sep + fileName    
    fullFilePathNew: str = file_dir2 + os.sep + fileName    

    fileContentOld = open(fullFilePathOld, 'r', encoding='UTF-8').readlines()
    fileContentNew = open(fullFilePathNew, 'r', encoding='UTF-8').readlines()

    fileContentOld[0] = compiledChangeRegex.sub('"M":[]', fileContentOld[0]) 
    fileContentNew[0] = compiledChangeRegex.sub('"M":[]', fileContentNew[0]) 

    if not os.path.isfile(fullFilePathNew):
        print(fileName)

    if fileContentOld != fileContentNew:
        print(fileName)