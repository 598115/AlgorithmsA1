#Author: Trym Haugan Berger
### BOYER-MOORE TEXT PATTERN SEARCHING ALGORITHM ###

#Get text and pattern

from filereader import read_text_from_file
P = "acies"                                      #Pattern. found at line 117 of text.txt
T = read_text_from_file("problem2&3/text.txt")   #Text

#Search text function
def BM_search(T, P):
    #Initialize variables

    m = len(P)  #Pattern length
    n = len(T)  #Text length
    i = m - 1   #Text iterator var
    j = m - 1   #Pattern iterator var
    compCounter = 0

    #Compute table

    lastTable = {}

    for a in range(m):
        lastTable[P[a]] = a

    while i <= n - 1:                      
        while j >= 0 and P[j] == T[i]:
            compCounter += 1 #Match counted
            j -= 1
            i -= 1
        if j < 0:
            print(f"BM Found match at text index: {i + 1}")
            print(f"Comparison ratio was: {compCounter/n}")
            return i + 1
        else:
            compCounter += 1 #Mismatch counted
            i = i + m - min(j, 1 + lastTable.get(T[i], -1))
            j = m - 1     
          
    print("Found no match in text")

BM_search(T, P)
