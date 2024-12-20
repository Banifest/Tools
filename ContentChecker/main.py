import os
import re
import asyncio

from dotenv import load_dotenv
from EnvironmentParameters import EnvironmentParameters



async def searchPattern(
        directory: str, 
        fileName: str,                   
        searchPatterns: list[re.Pattern]
    ) -> None:
    
    fullFilePath: str = directory + os.sep + fileName
    if os.path.isfile(fullFilePath):

        fileContent = ''.join(open(fullFilePath, 'r', encoding='UTF-8').readlines())
        for pattern in searchPatterns:
            positionMatch: re.Match = pattern.search(fileContent)
            if positionMatch:
                print(f"Pattern found in {fileName} in position {positionMatch.start()}")
        #print(f"Processed {fileName}")

async def main():      
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    environmentParameters: EnvironmentParameters = EnvironmentParameters(
        directory=os.getenv("DIRECTORY"),
        patterns2Search=[re.compile(regex) for regex in str(os.getenv("PATTERN2SEARCH")).split('SEPARATOR')]
    )  
    print(environmentParameters.directory)
    directoryFiles: list[str] = os.listdir(environmentParameters.directory)    

    tasks: list = []
    for fileName in directoryFiles:        
        tasks.append(asyncio.create_task(searchPattern(
            directory=environmentParameters.directory,
            fileName=fileName,
            searchPatterns=environmentParameters.patterns2Search
        )))
    
    if tasks:
        await asyncio.wait(tasks)


if __name__ == "__main__":
    
    asyncio.run(main())