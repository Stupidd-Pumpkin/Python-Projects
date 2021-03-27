#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

