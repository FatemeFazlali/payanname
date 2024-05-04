import os
import pandas as pd
import gzip
import shutil
import os
import datetime
import math

start_time = datetime.datetime.now()

whereIsTheCrash=open("whereIsTheCrash2.txt","a")


def AccCalaulatorAndPolarity(AA,ACC):
    if AA=="A" :
        MaxACC=188
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="R":
        MaxACC=312
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="N" :
        MaxACC=258
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="D" :
        MaxACC=234
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"
         
    elif AA=="C" :
        MaxACC=188
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="G" :
        MaxACC=112
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"
        
    elif AA=="Q" :
        MaxACC=293
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="E" :
        MaxACC=233
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="H":
        MaxACC=252
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="I":
        MaxACC=257
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="L" :
        MaxACC=243
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"
        
    elif AA=="K" :
        MaxACC=290
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="M" :
        MaxACC=280
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="F":
        MaxACC=265
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="P" :
        MaxACC=231
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="S":
        MaxACC=193
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="T" :
        MaxACC=217
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

    elif AA=="W" :
        MaxACC=303
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="Y":
        MaxACC=274
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","N"
        elif AccessibleArea>=0.36:
            return "E","N"
        else:
            return "I","N"

    elif AA=="V":
        MaxACC=228
        AccessibleArea=ACC/MaxACC
        if AccessibleArea<=0.18:
            return "B","P"
        elif AccessibleArea>=0.36:
            return "E","P"
        else:
            return "I","P"

def secondStructureToAB(s):
    a =str(line[15:18])
    if 'H' in a:
      return  "A"
    elif 'I' in a:
      return  "A"
    elif 'G' in a:
      return  "A"
    elif 'E' in a:
      return  "B"
    elif 'B' in a:
      return  "B"
    elif 'S' in a:
      return  "L" 
    elif 'T' in a:
      return  "L" 
    elif ' ' in a:
      return  "L" 

def DistanceBetween2End(xstartTemp,ystartTemp,zstartTemp,xEndTemp,yEndTemp,zEndTemp):
    xdistanceStart=xstartTemp
    ydistanceStart=ystartTemp
    zdistanceStart=zstartTemp
    xdistanceEnd=xEndTemp
    ydistanceEnd=yEndTemp
    zdistanceEnd=zEndTemp

    xdistance=float(xdistanceStart)-float(xdistanceEnd)
    ydistance=float(ydistanceStart)-float(ydistanceEnd)
    zdistance=float(zdistanceStart)-float(zdistanceEnd)

    x,y,z=format(xdistance,'.5f'),format(ydistance,'.5f'),format(zdistance,'.5f')
    x2=float(x)*float(x)
    y2=float(y)*float(y)
    z2=float(z)*float(z)
    distance=math.sqrt(x2+y2+z2)
    
    return distance

      
df = pd.DataFrame(columns=['RESIDUE', 'AA','STRUCTURE' ,'BP1','BP2', 'ACC',
'N_H__>O','O__>H-N','N_H__>O','O__>H-N',
'TCO','KAPPA','ALPHA','PHI','PSI','X-CA','Y-CA','Z-CA','polarity','AccessibleArea','structure'])

dfOFDB = pd.DataFrame(columns=['pdb_name','AA_number','AA','S_STRUCTURE' ,
                               'distance','polarity','surface_location'])

  #  RESIDUE AA STRUCTURE BP1 BP2  ACC 
  #  N-H-->O    O-->H-N    N-H-->O    O-->H-N 
  #  TCO  KAPPA ALPHA  PHI   PSI    X-CA   Y-CA   Z-CA  polarity /home/fazlali/

Direc = "C:/Users/pentium/Desktop/"
print(f"Files in the directory: {Direc}")
for x in os.listdir():

    if x.endswith("ent.dssp"):
        print(x)
        whereIsTheCrash.write(f"{x},")
        dsspFileOpen=open(x,"r")
        dsspFile=dsspFileOpen.readlines()
        flag=0
        for line in dsspFile:
            if "#" in line :
                flag=1

            elif "!" in line:
                flag=0
                break

            elif flag == 1 and "#" not in line :
                if line[15:25]==" ":
                    a=str(line[13:16]).replace(" ","")
                    b=float(line[35:39])
                    AccessibleArea,Polarity=AccCalaulatorAndPolarity(a,b)
                    df.loc[len(df.index)] = [line[5:12],line[12:15],"C",line[26:30],line[30:35],line[35:39],line[39:52],
                    line[52:64],line[64:75],line[75:85],line[85:92],line[91:97],line[97:103],line[103:109],line[109:116],
                    line[116:123],line[123:131],line[131:136],Polarity,AccessibleArea,secondStructureToAB(str(line[17:19]))]
            
                else:
                    a=str(line[13:16]).replace(" ","")
                    b=float(line[35:39])
                    AccessibleArea,Polarity=AccCalaulatorAndPolarity(a,b)
                    df.loc[len(df.index)] = [line[5:12],line[12:15],line[15:26],line[26:30],line[30:35],line[35:39],line[39:52],
                    line[52:64],line[64:75],line[75:85],line[85:92],line[91:97],line[97:103],line[103:109],line[109:116],
                    line[116:123],line[123:131],line[131:136],Polarity,AccessibleArea,secondStructureToAB(str(line[17:19]))]
        df.to_csv(f"{x}a.csv",sep=",")
        dsspFileOpen.close()


        for i in range(3,31):            
            for j in range (0,len(df.index)):
             if j+i<=len(df.index):
                pdbName=x.replace('ent.dssp', '')
                pdbName=pdbName.replace("pdb",'')
                pdbName=pdbName.replace(".",'')
                dfOFDB["pdb_name"]=pdbName
                aaTemp=""
                ssTemp=""
                pTemp=""
                surfaceLTemp=""
                for k in range(j,j+i):
                    aaTemp +=df.iloc[k,1]
                    ssTemp +=df.iloc[k,-1]
                    pTemp +=df.iloc[k,-3]
                    surfaceLTemp +=df.iloc[k,-2]
                xstartTemp=df.iloc[j,-6]
                ystartTemp=df.iloc[j,-5]
                zstartTemp=df.iloc[j,-4]
                xEndTemp=df.iloc[i,-6]
                yEndTemp=df.iloc[i,-5]
                zEndTemp=df.iloc[i,-4]
                dictanceTemp=DistanceBetween2End(xstartTemp,ystartTemp,zstartTemp,xEndTemp,yEndTemp,zEndTemp)
                new_row = pd.DataFrame({'pdb_name':pdbName, 'AA_number':i,"AA":aaTemp, 'S_STRUCTURE':ssTemp,
                        'distance':dictanceTemp, 'polarity':pTemp, 'surface_location':surfaceLTemp},
                                                            index =[0])
                       # simply concatenate both dataframes
                dfOFDB = pd.concat([new_row, dfOFDB]).reset_index(drop = True)
                j+=1
             else:break
        
        dfOFDB.to_csv(f"{pdbName}.csv",sep=",")
        df = df.iloc[0:0]
        dfOFDB = dfOFDB.iloc[0:0]
        os.remove(os.path.join(Direc,x))



end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds()
#seconds
print(execution_time)







