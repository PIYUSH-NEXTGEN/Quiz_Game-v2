from tkinter import *
from quiz_base import *
THEME_COLOR = "#375362"

class QuizInterface  :

    def __init__(self,quiz_base: QuizBrain):
        self.quiz  = quiz_base
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.canvas = Canvas(height=250,width=300,bg="white")

        false_png  = PhotoImage(file="false.png")
        true_image  = PhotoImage(file="true.png")

        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_button_pressed)
        self.true_button.grid(row=2,column=0)

        self.false_button = Button(image=false_png,highlightthickness=0,command=self.false_button_pressed)
        self.false_button.grid(row=2,column=1)


        self.score_label = (Label(text="Score: 0",fg="white",bg=THEME_COLOR))
        self.score_label.grid(row=0,column = 1)

        self.question_text = self.canvas.create_text(150,125,text="Some question text ", fill=THEME_COLOR ,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(pady=50,row=1,column=0,columnspan=2)

        self.get_next_question()

        self.window.mainloop()

    def  get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.canvas.itemconfig(self.question_text,text="You have completed the quiz . Thanks to give it a try")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,right):
        if right :
            self.canvas.config(bg="green")

        else :
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)



