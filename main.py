import random


bChangeCorrect = 0
bRandomCorrect = 0
rCorrect = 0

iterations = round(1E6)
answers = []
for i in range(iterations):
    answers.append(random.randint(1,3))


def eliminateOne(answer, guess,mustChange:bool):
    global possible_answers
    remaining_answers = [1,2,3]
    remaining_answers.remove(answer)

    if( mustChange):
        try:
            remaining_answers.remove(guess)
        except:
            pass

    possible_answers.remove(remaining_answers[random.randint(0,len(remaining_answers)-1)])

    possible_answers.index(answer)
    return possible_answers

for i in range(iterations):
    


    answer =  answers[i]
    bGuess = rGuess = random.randint(1,3)
    possible_answers = [1,2,3]
    remaining_answersChange = eliminateOne(answer=answer,guess=bGuess,mustChange=True)
    possible_answers = [1,2,3]
    remainting_answersRandom = eliminateOne(answer=answer,guess=bGuess,mustChange=True)
    bGuessChange = remaining_answersChange[random.randint(0,len(remaining_answersChange)-1)]
    bGuessRandom = remainting_answersRandom[random.randint(0,len(remainting_answersRandom)-1)]

    if(bGuessChange == answer):
        bChangeCorrect+=1
    if(bGuessRandom == answer):
        bRandomCorrect +=1
    if(rGuess == answer):
        rCorrect += 1

    if(i%round((iterations*0.05)) == 0):
        print(f"{round((i/iterations)*100,3)}%")


for i in range(2):
    print("")
print(f"Number Correct Randomly: {rCorrect}")
print(f"Number Correct By Changing: {bChangeCorrect}")
print(f"Number Correct By Random: {bRandomCorrect}")
    

for i in range(1):
    print("")