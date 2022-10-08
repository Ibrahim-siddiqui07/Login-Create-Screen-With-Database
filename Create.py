from tkinter import*
from Database import Database



class CreateScreen:
    def __init__(self, Screenvar, CreateButton):


        Create_Title = Label(text="Sign up", font="Arial 66", bg="#77AF9C", fg="#D7FFF1")
        Create_Title.place(x=10,y=0)



        Green_Frame = Frame(width=1000,height=1000,bg="#285943")
        Green_Frame.place(x=500,y=0)

        User_frame = Frame(height=2,width=300)
        User_frame.place(x=160,y=230)

        Pass_frame = Frame(height=2,width=300)
        Pass_frame.place(x=160,y=280)

        RePassword_frame = Frame(height=2,width=300)
        RePassword_frame.place(x=160,y=330)

        #-----------------------------------

        Username_Label = Label(text="Username:", font="Arial 24", bg="#77AF9C", fg="#D7FFF1")
        Username_Label.place(x=30,y=200)

        self.CreateUser_var = StringVar()

        CreateUser_entry = Entry(textvariable=self.CreateUser_var, border=0, highlightthickness=0, font="helvetica 24", bg="#77AF9C")
        CreateUser_entry.focus()
        CreateUser_entry.place(x=160,y=200)

        #-------------------------------------

        Password_Label = Label(text="Password:",bg="#77AF9C",font="Arial 24",fg="#D7FFF1")
        Password_Label.place(x=30,y=250)

        self.CreatePass_var = StringVar()

        CreatePassword_entry = Entry(textvariable=self.CreatePass_var, border=0, highlightthickness=0, fg="grey", font="helvetica 24", bg="#77AF9C", show="*")
        CreatePassword_entry.place(x=160,y=250)

        #--------------------------------------

        RePassword_Label = Label(text="Retype Password:",font="Arial 14",bg="#77AF9C",fg="#D7FFF1")
        RePassword_Label.place(x=30,y=300)


        self.RePassword_var = StringVar()
        RePassword_Entry = Entry(textvariable=self.RePassword_var, border=0, highlightthickness=0, font="helvetica 24", bg="#77AF9C", fg="Grey", show="*")
        RePassword_Entry.place(x=160,y=300)


        def ShowPassword():
            if RePassword_Entry.cget("show") == "*":
                RePassword_Entry.config(show="",fg="White")
            if CreatePassword_entry.cget("show") == "*":
                CreatePassword_entry.config(show="",fg="White")
            else:
                RePassword_Entry.config(show="*",fg="Grey")
                CreatePassword_entry.config(show="*",fg="Grey")




        ShowPassword_Button = Checkbutton(text="Show Password?", bg="#77AF9C", command=ShowPassword)
        ShowPassword_Button.place(x=350,y=350)

        CreateAccount_Button = Button(text="Select" ,border=0, highlightthickness=0, background="#77AF9C", width=5, height=2, command=CreateButton)
        CreateAccount_Button.place(x=255,y=350)
