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



def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Score(Motifs):
    Score=0
    consensus=Consensus(Motifs)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            if Motifs[i][j] != consensus[j]:
                Score+=1
    return Score    


def Pr(Text, Profile):
    p=1
    for i in range(len(Text)):
        p=p*Profile[Text[i]][i]
    return p    



def ProfileMostProbablePattern(Text, k, Profile):
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
