"""
Project PSIT62
Educational-planning
>>Page: Login
by Suphitsara Cheevanantaporn 61070230
"""
from tkinter import *
#key down function
#window
window = Tk()
window.title("My Educational-planning")
window.configure(background="#7482F4")

photol = PhotoImage(file="graduation.png")
Label (window, image=photol, bg="#7482F4") .grid(row=0, column=0, sticky=W)
#create label
Label (window, text="$$$$$$$$$$  Welcome to Educational-planning  $$$$$$$$$$", bg="#FD2294", fg="white", font="Time 15") .grid(row=1, column=0, sticky=W)

window.mainloop()
