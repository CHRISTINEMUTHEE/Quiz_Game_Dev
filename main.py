# Importing the Question class
from turtle import end_fill
from question_model import Question
# Importing the data
from data import question_data
from quiz_brain import QuizBrain

# # creating an empty list
question_bank = []
# Iterating through every question with its answer
for item in question_data:
    # Creating a new object from the questions class which has the query and answer as inputs
    my_questions = Question(item["text"], item["answer"])
    # appending the results into the empty list as objects
    question_bank.append(my_questions)
# # Creating an object from the class quiz brain that takes in questions from the bank
my_quiz=QuizBrain(question_bank)
# Looping through the questions till the very end and cumulating the total points gotten correctly

while my_quiz.still_has_question():
    # Go to the next questions
    my_quiz.next_question()
print("You have completed the challenge !!")
print(f"Your total score is {my_quiz.total_points} out of {len(my_quiz.q_list)}")
        
    
    

