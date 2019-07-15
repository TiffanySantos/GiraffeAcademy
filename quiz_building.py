#import the class 
from questions import question
# questions array
question_prompts = [
 "What color are apples?\n(a) red\n(b) purple\n(c) orange\n\n",
 "What color are bananas?\n(a) yellow\n(b) blue\(c) red\n\n",
 "What color are strawberries?\n(a) yellow\n(b) red\(c) purple\n\n"
]
# correct answers arra
questions = [
    question(question_prompts [0], "a"),
    question(question_prompts [1], "a"),
    question(question_prompts [2], "b"),
]
# loop through all questions, keeping track of score
def run_test(questions):
    score = 0 #init score to 0
    for question in questions: #do the following for each question
        answer = input(question.prompt) #take users answer
        if answer == question.answer: #check if the answer is correct
            score += 1 # add one for every correct answer
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
# call the function
run_test(questions)