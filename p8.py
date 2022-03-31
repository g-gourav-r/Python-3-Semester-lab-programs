# count the number of files, subdirectories and folders in the specified path
import os

path =os.walk(" ") # add the path here
tf=0
td=0
for root,sd,files in path:
  print("Root",root)
  print("Subdirectories",sd)
  print("Files",files)
  tf+=len(files)
  td+=len(sd)
print("Total files : ",tf)
print("Total subdirectories : ", td)

#Read lines from one file and print the odd lines in new file

old=open("old.txt")
data=old.read()
lines=data.split('\n')
oddlines=""
for index in range(0,len(lines),2):
  oddlines+=lines[index]+"\n"
  new=open("new.txt",'w')
  new.write(oddlines)
  new.close()
  old.close()
print("Operation complete")