from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:/Users/admin/StudyPython/Image/GIF/dog.gif")
photo2 = PhotoImage(file = "C:/Users/admin/StudyPython/Image/GIF/cat5.gif")

label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)
label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()

