import os
from functools import reduce

fileName=[]
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        fileName.append(d)
        
 
#rootdir = '/DataBank/pdb'
rootdir = 'E:/payannameh'
listdirs(rootdir)
print(fileName)
comma=","
addComma=lambda x,y : x+comma+y
commaSeperatedValueDirList=reduce(addComma,fileName)
dirAddressList=open('dirAddressList.txt',"w")
dirAddressList.write(commaSeperatedValueDirList)
dirAddressList.close()
