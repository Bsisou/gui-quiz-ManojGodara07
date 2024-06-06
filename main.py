# Import module 
from tkinter import *

# Funtction to show the main page
def show_main_page():
            main_page_frame.pack(side="left", fill="both", expand=True)
            quiz_page_frame.pack_forget()
            result_frame.pack_forget()

# Function to show the quiz page
def show_quiz_page():
            main_page_frame.pack_forget()
            quiz_page_frame.pack(side="left", fill="both", expand=True)
            result_frame.pack_forget()

def create_main_page(bg):

            # Add content to the main window
            main_page_frame.pack_forget()  # In case it's already packed
            main_page_frame.pack(side="left", fill="both", expand=True)
            canvas1 = Canvas(main_page_frame, width=1920, height=1080)
            canvas1.pack(fill="both", expand=True)
            canvas1.create_image(0, 0, image=bg, anchor="nw")
            textentry = Entry(canvas1)
            canvas1.create_window(885, 890, window=textentry, height=135, width=495)
            back_button = Button(canvas1, text="Start", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=show_quiz_page)
            button1_canvas = canvas1.create_window(1550, 820, anchor="nw", window=back_button)

def create_quiz_page(bg1):
            # Add content to the quiz window
            quiz_page_frame.pack_forget()  # In case it's already packed
            quiz_page_frame.pack(side="left", fill="both", expand=True)
            canvas2 = Canvas(quiz_page_frame, width=1920, height=1080)
            canvas2.pack(fill="both", expand=True)  # Make the canvas fill the frame
            canvas2.create_image(0, 0, image=bg1, anchor="nw")
            back_button = Button(canvas2, text="Back", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20), command=show_main_page)
            button1_canvas = canvas2.create_window(1550, 820, anchor="nw", window=back_button)
        
# Create object 
root = Tk() 
root.geometry("1920x1080")  # Set the size of the window

# creat frames
main_page_frame = Frame(root)
quiz_page_frame = Frame(root)
result_frame = Frame(root)

# Load images
bg = PhotoImage(file="Background.png")
bg1 = PhotoImage(file="Cricket quiz.png")

# Execute tkinter
create_main_page(bg)   # Then create main page
create_quiz_page(bg1)  # Create quiz page first
root.mainloop()