def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count


def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def Skew(Genome):
    skew = {0:0} 
    Skew=[]
    Skew.append(0)
    for i in range(1,len(Genome)+1):
        if Genome[i-1] =='C':
            Skew.append(Skew[i-1]-1)
            skew.update({i:Skew[-1]})
        elif Genome[i-1] =='G':
            Skew.append(Skew[i-1]+1)
            skew.update({i:Skew[-1]})
        else :
            Skew.append(Skew[-1])
            skew.update({i:Skew[-1]})
    return skew

def MinimumSkew(Genome):
    positions=[]
    skew=Skew(Genome)
    print(skew)
    for i in range(len(Genome)+1) :
        if skew[i] == min(skew.values()):
            positions.append(i)
    print(positions)
    return positions


def HammingDistance(p, q):
    count=0
    for i in range(len(p)):
        if p[i] != q[i]:
            count=count+1
    return count


def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] 
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)],Pattern) <=d:
            positions.append(i)
    return positions
######################################
def ReverseComplement(Pattern):
    pattern=list(Pattern)
    Comp=pattern
    for i in range(len(Pattern)):
        Comp[i]=Complement(pattern[i])
    comp=''.join(Comp)
    revComp=Reverse(comp)    
    
    return revComp

def Reverse(Pattern):
    listP=list(Pattern)
    listP.reverse()
    x=listP
    rev=''.join(x)
    return rev

def Complement(Nucleotide):
    if Nucleotide =='A':
        comp='T'
    if Nucleotide =='T':
        comp='A'
    if Nucleotide =='G':
        comp='C'
    if Nucleotide =='C':
        comp='G'
   # else:
    #    comp=Nucleotide
    return comp
######################################
