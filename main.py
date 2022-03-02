#--------------------------------------------------------#
#File: day quiz_brain                                    #
#Programmed by: Luka Henig (luka.henig@gmail.com)        #
#Curse: 100 Days of Code udemy                           #
#Date: 02/03/2022                                        #
#Description:Litle quiz game to learn und understand     #
#working with an input from API                          #
#--------------------------------------------------------#

#-------------------IMPORTS------------------------------#
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
