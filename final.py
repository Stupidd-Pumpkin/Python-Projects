#file_name="dict.txt"
#file_list=[]
#fin = open(file_name)
#for eachline in fin:
#	file_list.append(eachline.strip())
#
#print file_list

#file_set=set(file_list)
import string
import networkx as nx
#from difflib import *
f=open('dict.txt','r')
open('lists.txt','w').close()
q=open('lists.txt','a')
open('back.txt','w').close()
z=open('back.txt','a')
open('path.txt','w').close()
p=open('path.txt','a')
word_set = set(word.strip().upper() for word in f)
start_word=raw_input("Enter start word  : ")
end_word=raw_input("Enter end word  : ")
#maxsize=int (raw_input("Enter the maxsize  : ") )

#start_word="BUNNY"
#end_word="DIRTY"

maxsize=15
length=len(start_word)
alphabet_list=list(string.ascii_uppercase)
'''
list1=[]
for i in range(0,4):
	for a in alphabet_list:
		temp=list(start_word)
		temp[i]=a
		st="".join(temp)
		if(st in word_set):
			if st != start_word:
				list1.append(st)
print ( list1,'\n',file=q)
print ("\n")
list_set=set(list1)
'''

def compare(string1,string2,l):
	list1=list(string1)
	list2=list(string2)
	flag=0
	for i in range(0,l):
		if (list1[i]!=list2[i]):
			flag+=1
	return flag==1
	

count=0
parentlist=[]
parentlist.append([start_word])
for i in range (1,maxsize):
        parentlist.append([])
        for st1 in parentlist[i-1]:
                for a in alphabet_list:
                        for j in range(0,length):
                                temp=list(st1)
                                temp[j]=a
                                st="".join(temp)
                                if(st in word_set):
                                        if(st not in parentlist[i]):
                                                parentlist[i].append(st)
        #print (i,'\n\n\n\n',parentlist[i],'\n',file=q)
        #print >>q, i 
        #print >>q, '\n'
        #print >>q,  parentlist[i]
        #print >>q, '\n'
        if(end_word in parentlist[i]) and (count ==0 ):
                count=i
                maxsize=count+3
print count
count+=1
'''
backtrack=[]
backtrack.append([end_word])
print '\n'
print backtrack[0]

G=nx.DiGraph()

for i in range (1,count):
        backtrack.append([])
        for st1 in backtrack[i-1]:
                for a in alphabet_list:
                        for j in range(0,length):
                                temp=list(st1)
                                temp[j]=a
                                st="".join(temp)
                                if(st in parentlist[count-i-1]):
                                        if(st not in backtrack[i]) and (st not in backtrack[i-1]):
                                                backtrack[i].append(st)
        print'\n'
        print backtrack[i]
        #print (i,'\n\n\n\n',backtrack[i],'\n',file=z)
'''
G=nx.DiGraph()

for i in range (1,maxsize):
	for st1 in parentlist[i]:
		for st2 in parentlist[i-1]:
			if compare(st1,st2,length):
				G.add_edge(st1,st2)
	
#size=raw_input("Enter the upper limit  :")

no=[]

for i in range(0,5):
	no.append(0)

for path in nx.all_simple_paths(G, source=end_word, target=start_word,cutoff= count+3):
	no[len(path)-count]+=1
	#print >> p, path

print no


 
