# Creating a quiz brain class with two attributes and a method 
class QuizBrain:
    '''This class has two attributes
    1. number: This checks the question number
    2. list: This is a list of questions from the question bank'''
    def __init__(self,list):
        self.question_number=0
        self.q_list=list
        self.total_points=0
    # Creating a function
    ''' This function moves to the next question after we have checked if the answer is corect'''
    def next_question(self):
        current_question=self.q_list[self.question_number]
        # Let the question number start at 1
        self.question_number +=1
        user_input= input(f"Q {self.question_number} : {current_question.query} ? True/False")
        # Checking whether the answer was correct or wrong
        if user_input.lower()==current_question.answer.lower():
            print("You got it correct")
            self.total_points+=1
            
        else:
            print("You got it wrong")
        print(f"The correct answer is {current_question.answer}")  
        print(f"Total Points = {self.total_points} out of {len(self.q_list)}") 
    def still_has_question(self):
        # If the question number is equal to the total length of the questions, terminate the operation / return false
        # else is there are still question return true
        return self.question_number < len(self.q_list)              
    

