
from filereader import read_text_from_file

X = read_text_from_file("problem9/stringX.txt") 
Y = read_text_from_file("problem9/stringY.txt") 

def LCS_dynamic(X, Y):

    m = len(X)
    n = len(Y)

    table = [[0] * (n+1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                #Match
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                #No match
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    # The length of LCS is in the bottom-right cell
    return table[m][n]

print("Dynamic: Longest common substring has length: ", LCS_dynamic(X, Y))