#--------------------------------------------------------#
#File: day quiz_brain                                    #
#Programmed by: Luka Henig (luka.henig@gmail.com)        #
#Curse: 100 Days of Code udemy                           #
#Date: 02/03/2022                                        #
#Description:Litle quiz game to learn und understand     #
#working with an input from API                          #
#--------------------------------------------------------#

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
