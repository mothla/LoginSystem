from tkinter import *

root = Tk()
root.title("Sign in system")
root.geometry("400x320")  # set starting size of window
root.maxsize(400, 320)  # width x height
root.config(bg="#ffffff")  # set background color of root window

login = Label(root, text="SIGN IN", bg="white", fg='#FF74B1')#relief=RAISED
login.pack(ipady=5, fill='x')
login.config(font=("Font", 30))  # change font and size of label

# login image
image = PhotoImage(file="log.png")
img_resize = image.subsample(5,5)
Label(root, image=img_resize, bg="white").pack(pady=5)

def checkInput():
    usernm = "Mothla"
    pswrd = "mothla1234"
    entered_usernm = username_entry.get()  # get username from Entry widget
    entered_pswrd = password_entry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
       print("Welcome Mothla!")
       root.destroy()

    else:
        print("Login failed: Invalid username or password.")

def toggled():
 #display a message to the terminal every time the check button is clicked
   print("The check button works.")

# Username Entry
username_frame = Frame(root, bg="#ffffff")
username_frame.pack()

Label(username_frame, text="Username", bg="#ffffff").pack(side='left', padx=6)

username_entry = Entry(username_frame, bd=0)
username_entry.pack(side='right')

# Password entry
password_frame = Frame(root, bg="#ffffff")
password_frame.pack()

Label(password_frame, text="Password", bg="#ffffff").pack(side='left', padx=7)

password_entry = Entry(password_frame, bd=0)
password_entry.pack(side='right')

# Create Go! Button

go_button = Button(root, text="sign in", command=checkInput, bg="#ffffff", width=8)

go_button.pack(pady=10, padx=50)

# Remember me and forgot password
bottom_frame = Frame(root, bg="#EFEFEF")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#EFEFEF", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#EFEFEF")
forgot_pswrd.pack(side="right", padx=19)

root.mainloop()


