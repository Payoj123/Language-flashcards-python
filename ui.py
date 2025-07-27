from tkinter import * 
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR ="#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        ###### Window Setup #########
        self.window =Tk()
        self.window.title("Quizphase")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #####Rules######
        rules_text = (
            "📋 Quiz Rules:\n\n"
            "✔️ You will be asked 10 True/False questions.\n"
            "✔️ Click the ✅ (True) or ❌ (False) button to answer.\n"
            "✔️ You'll get 1 point for each correct answer.\n"
            "❌ No points are deducted for wrong answers.\n"
            "🏁 Your final score will be shown at the end.\n\n"
            "Good luck! 💪"
        )
        messagebox.showinfo(title="Welcome to QuizPhase!", message=rules_text)
        self.score=0
        self.my_label=Label(text=f"Score:{self.score}",font=("Ariel", 15,"bold"), fg="white",bg=THEME_COLOR)
        self.my_label.grid(row=0,column=1)
        ######### Canvas Setup ###########
        self.canvas =Canvas(self.window, width=300, height=200, bg="white",highlightthickness=0)
        self.questions=self.canvas.create_text(150,100,width=280,text="Questions",font=("Ariel",20,"italic"),fill="black")
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        ######### Button Setup ###########
        self.True_image=PhotoImage(file=r"D:\python\My codeeess\date and time\API\Quiz_app\images\true.png")
        self.True_button=Button(self.window,image=self.True_image,bg=THEME_COLOR, highlightthickness=0,command=self.is_True)
        self.True_button.grid(row=2,column=0)
        self.True_label=Label(text=f"True",font=("Ariel", 15,"bold"), fg="white",bg=THEME_COLOR)
        self.True_label.grid(row=3,column=0)

        self.False_image=PhotoImage(file=r"D:\python\My codeeess\date and time\API\Quiz_app\images\false.png")
        self.False_button=Button(self.window,image=self.False_image,bg=THEME_COLOR, highlightthickness=0,command=self.is_False)
        self.False_button.grid(row=2,column=1)
        self.False_label=Label(text=f"False",font=("Ariel", 15,"bold"), fg="white",bg=THEME_COLOR)
        self.False_label.grid(row=3,column=1) 
        self.get_next_question()
        self
        self.window.mainloop()
    ######### Functions Setup ###########
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions,text=q_text)
        else:
            self.canvas.itemconfig(self.questions,text="You've reached the end of the quiz!")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")
            messagebox.showinfo(title="Quiz Completed", message=f"Your final score is {self.score}/{self.quiz.question_number}")
    def is_True(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def is_False(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def reset_canvas(self):
        self.canvas.config(bg="white")
        self.get_next_question()
    def give_feedback(self,is_right):
        if is_right:
            self.score+=1
            self.my_label.config(text=f"Score:{self.score}")
            self.canvas.config(bg="green")
            self.window.after(1000,self.reset_canvas)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.reset_canvas)




        
        