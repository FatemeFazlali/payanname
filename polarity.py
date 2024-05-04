from Bio.PDB import PDBParser
import tarfile
import zipfile
import csv
import os
import numpy as np
import pandas as pd 
#hydrophobic==O
#hydrophilic==I
#neutral==N
#SEA > 3 ,	SEA < 10 , 30 > SEA > 10 
AbbreviationsPolarityHydropathyDictionary={
    "A":["ALA","NP","O",[0.48,0.35,0.17]],
    "R":["ARG","P","I",[0.84,0.05,0.11]],
    "N":["ASN","P","I",[0.82,0.10,0.08]],
    "D":["ASP","P","I",[0.81,0.09,0.10]],
    "C":["CYS","P","O",[0.32,0.54,0.14]],
    "G":["GLY","NP","N",[0.51,0.36,0.13]],
    "Q":["GLN","P","I",[0.81,0.10,0.09]],
    "E":["GLU","P","I",[0.93,0.04,0.03]],
    "H":["HIS","P","N",[0.66,0.19,0.15]],
    "I":["LLE","NP","O",[0.39,0.47,0.14]],
    "L":["LEU","NP","O",[0.41,0.49,0.10]],
    "K":["LYS","P","I",[0.93,0.02,0.05]],
    "M":["MET","NP","O",[0.44,0.20,0.36]],
    "F":["PHE","NP","O",[0.42,0.42,0.16]],
    "P":["PRO","NP","N",[0.78,0.13,0.09]],
    "S":["SER","P","N",[0.70,0.20,0.10]],
    "T":["THR","P","N",[0.71,0.16,0.13]],
    "W":["TRP","NP","O",[0.49,0.44,0.07]],
    "Y":["TYR","P","N",[0.67,0.20,0.13]],
    "V":["VAL","NP","O",[0.40,0.50,0.10]],
}
print(AbbreviationsPolarityHydropathyDictionary)






'''
entry_pdb_file='pdb3gdq.ent.gz'
output_dssp_file=f"{entry_pdb_file}.dssp"
cmd = f"./dssp {entry_pdb_file} {output_dssp_file}"
os.system(cmd)

'''


DSSPfile =open("E:/payannameh/1.dssp","r")
OutputCsvFile=open("E:/payannameh/output.csv","w")
writer=csv.writer(OutputCsvFile)
countline = 0
flag=0
CsvRows=[]
CsvFileName="OutputCsvFile.csv"
writer=csv.writer(OutputCsvFile)
x=[]
y=[]
z=0
i=0

TempMatrix=np.matrix(['fileName','NumberOfAminoAcid','AminoAcidseq','polarity','secondStructure','surfacelocation','x','y','z'],[])


line_count = 0
for line in DSSPfile:           
        line_count += 1
        if  "#" in line :
            flag=1
            print(line)   
        if "#" not in line and flag==1:
            if line[16]==" ":
                print("C")
                x.append("C")
                y=AbbreviationsPolarityHydropathyDictionary.get("C")
            else:
                print(line[16])
                x.append(line[16])
                y=AbbreviationsPolarityHydropathyDictionary.get(line[16])
                
print(y)
start=0
end=3


'''
for i in range(3,31,1):
    data = [x[0:i] for l in range(0, len(x), 1)]   
    print(data)
 '''                   
OutputCsvFile.close()
DSSPfile.close()

def DistanceBetween2End(start,end):
    xdistanceStart=start[118:123]
    ydistanceStart=start[126:130]
    zdistanceStart=start[133:137]
    xdistanceEnd=end[118:123]
    ydistanceEnd=end[126:130]
    zdistanceEnd=end[133:137]
    xdistance=float(xdistanceStart)-float(xdistanceEnd)
    ydistance=float(ydistanceStart)-float(ydistanceEnd)
    zdistance=float(zdistanceStart)-float(zdistanceEnd)

    return xdistance,ydistance,zdistance


A="    1  132 R Q              0   0  200      0, 0.0    81,-0.7     0, 0.0     2,-0.3   0.000 360.0 360.0 360.0 101.6   53.4    13.9    14.0"
B="    1  132 R Q              0   0  200      0, 0.0    81,-0.7     0, 0.0     2,-0.3   0.000 360.0 360.0 360.0 101.6   33.4    3.9    2.0"
x,y,z=DistanceBetween2End(A,B)

CsvFieldsName=['fileName','NumberOfAminoAcid','Residue','AA','structure','BP1','bp2','ACC','N-H--O','O--H-N','N-H--O','O--H-N','TCO','KAPPA','ALPHA','PHI','PSI','X-CA','Y-CA','Z-CA']

TempMatrix=np.matrix(['fileName','NumberOfAminoAcid','AminoAcidseq','polarity','secondStructure','surfacelocation','x','y','z'],[])
print(TempMatrix)

import ctypes

'''
class DynamicArray(object):
	'''
	DYNAMIC ARRAY CLASS (Similar to Python List)
	'''
	
	def __init__(self):
		self.n = 0 # Count actual elements (Default is 0)
		self.capacity = 1 # Default Capacity
		self.A = self.make_array(self.capacity)
		
	def __len__(self):
		"""
		Return number of elements sorted in array
		"""
		return self.n
	
	def __getitem__(self, k):
		"""
		Return element at index k
		"""
		if not 0 <= k <self.n:
			# Check it k index is in bounds of array
			return IndexError('K is out of bounds !')
		
		return self.A[k] # Retrieve from the array at index k
		
	def append(self, ele):
		"""
		Add element to end of the array
		"""
		if self.n == self.capacity:
			# Double capacity if not enough room
			self._resize(2 * self.capacity)
		
		self.A[self.n] = ele # Set self.n index to element
		self.n += 1

	def insertAt(self,item,index):
		"""
		This function inserts the item at any specified index.
		"""

		
		if index<0 or index>self.n:
			print("please enter appropriate index..")
			return
		
		if self.n==self.capacity:
			self._resize(2*self.capacity)
			
		
		for i in range(self.n-1,index-1,-1):
			self.A[i+1]=self.A[i]
			
		
		self.A[index]=item
		self.n+=1


		
	def delete(self):
		"""
		This function deletes item from the end of array
		"""

		if self.n==0:
			print("Array is empty deletion not Possible")
			return
		
		self.A[self.n-1]=0
		self.n-=1
		
		
		
	
	def removeAt(self,index):
		"""
		This function deletes item from a specified index..
		"""		

		if self.n==0:
			print("Array is empty deletion not Possible")
			return
				
		if index<0 or index>=self.n:
			return IndexError("Index out of bound....deletion not possible")		
		
		if index==self.n-1:
			self.A[index]=0
			self.n-=1
			return		
		
		for i in range(index,self.n-1):
			self.A[i]=self.A[i+1]			
			
		
		self.A[self.n-1]=0
		self.n-=1

		
	def _resize(self, new_cap):
		"""
		Resize internal array to capacity new_cap
		"""
		
		B = self.make_array(new_cap) # New bigger array
		
		for k in range(self.n): # Reference all existing values
			B[k] = self.A[k]
			
		self.A = B # Call A the new bigger array
		self.capacity = new_cap # Reset the capacity
		
	def make_array(self, new_cap):
		"""
		Returns a new array with new_cap capacity
		"""
		return (new_cap * ctypes.py_object)()

   # Instantiate
arr = DynamicArray()
# Append new element
arr.append(1)
len(arr)
# Append new element
arr.append(2)
# Check length
len(arr)
print(arr)

"""

parentFileName="E:/payannameh/2.zip"
with zipfile.ZipFile(parentFileName,'r') as parentFile:
        print(parentFile.infolist())
        parentFile.extractall()
        nextZipName=parentFile.namelist()[0]
        while True:
            if zipfile.is_zipfile(nextZipName):
                if zipfile.is_zipfile(nextZipName):
                    with zipfile.ZipFile(nextZipName,"r") as childFile:
                        childFile.extractall()
                        nextZipName=childFile.namelist[0]
                        
                        kiddoFile=tarfile.open(nextZipName)
                        kiddoFile.extract()
                        print("done")
                        kiddoFile.close()          
            else:
                break    
                """

'''