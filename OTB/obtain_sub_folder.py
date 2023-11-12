import os

dirct = 'E:/data/OTB/'
dirList = []
fileList = []
files = os.listdir(dirct)  # 文件夹下所有目录的列表
print('files:', files)
for f in files:
    if os.path.isdir(dirct + '/' + f):  # 这里是绝对路径，该句判断目录是否是文件夹
        dirList.append(f)
    elif os.path.isfile(dirct + '/' + f):  # 这里是绝对路径，该句判断目录是否是文件
        fileList.append(f)
print("文件夹有：", dirList)
print("文件有：", fileList)
