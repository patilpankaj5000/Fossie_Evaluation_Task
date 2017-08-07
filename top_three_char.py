# Function which accepts a string 'S' as an argument containing only lowercase English letters and 
# returns top 3 most common characters in string as a list.

# Creator: Pankaj Patil

# Input : 'aaaaabbbccccdddef'
# Output: ['a','c','b','d']
# In above example, given string has top 3 most common characters as
# a with frequency 5 
# c with frequency 4
# d with frequency 3

def top_three_char(S):
    if S.islower():
        letterdict={}               
        for letter in S:
            letterdict[letter] = 0
        for letter in S:
            letterdict[letter] += 1
        sorted_occurence=[]
        tmp=[]
        for i in letterdict:         
            tmp.append([letterdict[i],i])
        sorted_occurence=sorted(tmp,reverse=True)
        #print(sorted_occurence)
        final=[]
        for i in range(3):
            final.append(sorted_occurence[i][1])
        return final
    else:
        print("string should be in lower case")

