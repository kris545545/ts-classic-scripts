import os
import shutil
from datetime import datetime

# Variables
gameRoot = "D:\SteamLibrary\steamapps\common\RailWorks"
scriptDir = os.path.join(gameRoot, "0Scripts\\")
backupDir = os.path.join(scriptDir,"backup")
profilesFile = os.path.join(gameRoot, "Content\PlayerProfiles.bin")
serzCmd = os.path.join(gameRoot, "serz.exe")

# First run method to determine if the backup directory exists. If it doesn't, the script will create it.
def firstRun():
    if not backupDir:
        print("Backup directory not found. Creating at " + backupDir)
        os.mkdir(backupDir)
    print("Backup directory found at " + backupDir)
    extractContents()
    
def extractContents():
    # Sets the timestamp to the current local computer time formatted as 2023-08-07-21_40_16
    timestamp = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    print(timestamp)
    # Backs up the PlayerProfiles.bin-file in case shit hits the fan
    destFile = os.path.join(backupDir,"PlayerProfiles-" + timestamp + ".xml")
    shutil.copy(profilesFile, destFile)
    # Extracts the .bin-file to an XML file which can be edited
    os.system(serzCmd + " " + profilesFile + " /xml:" + scriptDir + "out.xml")

firstRun()
