import tkinter
import tkinter.messagebox as messagebox

top = tkinter.Tk()
def helloCallBack():
    messagebox.showinfo( "Program GUI", "Hello, this is adillah")

B = tkinter.Button(top, text ="Hello, dila", command =helloCallBack)
B.pack()
top.mainloop()
