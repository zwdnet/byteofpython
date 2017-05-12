# -*- coding:utf-8 -*-
import os
import time
import zipfile

source = "E:\\资料\\code\\byteofpython"
target_dir = "E:"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input("Enter a comment -->")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + now + "_" + comment.replace(" ", "_") + ".zip"

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)


def GetFileList(FindPath, FlagStr = []):
    FileList = []
    FileNames = os.listdir(FindPath)
    return FileNames

f = zipfile.ZipFile(target, mode="w")
sourceFileList = GetFileList(source, ['py', 'exe'])
print(sourceFileList)
for file in sourceFileList:
    f.write(file)
f.close()
print("备份完成")
# zip_command = "zip -r {0} {1}".format(target, " ".join(source))
# print("zip command is:")
# print(zip_command)
# print("Running:")
# if os.system(zip_command) == 0:
#     print("Successful backup to ", target)
# else:
#     print("Backup FAILED")
