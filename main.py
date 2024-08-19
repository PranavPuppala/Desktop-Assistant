from tkinter import *
from PIL import Image, ImageTk # type: ignore
import speechToText
import actions

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def on_enter(event):
    send()

def ask():
    user_data = speechToText.speech_to_text()
    user_data = user_data.lower()
    result = actions.action(user_data)
    text.insert(END, "User: " + user_data + "\n")
    print(result)
    
    if result == "shutting down...": 
        root.destroy()
    elif result is not None:
        text.insert(END, "Assistant: " + result + "\n")
    
    # Auto-scroll
    text.see(END)

def send():
    user_data = entry.get()
    entry.delete(0, END)
    user_data = user_data.lower()
    result = actions.action(user_data)
    text.insert(END, "User: " + user_data + "\n")
    print(result)
    
    if result == "shutting down...": 
        root.destroy()
    elif result is not None:
        text.insert(END, "Assistant: " + result + "\n")
    
    # Auto-scroll
    text.see(END)

def delete():
    text.delete("1.0", END)

# Main window
root = Tk()
center_window(root, 550, 710)
root.resizable(False, False)
root.config(bg="#9ba3a0")

# Create a LabelFrame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", bg="#9ba3a0")
frame.grid(row=0, column=1, padx=70, pady=20)

# Create a Label with a proper bd value
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bd=0, relief="solid", bg="#9ba3a0")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
img_name = r"Desktop _Assistant_Project\assistant.png"
image = Image.open(img_name)
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image=image)
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Text widget
text = Text(root, font=("Courier", 10, "bold"), bg="#358194")
text.grid(row=2, column=0)
text.place(x=90, y=350, width=375, height=100)

# Entry widget
entry = Entry(root)
entry.place(x=90, y=480, width=375, height=30)

# Buttons
ask_button = Button(root, text="ASK", command=ask, activebackground="#358194", pady=16, padx=40, bg="#358194", borderwidth=3, relief="solid")
ask_button.place(x=40, y=575)

delete_button = Button(root, text="DELETE", command=delete, activebackground="#358194", pady=16, padx=40, bg="#358194", borderwidth=3, relief="solid")
delete_button.place(x=220, y=575)

send_button = Button(root, text="SEND", command=send, activebackground="#358194", pady=16, padx=40, bg="#358194", borderwidth=3, relief="solid")
send_button.place(x=400, y=575)

# Bind Enter key to the on_enter function
root.bind('<Return>', on_enter)

root.mainloop()


