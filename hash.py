#Robinson
#sy402 lab5

#help links
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
#https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

#imports
import os
import hashlib

fileDict = {"files":[], "fileHashes":[]}

def hashedDict(file, md5, sha1):
    fileDict["files"].append([file])
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

    print("File Name: %s" %file)
    print("MD5: %r" %md5Hashed)
    print("SHA1: %r" %sha1Hashed)
    
    print(file + " hashed is: %s" %md5Hashed)
    hashedDict(file, md5Hashed, sha1Hashed)
    return(prompter())  

#function to go thru directory for files and other directories. Print directory send files to foundFile()
def thruDirectory(strDirectory):
  print(strDirectory)
  directory = os.fsencode(strDirectory)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if "." in filename: 
      fileFilter(filename)
    else:
      thruDirectory(filename)
  print(done)
  return

def prompter():
    file = str(input("enter file or directory: "))
    thruDirectory(file)
    
prompter()

