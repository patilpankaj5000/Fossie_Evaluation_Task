def top_three_char(S):
    if S.islower():
        letterdict={}
        for letter in S:
            letterdict[letter] = 0
        for letter in S:
            letterdict[letter] += 1
        sorted_occurence=sorted(letterdict.values(),reverse=True)
     top_three=[]
     for i in range(len(sorted_occurence)):
         if sorted_occurence[i] in top_three and len(top_three)<3:
              continue
         elif len(top_three)==3:
             break
         else:
             top_three.append(sorted_occurence[i])
     final=[]
     for i in letterdict:
         if letterdict[i] in top_three:                 
             final.append(i)
         elif len(final)==3:
             break
         else:
             continue
 else:
     print("string should be lower case")
