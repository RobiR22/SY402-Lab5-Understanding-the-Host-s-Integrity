#Robinson
#sy402 lab5

#help links
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
#https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

#imports
import os
import hashlib
from datetime import datetime

fileDict = {"files":[], "fileHashes":[]}

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
histDict = {"Last Update": [], "directories":[]}
histDict["Last Update"].append(dt_string)

count = 0

def summary():
    count = 0
    fileHash = ""
    history = ""
    for x in fileDict["files"]:
        fileHash = fileHash + str(fileDict["files"][count]) + " " + str(fileDict["fileHashes"][count]) + "\n"
        count = count + 1
    for x in histDict["directories"]:
        history = history + str(histDict["Last Update"]) + " " + str(x) + "\n"
    print("Summary of program.\n" +
    "Files and their hashes:\n" +
    fileHash +
    "History: \n" +
    history)
    return()

def hashedDict(file, md5, sha1):
    fileDict["files"].append(file)
    fileDict["fileHashes"].append([md5, sha1])
    print(fileDict)

def counter(file):
    count = 0
    for char in file:
        count = count + 1
    return(count)
  
def fileFilter(file):
    dot = "."
    strFile = str(file)
    count = counter(strFile)
    if count >= 3:
        if strFile[-2] == dot:
            theHasher(file)
        elif strFile[-3] == dot:
            theHasher(file)
        elif strFile[-4]== dot:
            theHasher(file)
        elif strFile[-5] == dot:
            theHasher(file)
        else: print("error")
    return()

def theHasher(file):
    #encodeFile = file.encode()
    openedFile = open(file)
    readFile = openedFile.read()
    
    #md5Hash = hashlib.md5(encodeFile)
    #md5Hashed = md5Hash.hexdigest()

    #sha1Hash = hashlib.sha1(encodeFile)
    #sha1Hashed = sha1Hash.hexdigest()

    md5Hash = hashlib.md5(readFile)
    md5Hashed = md5Hash.hexdigest()

    sha1Hash = hashlib.sha1(readFile)
    sha1Hashed = sha1Hash.hexdigest()
    
    opendedFile.close()

    #print("File Name: %s" %file)
    #print("MD5: %r" %md5Hashed)
    #print("SHA1: %r" %sha1Hashed)
    
    #print(file + " hashed is: %s" %md5Hashed)
    hashedDict(file, md5Hashed, sha1Hashed)
    return()  

#function to go thru directory for files and other directories. Print directory send files to foundFile()
def thruDirectory(strDirectory):
  blackList = ["dev", "proc", "run", "sys", "tmp", "lib"]
  directory = os.fsencode(strDirectory)
  histDict["directories"].append(directory)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if str(filename) in blackList:
        pass
    elif "." in filename: 
      fileFilter(filename)
    else:
      thruDirectory(filename)
  summary()

def prompter():
    file = str(input("enter file or directory: "))
    thruDirectory(file)
    
prompter()

