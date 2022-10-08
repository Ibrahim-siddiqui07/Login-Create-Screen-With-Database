from Database import Database
from tkinter import*



class LoginScreen:
    def __init__(self, ScreenVar, LoginButton, CreateButton):
        Green_Frame = Frame(width=1000,height=1000,bg="#285943")
        Green_Frame.place(x=500,y=0)
        
        User_Frame = Frame(height=2,width=300)
        User_Frame.place(x=160,y=230)


        Pass_frame = Frame(height=2,width=300)
        Pass_frame.place(x=160,y=280)

        Login_Title = Label(text="Login", font="Arial 66",bg="#77AF9C",fg="#D7FFF1")
        Login_Title.place(x=10,y=0)
        #--------------------------

        self.User_Var = StringVar()

        User_Label = Label(text="Username:",font="Arial 24",bg="#77AF9C",fg="#D7FFF1")
        User_Label.place(x=30,y=200)

        User_entry = Entry(textvariable=self.User_Var, border=0, highlightthickness=0, font="helvetica 24", bg="#77AF9C")
        User_entry.focus()
        User_entry.place(x=160,y=200)

        #-----------------------------

        self.Pass_Var = StringVar()

        Pass_Label = Label(text="Password:", bg="#77AF9C", font="Arial 24", fg="#D7FFF1")
        Pass_Label.place(x=30,y=250)
        Pass_entry = Entry(textvariable=self.Pass_Var,border=0, highlightthickness=0, fg="grey",font="helvetica 24", show="*", bg="#77AF9C")
        Pass_entry.place(x=160,y=250)

        #-----------------------------


        def ShowPass():
            if Pass_entry.cget("show") == "*":
                Pass_entry.config(show="",fg="White")
            else:
                Pass_entry.config(show="*",fg="Grey")

        Show_Pass = Checkbutton(text="Show Password?", bg="#77AF9C", command=ShowPass)
        Show_Pass.place(x=350,y=300)

        #----------------------------


        CreateAccount_button = Button(text="Create Account?" ,border=0, highlightthickness=0, width=10, height=2, command=CreateButton)
        CreateAccount_button.place(x=30,y=800)


        Login_button = Button(text="Login",border=0,highlightthickness=0,background="#77AF9C",width=5,height=2,command=LoginButton)
        Login_button.place(x=255,y=290)



