from tkinter import *

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

        #load image
        self.bg = PhotoImage(file="Background.png")        
        self.bg1 = PhotoImage(file="cricket quiz.png")

        # Initialize frames
        self.main_page_frame = Frame(self.root)
        self.quiz_page_frame = Frame(self.root)
        self.result_page_frame = Frame(self.root)

        # Initialize variables
        self.score = IntVAr()
        self.score.set(0)
        self.question_index = 0
        self.question_text = StringVar()

        # create pages
        self.create_main_page(self.bg)        
        self.create_quiz_page(self.bg1)
        self.create_result_page(self.bg1)

        # Show main page
        self.show_main_page()

    def show_main_page(self):
        self.main_page_frame.pack(side="left", fill="both", expand=True)
        self.quiz_page_frame.pack_forget()
        self.result_page_frame.pack_forget()

    def show_quiz_page(self):
        self.main_page_frame.pack_forget()
        self.quiz_page_frame.pack(side="left", fill="both", expand=True)
        self.result_frame.pack_forget()
        self.display_question(0)

    def display_question(self, question_index):
        self.question_index = question_index
        if question_index < len(cricket_questions):
            question = cricket_questions[question_index]
            self.question_text.set(question["question"])
            for i, choice in enumerate(question["choices"]):
                self.choice_buttons[i].config(text=choice, command=lambda c=choice: self.check_answer(c))
        else:
            self.show_result()

    def check_answer(self, selected_choice):
        correct_choice = cricket_questions[self.question_index]["correct"]
        if selected_choice == correct_choice:
            self.score.set(self.score.get() + 1)
        self.question_index += 1
        self.display_question(self.question_index + 1)

    def show_result(self):
        self.quiz_page_frame.pack_forget()
        self.result_frame.pack(side="left", fill="both", expand=True)
        self.result_label.config(text=f"Your score: {self.score.get()} / {len(cricket_question)}")

    def create_main_page(self, bg):
        self.main_page_frame.pack_forget()
        self.main_page_frame.pack(side="left", fill="both", expand=True)
        canvas1 = Canvas(self.main_page_frame, width=1920, height=1080)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        textentry = Entry(canvas1)
        canvas1.create_window(885, 890, window=textentry, height=135, width=495)
        start_button = Button(canvas1, text="Start", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=self.show_quiz_page)
        canvas1.create_window(1550, 820, anchor="nw", window=start_button)