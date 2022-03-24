#Robinson
#sy402 lab5

#help links
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

#imports
import os

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
