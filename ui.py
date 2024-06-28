from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
#This is the quiz UI
class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizzler'
        self.window.configure(bg=THEME_COLOR, padx=20,pady=20)

        score = self.user_score = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.user_score.grid(row=0, column=1)

        self.user_canvas = Canvas(height=250, width=300, bg='White')
        self.question_text = self.user_canvas.create_text(150, 125, text='This is the question',
                                     fill=THEME_COLOR,
                                     font=('Arial', 20, 'italic'),
                                     width=280)
        self.user_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        ok_image = PhotoImage(file="images/true.png",height=97, width=100)
        not_ok_image = PhotoImage(file="images/false.png", height=97, width=100)

        self.ok_button = Button(image=ok_image, command=self.is_true, state="active")
        self.ok_button.grid(row=2, column=0)

        self.not_ok_button = Button(image=not_ok_image, command=self.is_false, state="active")
        self.not_ok_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.user_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.user_score.config(text= f"Score: {self.quiz.score}/10")
            q_text = self.quiz.next_question()
            self.user_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.user_canvas.itemconfig(self.question_text, text="This is the end of the game")
            self.not_ok_button.config(state="disabled")
            self.ok_button.config(state="disabled")
    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            bg = "green"
        else:
            bg = "red"
        self.user_canvas.config(bg=bg)
        self.window.after(1000, self.get_next_question())

