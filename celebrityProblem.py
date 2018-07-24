# The Celebrity Problem
# In a party of N people, only one person is known to everyone. Such a person
# may be present in the party, if yes, (s)he does not know anyone in the party.
# We can only ask questions like 'does A know B? '. Find the stranger (celebrity)
# in minimum number of questions.

from Stack import NewStack

matrix = [[0,0,1,0],
                [0,0,1,0],
                [0,0,0,0],
                [0,0,1,0]]

def isknow():
    for i in range(4):
        for j in range(4):
            if matrix[i]!=matrix[j]:
                print(i,j)

def celebrityfind():
    pass

print(isknow())

