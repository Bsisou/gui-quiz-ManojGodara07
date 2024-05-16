# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry("1920x1080") 

# Add image file 
bg = PhotoImage(file = "Background.png") 

# Create Canvas 
canvas1 = Canvas( root, width = 1920, 
        height = 1080) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg, 
          anchor = "nw") 


# Create Buttons 
button1 = Button( root, text = "Start", height=3, width=8, bg="white", fg="black", font=("Helvetica", 20)) 

# Display Buttons 
button1_canvas = canvas1.create_window( 1550, 820, anchor = "nw", 
                  window = button1) 

# Execute tkinter 
root.mainloop() 
print("test")