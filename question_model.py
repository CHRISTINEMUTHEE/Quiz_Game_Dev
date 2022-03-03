# creating a python class with two attributes
class Question:
    '''
    This class takes in two parameters when initialized
    param_1: text which should serve as our query
    param_2: this should serve as your answer
    '''
    def __init__(self , text , answer):
        self.query = text
        self.answer = answer


# Creating an object from the class
# my_quiz=Question("what is my name", "Christine")
#
#
# print(my_quiz.query)
# print(my_quiz.answer)