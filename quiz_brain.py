#--------------------------------------------------------#
#File: day quiz_brain                                    #
#Programmed by: Luka Henig (luka.henig@gmail.com)        #
#Curse: 100 Days of Code udemy                           #
#Date: 02/03/2022                                        #
#Description:Litle quiz game to learn und understand     #
#working with an input from API                          #
#--------------------------------------------------------#

#--------------------CONSTANTS---------------------------#
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """returns number of questions left"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """display next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        #self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False