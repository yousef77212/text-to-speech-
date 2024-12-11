import tkinter as tk
from gtts import gTTS
import os

def play_text():
    text = text_entry.get()
    if text.strip(): 
         
        speech = gTTS(text=text, lang='en', slow=False)
        speech.save("output.mp3")
        os.system("start output.mp3")

 
def set_text():
    text_entry.delete(0, tk.END)


def exit_app():
    root.destroy()

   
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x250")


title_label = tk.Label(root, text="Text to Speech", font=("Arial", 16))
title_label.pack(pady=10)


text_label = tk.Label(root, text="Enter your text:", font=("Arial", 12))
text_label.pack()


text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)


play_button = tk.Button(button_frame, text="Play", command=play_text, width=10)
play_button.grid(row=0, column=0, padx=10)


exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=10, bg="red", fg="white")
exit_button.grid(row=0, column=1, padx=10)


set_button = tk.Button(button_frame, text="Set", command=set_text, width=10)
set_button.grid(row=0, column=2, padx=10)

root.mainloop()

