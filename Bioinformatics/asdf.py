# Insert your Pr(Text, Profile) function here from Motifs.py.
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count=Count(Motifs)
    for symbol in 'ATGC':
        profile[symbol]=[]
        for i in range(k):
            profile[symbol].append(count[symbol][i]/t)
    return profile

def Pr(Kmer, Profile):
    p=1
    for i in range(k):
        p=p*Profile[Kmer[i]][i]
    return p  
# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    m=0
    Pattern=''
    for i in range(len(Text)-k+1):
        Kmer=''
        for j in range(i,i+k):
            Kmer+=(Text[j])
        pr=Pr(Kmer,Profile)
        if pr > m:
            m=pr
            Pattern=Kmer
    return Pattern        
        

Text='TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA'
k=5

A=[0.2 ,0.2, 0.3 ,0.2 ,0.3]
C=[0.4 ,0.3 ,0.1 ,0.5 ,0.1]
G=[0.3 ,0.3 ,0.5 ,0.2 ,0.4]
T=[0.1 ,0.2 ,0.1 ,0.1 ,0.2]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
x=ProfileMostProbablePattern(Text, k, Profile)
print(x)
