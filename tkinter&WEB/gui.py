import tkinter
m=tkinter.Tk(className='Claci')
m.title("Counting Seconds")
button=tkinter.Button(m,text='Stop',width=25,command=m.destroy)
button.pack()
m.mainloop()
