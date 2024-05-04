import gzip
import shutil

def pdbgetter(pdbName):
    #rootdir = '/DataBank/pdb'
    rootdir = 'E:/payannameh'
    DIR=f"{rootdir}/{pdbName[4:6]}/{pdbName}.gz"
    print(DIR)
    outputPDB=f"./{pdbName}"
    with gzip.open(DIR, 'rb') as f_in:
        with open(outputPDB, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    return outputPDB


InputProteinFileNameList=open('proteinNameTest.txt','r')
proteinFileNameList=InputProteinFileNameList.readlines()
whereIsTheCrash=open('whereIsTheCrash.txt',"w")

def pdbNamelist(pdbFileNameList):
    for line in pdbFileNameList:
        b=f'{line.strip()}\n'
        whereIsTheCrash.write(b)
        c=f"pdb{line.strip()}.ent"
        pdbgetter(c)
        
    whereIsTheCrash.close()


pdbNamelist(proteinFileNameList)

