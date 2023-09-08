import random

smoker = input('Are you a smoker? ').lower(
)  #First get input from  the user asking if he is a smoker or not

#we next made 4 individual variables ATCG which is equal to its RNA Sequences
A = "U"
T = "A"
C = "G"
G = "C"

#Insertation,Deleation,substitution are three variables that are also getting monitored.
insertation = 0
deleation = 0
substitution = 0

DNA_sequence = [
    A, T, C, G
]  #The list called DNA Sequence will be holding the 4 individual DNA Variables holding the RNA Values
DNA_sequence2 = ['A', 'T', 'C', 'G']
list = []
list2 = []
gen = 0  #Gen will be keeping track of the 10 generations
mutation_chance = 0  #This will keep track of the Mutation Chances

mutation = 0  # The mutation variable is going to be monitoring the number of muations that will occur over the 10 Generations
deleation = 0  #Deleation variable keeps track of the total number of mutations that happend

for i in range(
        20
):  #This is going through each element in the list so just make a for loop in the range 20 because there are 20 DNA sequences.
    anything = random.randint(
        0, 3)  #The anything variable is holding the random range chance of the
    list.append(
        DNA_sequence[anything]
    )  #From a random index in the range (0,3) it is appending the random DNA Sequence to variable list 20  times
    list2.append(
        DNA_sequence2[anything]
    )  # we are also doing the same thing again but this time we are appending the DNA Sequence after it gets randomized into list 2.

for i in range(10):  #Make a for loop which is run until the generation is 10

    if smoker == "yes":  # Inside the for loop make a if statement to check if the input is equal to yes
        mutation_chance = 8  #if the input equals yes than the mutation chance will equal 8 since its higher probability of the person getting lung cancer
    else:
        mutation_chance = 2  #else if the input equals no then the mutation chance is equal to a lower variable
    print('DNA Sequence:', list2)  #Print the DNA Sequence
    anything2 = random.randint(1, 10)

    if mutation_chance > anything2:
        anything3 = random.randint(1, 3)

        if anything3 == 1:  #Mutation 1: Deleation
            print()
            anything4 = random.randint(
                0, 19
            )  #This is holding the random chance of each section in one whole mutation
            list.pop(anything4)  #using the random range delete the
            pop = list2.pop(anything4)
            mutation += 1
            deleation += 1
            print('Deletion of', pop, 'at position', anything4)

        elif anything3 == 2:  #Insertation
            print()
            anything4 = random.randint(1, 19)
            anything5 = random.randint(0, 3)
            list.insert(anything4, DNA_sequence[anything5])
            list2.insert(anything4, DNA_sequence2[anything5])
            mutation += 1
            insertation += 1
            print(' Insertion of ', DNA_sequence2[anything5], ' at position ',
                  anything4)

        elif anything3 == 3:  #Substitution
            anything6 = random.randint(1, 9)
            anything7 = random.randint(0, 3)
            list2.pop(anything6)
            list.insert(anything6, DNA_sequence[anything7])
            print('Substituded ' + list2[anything6] + ' with ' +
                  DNA_sequence[anything7])
            print('')
            mutation += 1
            substitution += 1
            print('Substitution')

#At the end of the code print out the total number of Mutations individually and the whole.
print()
print()
print('Total Number of Mutations: ' + str(mutation))
if mutation > 4:
    print('Outlook: You Unfortuantly have developed Cancer')
else:
    print('You Do not have Cancer')
print()
print('Total Substitution: ' + str(substitution))
print()
print('Total Deleation: ' + str(deleation))
print()
print('Total Insertation: ' + str(insertation))