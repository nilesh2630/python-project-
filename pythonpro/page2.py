from tkinter import *
 
ws = Tk()
ws.geometry('800x600')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

  
 
Label(
    ws,
    text="Welcome!! You are sucssefully logged in 😊 🎉",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font ="ariel 27 bold",
    fg="white"
).pack(expand=True, fill=BOTH)
 
 
 
ws.mainloop()