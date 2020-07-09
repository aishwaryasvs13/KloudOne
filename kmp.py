#Knuth-Morris-Pratt Algorithm
#Aishwarya-SVS

def KMPSearch(pattern, text):
    M = len(pattern) #lenght of pattern
    N = len(text)   #lenght of text

    lps = [0] * M #Create list with fixed length to store list of prefixes
    j = 0

    computeLPSArray(pattern, M, lps) #Calling function to get matching sub-string

    i = 0
    while i < N:
        if pattern[j] == text[i]:  #a character match
            i += 1
            j += 1

        if j == M:
            print ("Found pattern at index " + str(i - j)) #a complete match

            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:

            if j != 0:  #no match but we have advanced in pattern
                j = lps[j - 1]
            else:
                i += 1  #no match and have NOT advanced in pattern

def computeLPSArray(pattern, M, lps):
    len = 0
    i = 1

    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

text = input("Enter the text string: ") #Text String
pattern = input("Enter the pattern to be found: ")    #Pattern String

KMPSearch(pattern, text)
