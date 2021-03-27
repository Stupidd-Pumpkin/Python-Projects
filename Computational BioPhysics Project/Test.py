#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import os
import numpy as np

proteins  = ["GLY","ALA","LEU","MET","PHE","TRP","LYS","GLN","GLU","SER","PRO","VAL","ILE","CYS","TYR","HIS","ARG","ASN","ASP","THR"]
initials = ["G","A","L","M","F","W","K","Q","E","S","P","V","I","C","Y","H","R","N","D","T"]

n_files = 0
phi = np.load("Phi.npy",)
psi = np.load("Psi.npy")
count = np.load("Count.npy")
data = np.load("Train_data.npy")
labels = np.load("Train_labels.npy",encoding = 'bytes')

types = ["H","S","E"]
path = 'Test/'

count0 = 0

pdb_code = input ('Enter the Protein name: ')
with open("Test_csv/%s.csv" % pdb_code) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    test_data = []
    for row in csv_reader:
        test_data.append(row)


f1 = 'Test_results/'+pdb_code +'.txt'
file=open(f1,"w+")
q='XX'

for i in range(2, len(test_data)-2):
    test_phi = phi[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])]
    test_psi = psi[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])]
    ch = str(labels[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])])
    #print(ch, end=' ')
    if (ch!= 'b\'\''):
        test_label = ch[2]
    countType = np.zeros((3))
    countX = 0
    if (count[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])] == 0):
        for j in range(20):
            for k in range(20):
                ch = str(labels[j][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][k])
                if (ch != 'b\'\''):
                    countType[types.index(ch[2])] = countType[types.index(ch[2])] + 1

        if (np.max(countType) != 0):
            test_label = types[np.argmax(countType)]
        else :
            for j in range(20):
                for k in range(20):
                    for l in range(20):
                        for m in range(20):
                            ch = str(labels[j][k][initials.index(test_data[i][0])][l][m])
                            if (ch != 'b\'\''):
                                countType[types.index(ch[2])] = countType[types.index(ch[2])] + 1

        if (np.max(countType)!= 0):
            test_label = types[np.argmax(countType)]
        else :
            test_label = "X"

    q = q+test_label

    #print(test_label, end = '')
q=q+'XX'
file.write("%s" % (q))
file.close()    
#print(n_files)
n_files = n_files + 1

print("Testing done")
#print(count0)


# In[ ]:




