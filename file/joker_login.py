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
window.configure(background="black")

photol = PhotoImage(file="graduation.png")
Label (window, image=photol, bg="black") .grid(row=0, column=0, sticky=W)
#create label
Label (window, text="$$$$$$$$$$  Welcome to Educational-planning  $$$$$$$$$$", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

window.mainloop()
