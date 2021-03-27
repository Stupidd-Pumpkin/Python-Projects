#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import os
import numpy as np

proteins  = ["GLY","ALA","LEU","MET","PHE","TRP","LYS","GLN","GLU","SER","PRO","VAL","ILE","CYS","TYR","HIS","ARG","ASN","ASP","THR"]
initials = ["G","A","L","M","F","W","K","Q","E","S","P","V","I","C","Y","H","R","N","D","T"]
path = 'Train/'

#file = '1HMP_biopython.csv'
phi = np.zeros((20,20,20,20,20))
psi = np.zeros((20,20,20,20,20))
count = np.zeros((20,20,20,20,20))
labels = np.chararray((20,20,20,20,20))

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.pdb' in file:
            files.append(os.path.join(r, file))

n_files = 0
for f in files :
    pdb_code = f[6:len(f)-4]
    with open("Train_csv/%s.csv" % pdb_code) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\t')
        data = []
        for row in csv_reader:
            data.append(row)

    for i in range(2, len(data)-2):
        phi[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] = phi[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] + float(data[i][1])
        psi[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] = psi[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] + float(data[i][2])
        count[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] = count[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] + 1
        #labels[initials.index(data[i-2][0])][initials.index(data[i-1][0])][initials.index(data[i][0])][initials.index(data[i+1][0])][initials.index(data[i+2][0])] = label
    
    #print("%i" %n_files)
    n_files = n_files+1

for a1 in range(20):
    for a2 in range(20):
        for a3 in range(20):
            for a4 in range(20):
                for a5 in range(20):
                    if (count[a1][a2][a3][a4][a5] != 0):
                        phi[a1][a2][a3][a4][a5] = phi[a1][a2][a3][a4][a5]/count[a1][a2][a3][a4][a5]
                        psi[a1][a2][a3][a4][a5] = psi[a1][a2][a3][a4][a5]/count[a1][a2][a3][a4][a5]
                        #print(phi[a1][a2][a3][a4][a5], phi[a1][a2][a3][a4][a5], end = ' ')
                        if (phi[a1][a2][a3][a4][a5]>-75 and phi[a1][a2][a3][a4][a5]<-45 and psi[a1][a2][a3][a4][a5]>-60 and psi[a1][a2][a3][a4][a5]<-30):
                            labels[a1][a2][a3][a4][a5] = 'H'
                        elif (phi[a1][a2][a3][a4][a5]>-135 and phi[a1][a2][a3][a4][a5]<-105 and psi[a1][a2][a3][a4][a5]>120 and psi[a1][a2][a3][a4][a5]<150):
                            labels[a1][a2][a3][a4][a5] = 'E' 
                        else :
                            labels[a1][a2][a3][a4][a5] = 'S'
                        train_label =str(labels[a1][a2][a3][a4][a5])
                        labels[a1][a2][a3][a4][a5] = train_label[2]
                        #print(labels[a1][a2][a3][a4][a5], end = ' ')                          
#data = np.asarray(data)
np.save("Phi",phi)
np.save("Psi",psi)
np.save("Count",count)
np.save("Train_data",data)
np.save("Train_labels",labels)

print("Training done")

