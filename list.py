import os
folders = input("enter the folder name with space").split()
try:
   for folder in folders:
     files = os.listdir(folder)
     for file in files:
       print(file)

except FileNotFoundError :
 print("file not found")
except PermissionError:
  print("permission error")

    

