import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, Entry, Button, END

from PIL import ImageTk, Image
from captcha.image import ImageCaptcha


def createImage(flag=0):


    global random_string
    global image_label
    global image_display
    global entry
    global verify_label
  


    if flag == 1:
        verify_label.grid_forget()


        entry.delete(0, END)


    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))


    image_captcha = ImageCaptcha(width=260, height=60)


    image_generated = image_captcha.generate(random_string)

    image_display = ImageTk.PhotoImage(Image.open(image_generated))

    labe=Label(root,image=image_display)
    # labe.image=image_display
    # labe.grid(row=2, column=1)
    labe.place(x=10,y=120) #------------




def nextPage():
    import page2


def check(x, y):

    k=0
    j=0
    l=0

    global verify_label

    verify_label.grid_forget()

    user=user_info.get()
    pas=pass_info.get()


    if user=="" :
        messagebox.showerror("error","please enter your username")
        j=0
    else:
        j=1

    if pas=="" :
        messagebox.showerror("error","please enter your password") 
        l=0
    else:
        l=1


    if x.lower() == y.lower() :
        k=1
        verify_label = Label(master=root,
        text="Verified ",
        font="Arial 17",
        bg='#ffe75c',
        fg="#00a806"
        )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
        verify_label.place(x=140,y=270)
    else:
        k=0
        verify_label = Label(master=root,
        text="Incorrect!",
        font="Arial 15",
        bg='#ffe75c',
        fg="#fa0800"
        )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
        verify_label.place(x=140,y=270)
        createImage()
    if j==1 and k==1 and l==1:
        nextPage()
        






root = Tk()
root.title('Image Captcha')
root.configure(background='#FF9F9F')

root.geometry('500x400')

Label(root,text="user name", font="20",bg="#FF9F9F").place(x=10,y=20)
Label(root,text="password", font="20",bg="#FF9F9F").place(x=10,y=70)



user_info=StringVar()
pass_info=StringVar()

name_entry=Entry(root,font="10",width=24, bd=2, textvariable=user_info, ) #bd for border for fetching information textvariable written
name_entry.place(x=100,y=25)
pass_entry=Entry(root,font="10",width=24, bd=2, textvariable=pass_info,show="*") #bd for border for fetching information textvariable written
pass_entry.place(x=100,y=75)

verify_label = Label(root)
image_label = Label(root)



entry = Entry(root, width=19, borderwidth=2,font="Arial 15")

entry.place(x=50,y=195)


createImage()


# path = 'ENTER THE PATH OF THE RELOAD BUTTON IMAGE'
reload_img = ImageTk.PhotoImage(Image.open("CAPTCHA.png").resize((32, 32)))
reload_button = Button(image=reload_img, command=lambda: createImage(1))

reload_button.grid(row=2, column=1, pady=10)
reload_button.place(x=320, y=150) #--------------

submit_button = Button(root, text="Submit", font="Arial 10", command=lambda: check(entry.get(), random_string))
submit_button.grid(row=3, column=0, columnspan=2, pady=10)
submit_button.place(x=150, y=230) #-----------
root.bind('<Return>', func=lambda Event: check(entry.get(), random_string))

root.mainloop()






