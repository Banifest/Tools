import os
import zipfile
import zlib
from typing import AnyStr
 
fileDir = r'E:\work\WS2DB'
 
directoryFiles: list[str] = os.listdir(fileDir)
concatenatedJSONs: str = ''

for fileName in directoryFiles:
    fullSingleJSONFilePath: str = fileDir + os.sep + fileName
    
    singleFileContent: str = ''.join(open(fullSingleJSONFilePath, 'r', encoding='UTF-8').readlines())[1:-1]

    if concatenatedJSONs == '': 
        concatenatedJSONs = '[' + singleFileContent
    else:
        concatenatedJSONs += ',' + singleFileContent    
concatenatedJSONs += ']'

saveFilePath: str = 'E:' + os.sep + 'Concatenated.zip'
zipper: zipfile.ZipFile = zipfile.ZipFile(saveFilePath, 'w', zipfile.ZIP_DEFLATED, False, 4)
zipper.writestr('concatenated.json', concatenatedJSONs)
zipper.close()

print('finished!')