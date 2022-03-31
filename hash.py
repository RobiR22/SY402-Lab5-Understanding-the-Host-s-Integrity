#Robinson
#sy402 lab5

#help links
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

#imports
import os

def counter(file):
    count = 0
    for char in file:
        count = count + 1
    return(count)
  
def fileFilter():
    dot = "."
    count = counter(file)
    if count >= 3:
        if file[-2] == dot:
          #hashFile
    if count >= 4:
        if file[-3] == dot:
            #hashFile
    if count >= 5:
        if file[-4]== dot:
            #hashFile
    if count >= 6:
        if file[-5] == dot:
            #hashFile....................................................................................
    
    return(fileFilter())  
  

#function to go thru directory for files and other directories. Print directory send files to foundFile()
function thruDirectory(strDirectory):
  print(strDirectory)
  directory = os.fsencode(strDirectory)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if "." in filename: 
      foundFile(filename)
    else:
      thruDirectory(filename)
  print(done)
  return

#Prints found file
function foundFile(filename):
  print(filename)
  return
