from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

Question_Bank = []
for index in range(len(question_data)):
    
    Question_Bank.append(Question(question_data[index]['text'],question_data[index]['answer']))
    

quiz = Quiz_Brain(Question_Bank)



while quiz.still_has_questions() == False:
    quiz.next_question()

