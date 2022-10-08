from Create import CreateScreen
from Main import MainScreen
from Login import LoginScreen
from Database import Database
from tkinter import*







Screen = Tk()
Screen.title("Login")
Screen.config(bg="#77AF9C")
Screen.attributes("-fullscreen", True)




def LoginButton_Command():
    MyLoginCollection = Database("LoginInformation", "LoginData")

    LoginEntry_Var =  LoginWidgets.User_Var.get()
    PasswordEntry_Var =  LoginWidgets.Pass_Var.get()

    UserName_Query = MyLoginCollection.MyCollection.find_one({"Username": LoginEntry_Var})
    PasswordName_Query = MyLoginCollection.MyCollection.find_one({"Password": PasswordEntry_Var})

    if UserName_Query and PasswordName_Query:
        for items in Screen.winfo_children():
                    items.destroy()
        #Put Main Screen here

    else:
        Warning_Label = Label(text="Wrong Username or Password!", fg='#8CD790',bg="#77AF9C",font="Arial 24")
        Warning_Label.place(x=10,y=350)


    if not LoginEntry_Var or not PasswordEntry_Var:
        Warning_label = Label(text="Blank Username Or Password!",fg='#8CD790',bg="#77AF9C",font="Arial 24")
        Warning_label.place(x=10,y=350)

def CreateButton_Command():
    CreateAccount_Collection = Database("LoginInformation", "LoginData")
    LoginEntry_Var = CreateAccount_Screen.CreateUser_var.get()
    PasswordEntry_Var = CreateAccount_Screen.CreatePass_var.get()
    RePasswordEntry_Var = CreateAccount_Screen.RePassword_var.get()

    AccountCheck = CreateAccount_Collection.MyCollection.find_one({"Username": LoginEntry_Var})
    if AccountCheck:
        WarningLabel = Label(text="Username Is Already Taken!",fg='#8CD790',bg="#77AF9C",font="Arial 24")
        WarningLabel.place(x=10,y=400)
    
    if not RePasswordEntry_Var == PasswordEntry_Var:
        WarningLabel = Label(text="Passwords don't match!",width=20,fg='#8CD790',bg="#77AF9C",font="Arial 30")
        WarningLabel.place(x=10,y=400)

    if not RePasswordEntry_Var or not PasswordEntry_Var or not LoginEntry_Var:
        Warninglabel = Label(text="Blank Username Or Password!",fg='#8CD790',bg="#77AF9C",font="Arial 24")
        Warninglabel.place(x=10,y=400)
    elif RePasswordEntry_Var == PasswordEntry_Var and not AccountCheck:
        CreateAccount = {"Username": LoginEntry_Var, "Password": PasswordEntry_Var}
        CreateAccount_Collection.MyCollection.insert_one(CreateAccount)
        for items in Screen.winfo_children():
            items.destroy()
        #Insert Main Screen
    
    








def CreateScreen_Command():
    for items in Screen.winfo_children():
        items.destroy()
    global CreateAccount_Screen
    CreateAccount_Screen = CreateScreen(Screen, CreateButton_Command)









LoginWidgets = LoginScreen(Screen, LoginButton_Command, CreateScreen_Command)





















Screen.mainloop()