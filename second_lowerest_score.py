# Function accepts nested list as input which contains name of student & his or her score.
# Function returns name(s) of students having second lowest score as a list
# Creator: Pankaj Patil
# Input : [['Harish',37.21],['Shakti',37.21],['Tina',37.20],['Mayur',40.1],['Jayesh',39]]
# Output: ['Harish','Shakti']

def second_lowest_grade(score):
    only_score=[]
    final=[]
    for i in range(len(score)):
        only_score.append(score[i][1])
    only_score.sort()
    #print(only_score)
    second_lowest_score=only_score[1]
    #print(second_lowest_score)
    for i in range(len(score)):
        if second_lowest_score==score[i][1]:
            final.append(score[i][0])
    return final
