#--------------------------------------------------------#
#File: day quiz_brain                                    #
#Programmed by: Luka Henig (luka.henig@gmail.com)        #
#Curse: 100 Days of Code udemy                           #
#Date: 02/03/2022                                        #
#Description:Litle quiz game to learn und understand     #
#working with an input from API                          #
#--------------------------------------------------------#

#---------------------IMPORTS----------------------------#
from tkinter import *
from quiz_brain import QuizBrain

#----------------------CONSTANTS-------------------------#
THEME_COLOR = "#375362"


class QuizInterface:
    """UI for the game"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_btn_pressed)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_btn_pressed)
        self.false_btn.grid(row=2, column=1)

        self.score_lbl = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_lbl.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        """Check if there is a question left and display it"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You reached the end, the quiz is out of questions")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)