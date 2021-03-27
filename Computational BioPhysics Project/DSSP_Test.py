#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
path=os.listdir('DSSP/')
#print (path)
for f1 in path :
  if '_DSSP' in f1:
    in_file=open('DSSP/'+f1,'r')
    f2="DSSP_Struct/"+f1[:-5]+'.txt'
    out_file= open(f2,"w+")
    q=in_file.readlines()
    q1=''
    for line in range (28,len(q)) : 
      if q[line][13]=='!': continue 
      if q[line][16]=='B' : k='E'
      elif q[line][16]=='G' : k='H'
      elif q[line][16]=='I' : k='H'
      elif q[line][16]=='T' : k='S'
      elif q[line][16]==' ' : k='X'
      else : k=q[line][16]
      q1=q1+k

    out_file.write("%s" % (q1))
    
    in_file.close()    
    out_file.close() 


# In[ ]:




