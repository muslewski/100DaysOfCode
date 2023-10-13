from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from quiz_brain import QuizBrain

# Night Blue
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.gif = Image.open("images/space.gif")
        # Create a list of PhotoImage objects for each frame
        self.gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.gif)]
        self.current_frame = 0
        self.background_label = Label(self.window, image=self.gif_frames[self.current_frame])
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.window.after(100, self.update_gif)

        self.score_label = Label(text=" Score: 0 ",relief=SUNKEN, bg="white", fg=THEME_COLOR, font=("Arial", 18, "normal"))
        self.score_label.config(highlightthickness=0)
        self.canvas = Canvas(bg="white", height=250, width=300, relief=SUNKEN, borderwidth=3)
        self.question_text = self.canvas.create_text(150, 125, text="something", font=FONT, fill=THEME_COLOR, width=280)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.correct)
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.wrong)

        self.score_label.grid(column=1, row=0, pady=20)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.button_true.grid(column=0, row=2, pady=20)
        self.button_false.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#ccffdd")
        else:
            self.canvas.config(bg="#ff9999")
        self.canvas.after(1000, self.get_next_question)
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def update_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.background_label.configure(image=self.gif_frames[self.current_frame])
        self.window.after(25, self.update_gif)  # Update speed
