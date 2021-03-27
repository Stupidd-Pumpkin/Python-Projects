
#file_name="dict.txt"
#file_list=[]
#fin = open(file_name)
#for eachline in fin:
#	file_list.append(eachline.strip())
#
#print file_list

#file_set=set(file_list)
import string
#from difflib import *
f=open('dict.txt','r')
open('lists.txt','w').close()
q=open('lists.txt','a')
open('back.txt','w').close()
z=open('back.txt','a')
word_set = set(word.strip().upper() for word in f)
start_word="NOSE"
end_word="CHIN"
maxsize=10
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
        print (i,'\n\n\n\n',parentlist[i],'\n',file=q)
        if(end_word in parentlist[i]) and (count ==0 ):
                count=i
print (count)
count+=1
backtrack=[]
backtrack.append([end_word])
print ('\n',backtrack[0])
count+=1
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
        print('\n',backtrack[i])
        print (i,'\n\n\n\n',backtrack[i],'\n',file=z)
