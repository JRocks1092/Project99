import os
import shutil
import time

days = int(input("No of days old to delete : "))
days_seconds = time.time()-days * 24 * 60 * 60
path = input("Enter Path : ")
path = path.replace("/", "\\")

if os.path.exists(path):
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
                filePath = os.path.join(root, name)		                
                if os.stat(filePath).st_ctime > days_seconds:
                    c = filePath.split('\\')
                    print("removing file "+c[len(c)-1]+".....")
                    os.remove(filePath)
        for name in directories:
                filePath = os.path.join(root, name)
                if os.stat(filePath).st_ctime > days_seconds:
                    c = filePath.split('\\')
                    print("removing folder "+c[len(c)-1]+".....")
                    shutil.rmtree(filePath)
else:
    print("No Folder with such name....")