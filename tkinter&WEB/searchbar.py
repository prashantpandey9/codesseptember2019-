from tkinter import *
import webbrowser
win=Tk()
win.title("Search Bar")
def search():
    url=entry.get()
    webbrowser.open("https://www.google.com"+url)
    
label1=Label(win,text="Enter URL Here:  ",font=("arial",10,"bold"))
label1.grid(row=0,column=0)

entry=Entry(win,width=30)
entry.grid(row=0,column=1)

button=Button(win,text="Search",command=search,bg='pink',fg='blue')
button.grid(row=1,column=0,columnspan=2,pady=2)


win.mainloop()

