n=int(input())
A=[]
count=0
for i in range(n):
    A.append(int(input()))
    if A[i]>n/2:
        count=count+1
if count==0:
    print('0')
else :
    print('1')
