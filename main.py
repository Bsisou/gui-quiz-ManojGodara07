from tkinter import *
from tkinter import messagebox
import random

# List of cricket quiz questions
cricket_questions = [
    {
        "question": "How many players are there in a cricket team?",
        "choices": ["9", "10", "11", "12"],
        "correct": "11"
    },
    {
        "question": "What is the length of a cricket pitch?",
        "choices": ["18 yards", "20 yards", "22 yards", "24 yards"],
        "correct": "22 yards"
    },
    {
        "question": "What are the two main types of bowlers in cricket?",
        "choices": ["Fast and spin", "Fast and slow", "Spin and swing", "Medium and off-spin"],
        "correct": "Fast and spin"
    },
    {
        "question": "What does LBW stand for in cricket?",
        "choices": ["Leg Before Wicket", "Leg Behind Wicket", "Leg Between Wickets", "Leg By Wicket"],
        "correct": "Leg Before Wicket"
    },
    {
        "question": "How many runs are awarded for hitting the ball over the boundary without it touching the ground?",
        "choices": ["4", "5", "6", "7"],
        "correct": "6"
    },
    {
        "question": "What is the term used when a bowler dismisses three batsmen with consecutive deliveries?",
        "choices": ["Double Hat-trick", "Triple Wicket", "Hat-trick", "Quick Wicket"],
        "correct": "Hat-trick"
    },
    {
        "question": "How many balls are there in an over in cricket?",
        "choices": ["4", "5", "6", "8"],
        "correct": "6"
    },
    {
        "question": "What is the role of a wicketkeeper in cricket?",
        "choices": ["To bowl deliveries", "To catch balls behind the stumps", "To field in the deep", "To bat first"],
        "correct": "To catch balls behind the stumps"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")

        # Load images
        self.bg = PhotoImage(file="Background.png")
        self.bg1 = PhotoImage(file="Cricket quiz.png")

        # Initialize frames
        self.main_page_frame = Frame(self.root)
        self.quiz_page_frame = Frame(self.root)
        self.result_frame = Frame(self.root)

        # Initialize variables
        self.score = IntVar()
        self.score.set(0)
        self.question_index = 0
        self.question_text = StringVar()
        self.user_input = StringVar()
        self.user_name = StringVar()

        # Shuffle the questions
        self.shuffled_questions = random.sample(cricket_questions, len(cricket_questions))

        # Create pages
        self.create_main_page(self.bg)
        self.create_quiz_page(self.bg1)
        self.create_result_page(self.bg1)

        # Show main page
        self.show_main_page()

    def validate_input(self, P):
        if len(P) > 7:
            messagebox.showerror("Input Error", "Input cannot be more than 7 characters. Please try again.")
            return False
        return True

    def show_main_page(self):
        self.main_page_frame.pack(side="left", fill="both", expand=True)
        self.quiz_page_frame.pack_forget()
        self.result_frame.pack_forget()

    def show_quiz_page(self):
        if len(self.user_input.get()) == 0:
            messagebox.showerror("Input Error", "Please enter your name.")
            return
        self.user_name.set(self.user_input.get())
        self.main_page_frame.pack_forget()
        self.quiz_page_frame.pack(side="left", fill="both", expand=True)
        self.result_frame.pack_forget()
        self.display_question(0)

    def display_question(self, question_index):
        self.question_index = question_index
        if question_index < len(self.shuffled_questions):
            question = self.shuffled_questions[question_index]
            self.question_text.set(question["question"])
            for i, choice in enumerate(question["choices"]):
                self.choice_buttons[i].config(text=choice, command=lambda c=choice: self.check_answer(c))
        else:
            self.show_result()

    def check_answer(self, selected_choice):
        correct_choice = self.shuffled_questions[self.question_index]["correct"]
        if selected_choice == correct_choice:
            self.score.set(self.score.get() + 1)
        self.score_label.config(text=f"Score: {self.score.get()}")
        self.display_question(self.question_index + 1)

    def show_result(self):
        self.quiz_page_frame.pack_forget()
        self.result_frame.pack(side="left", fill="both", expand=True)
        score = self.score.get()
        total_questions = len(self.shuffled_questions)

        if score == total_questions:
            result_message = "Perfect score! You're a cricket genius!"
        elif score > total_questions / 2:
            result_message = "Great job! You know your cricket well."
        else:
            result_message = "Keep practicing! You'll get better with time."

        self.result_label.config(text=f"{self.user_name.get()}, your score: {score} / {total_questions}\n{result_message}")

    def create_main_page(self, bg):
        self.main_page_frame.pack_forget()
        self.main_page_frame.pack(side="left", fill="both", expand=True)
        canvas1 = Canvas(self.main_page_frame, width=1920, height=1080)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")

        validate_cmd = self.root.register(self.validate_input)
        textentry = Entry(canvas1, textvariable=self.user_input, validate="key", validatecommand=(validate_cmd, '%P'))
        canvas1.create_window(885, 890, window=textentry, height=135, width=495)

        start_button = Button(canvas1, text="Start", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=self.show_quiz_page)
        canvas1.create_window(1550, 820, anchor="nw", window=start_button)

    def create_quiz_page(self, bg1):
        self.quiz_page_frame.pack_forget()
        self.quiz_page_frame.pack(side="left", fill="both", expand=True)
        canvas2 = Canvas(self.quiz_page_frame, width=1920, height=1080)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg1, anchor="nw")

        question_label = Label(canvas2, textvariable=self.question_text, font=("Helvetica", 20), bg="white")
        question_label.place(x=960, y=200, anchor="center")

        self.choice_buttons = []
        for i in range(4):
            button = Button(canvas2, text="", height=5, width=20, bg="white", fg="black", font=("Helvetica", 18))
            self.choice_buttons.append(button)
            if i < 2:
                button.place(x=540 + i*700, y=400, anchor="center")
            else:
                button.place(x=540 + (i-2)*700, y=600, anchor="center")

        exit_button = Button(canvas2, text="Exit", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=self.show_main_page)
        canvas2.create_window(1550, 820, anchor="nw", window=exit_button)

        # Add a label for displaying the score
        self.score_label = Label(canvas2, text="Score: 0", font=("Helvetica", 20), bg="white")
        self.score_label.place(x=1800, y=50, anchor="center")

    def create_result_page(self, bg1):
        self.result_frame.pack_forget()
        self.result_frame.pack(side="left", fill="both", expand=True)
        canvas3 = Canvas(self.result_frame, width=1920, height=1080)
        canvas3.pack(fill="both", expand=True)
        canvas3.create_image(0, 0, image=bg1, anchor="nw")
        self.result_label = Label(canvas3, text="", font=("Helvetica", 20), bg="white")
        self.result_label.place(x=960, y=540, anchor="center")
        exit_button = Button(canvas3, text="Exit", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=self.show_main_page)
        exit_button.place(x=1550, y=820, anchor="nw")

# Create object
root = Tk()
app = QuizApp(root)
root.mainloop()
