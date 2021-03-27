#!/usr/bin/env python
# coding: utf-8

# In[79]:


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
                        #print(labels[a1][a2][a3][a4][a5], end = ' ')                          

#np.save("Phi",phi)
#np.save("Psi",psi)
#np.save("Count",count)
#np.save("Train_data",data)
#np.save("Train_labels",labels)

print("Training done")

            


# In[99]:


n_files = 0

path = 'Test/'
test_files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.pdb' in file:
            test_files.append(os.path.join(r, file))

for f in test_files :
    pdb_code = f[5:len(f)-4]
    with open("Test_csv/%s.csv" % pdb_code) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\t')
        test_data = []
        for row in csv_reader:
            test_data.append(row)
            
    test_labels = np.chararray(len(test_data))
    f1 = 'Test_results/'+pdb_code +'.txt'
    file=open(f1,"w+")
    q='XX'

    for i in range(2, len(test_data)-2):
        test_phi = phi[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])]
        test_psi = psi[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])]
        test_labels[i] = labels[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])]
        #print(count[initials.index(test_data[i-2][0])][initials.index(test_data[i-1][0])][initials.index(test_data[i][0])][initials.index(test_data[i+1][0])][initials.index(test_data[i+2][0])], end = ' ')
        b = str(test_labels[i])
        if len(b)<3 : b='XXX'
        #print(test_labels[i])
        q=q+b[2]
    q=q+'XX'
    file.write("%s" % (q))
    file.close()
    #np.save("Test_results/%s" % pdb_code, test_labels)


    #print(n_files)
    n_files = n_files + 1

print("Testing done")



path=os.listdir('Test_results/')
#print (path)
alphabet = ["H", "S", "E", "X"]
conf = np.zeros((4,4))
for f1 in path :
    if '.txt' in f1:
        file1=open('Test_results/'+f1,'r')
        file2=open('DSSP_Struct/'+f1,'r')
        q1=file1.readline()
        q2=file2.readline()
        #print(len(q1)-len(q2), f1)
        if len(q1)- len(q2)==0 :
            for i in range(len(q1)):
                conf[alphabet.index(q1[i])][alphabet.index(q2[i])] = conf[alphabet.index(q1[i])][alphabet.index(q2[i])] + 1
    
print (conf)
total = 0
diag = 0
for i in range(4):
    for j in range(4):
        total = total + conf[i][j]
    diag = diag + conf[i][i]

acc = diag/total
print(acc) 

