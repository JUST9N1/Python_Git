from tkinter import *
import os

window = Tk()
window.title("Facebook")
window.geometry("1000x600")
window.configure(bg = "#E8E8E8")


def Login_sucess():
    global screen2
    screen2 = Toplevel(window)
    screen2.title("Success")
    screen2.geometry("150x190")
    Label(screen2, text="Login Success").pack()
    Button(screen2, text="OK", command = screen2.destroy).pack()

def Password_not_recognised():
    global screen3
    screen3 = Toplevel(window)
    screen3.title("Invalid Password")
    screen3.geometry("150x190")
    Label(screen3, text="Password not recognised..").pack()
    Button(screen3, text="OK", command = screen3.destroy).pack()

def User_not_found():
    global screen4
    screen4 = Toplevel(window)
    screen4.title("Error")
    screen4.geometry("150x190")
    Label(screen4, text="User not found...").pack()
    Button(screen4, text="OK", command = screen4.destroy).pack()






def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+ "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text= "Registration Sucessful", fg="green").pack()


def signup():
    global screen1
    global username
    global password
    global username_entry
    global password_entry
    screen1 = Toplevel(window)
    screen1.title("SIGN UP")
    screen1.geometry("300x250")

    H1label = Label(screen1, text="SignUP", font=("calibri", 15, "bold")).pack()
    h2label = Label(screen1, text= "it's quick and easy", font=("calibri, 10")).pack()

    username = StringVar()
    password = StringVar()


    Label(screen1, text= "Please enter details below: ").pack()
    Label(screen1, text= "").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1, text= "Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text= "").pack()
    Button(screen1, text= "Register", width=10, height=1, command=register_user).pack()





def login():
    username1 = name.get()
    password = passcode.get()
    username2.delete(0, END)
    userpass.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password in verify:
            Login_sucess()
        else:
            Password_not_recognised()

    else:
            User_not_found()




F_label = Label(window, text="Facebook", bg= "#E8E8E8", font=("Aerial", 50, "bold"), fg= "#427BFF")
F_label.place(x=40, y= 250)

text_label = Label(window, text="Connect with friends and the world",bg = "#E8E8E8", font=("Aerial", 20))
text_label.place(x=40, y= 320)

text_label2= Label(window, text= "around you on facebook",bg = "#E8E8E8", font=("Aerial", 20))
text_label2.place(x=40, y= 351)


canvas = Canvas(window, width=415, height=320, bg= "#fffcfc")
canvas.place(x= 550, y= 150)

name = StringVar()
username2 = Entry(window, textvariable=name, width=25, font=("Verdana", 15), bg="#E8E8E8", fg= "#999999")
username2.place(x= 595, y= 170, height=40)

passcode = StringVar()
userpass = Entry(window, textvariable=passcode, width=25, font=("Verdana", 15), bg="#E8E8E8", fg= "#999999")
userpass.place(x= 595, y= 220, height=40)

loginBtn = Button(window, text = "LOGIN", bg= "blue", fg= "White", font=("Aerial", 15, "bold"), command=login)
loginBtn.place(x = 610, y = 269, width= 290)

fp_btn = Button(window, text="forgot password?", bg="white", fg= "blue")
fp_btn.place(x=685, y= 316)

signupBtn = Button(window, text = "SIGN UP", bg= "blue", fg= "White", font=("Aerial", 15, "bold"), relief="solid", command=signup)
signupBtn.place(x = 610, y = 350, width=290)

last_label= Label(window, text="Join and connect with billions of people.", font=("Aerial",13, "italic" ))
last_label.place(x= 610, y=420)


window.mainloop()