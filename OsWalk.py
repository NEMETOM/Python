import os
cfiles = []
for root, dirs, files in os.walk(str(input("Define directory: "))):
    print(files)
