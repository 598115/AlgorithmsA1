
### KNUTH-MORRIS-PRATT TEXT PATTERN SEARCHING ALGORITHM ###

from filereader import read_text_from_file

P = "acies"
T = read_text_from_file("problem2&3/text.txt")


def kmp_search_first(text, pattern):
    ##############Compute table################
    compCounter = 0
    length = 0  
    lps = [0] * len(pattern)  
    i = 1  

    while i < len(pattern):
        compCounter += 1
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
 
                i += 1
    ########################################
    i = 0  # Index for text
    j = 0  # Index for pattern
    n = len(text)

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            compCounter += 1

        if j == len(pattern):
            # Pattern found, return the starting index
            print(f"KMP Found match at text index: {i - j}")
            print(f"Comparison ratio was: {compCounter/n}")
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    # Pattern not found
    print("Found no match in text")
    return

kmp_search_first(T, P)