import time

print("=========================")
print("== begin py-fileparser ==")

# prompt user for file path
pathToCopy = input("Enter your file path: ")

if pathToCopy == '':
  raise Exception("No file path provided, aborting")

lowerCaseInput = input("Convert result to lowercase? 'y' or 'n': ")
lowercaseToggled = lowerCaseInput == 'y'

# generate new file path
dt = int(time.time())
dtString = str(dt)
pathToModify = './created_files/' + dtString + '.txt'

# open & read file, set to readResult
fileToCopy = open(pathToCopy, "r")
readResult = fileToCopy.read()

# prompt user for replace details
print("Enter Below: Text to replace, separated by commas (case-sensitive): ")
replaceOld = input()
replaceOldArr = replaceOld.split(',')

print("Enter Below: Text to replace with, also separated with corresp. commas. (Exp. " + str(len(replaceOldArr)) + " params) (case-sensitive):  ")
replaceNew = input()
replaceNewArr = replaceNew.split(',')

# handle each replacement
for index, replaceItem in enumerate(replaceNewArr): 
  # replaceOldArr[index] = replaceItem.lower()
  readResult = readResult.replace(replaceOldArr[index], replaceNewArr[index]) 

# set result to lowercase if toggled by user previously
if lowercaseToggled:
  readResult = readResult.lower() # lower case

# create new file at destination path
fileToModify = open(pathToModify, "w")
fileToModify.write(readResult)

print("== File Created at: " + pathToModify)
print("== end py-fileparser ==")
print("=======================")