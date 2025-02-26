from tkinter import *           # Import evey thing from tkinter module using * .
from tkinter import messagebox
from tkinter import ttk


pro = Tk()                      # Create a object of Tk class and assign it to pro.
pro.geometry("500x400")         # Set the width and height of the window.
pro.resizable(0, 0)             # Set the window resizable in x and y direction.
pro.title("LOG IN system")          # Set the title of the window.
pro.configure(bg="Teal")  # Set the background color of the window.
pro.config(cursor="arrow")      # Set the cursor of the window.
pro.iconbitmap("F:ROS\\Tkinter for GUI\\icon1.ico")     # Set the icon of the window.
scl = Scrollbar(pro , orient=VERTICAL )            # Create a scrollbar.
scl.pack(side=RIGHT, fill=Y)    # Add the scrollbar to the window.

# ------------------- Functions for commands -------------------
def login() :
    username = "ziad"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo("Login Status", "Login Successful!\nWelcome to our community")
        username_entry.delete(0 , END)
        password_entry.delete(0 , END)
        login_window()
    else:
        messagebox.showerror("Login Status", "Invalid Username or Password\nPlease try again")
        username_entry.delete(0 , END)
        password_entry.delete(0 , END)

def signup():
    signup_window = Toplevel(pro)
    signup_window.title("SIGN UP System")
    signup_window.geometry("400x400")
    signup_window.iconbitmap("F:ROS\\Tkinter for GUI\\icon1.ico")     # Set the icon of the window.
    signup_window.configure(bg="Teal")
    # ------------------- Insert photo ---------------------
    background_photo = PhotoImage(file="F:ROS\\Tkinter for GUI\\photo.png" )  # Create a photo.
    label5 = Label(signup_window, image=background_photo)  # Create a label for the photo. 
    label5.image = background_photo 
    label5.pack()                   # Add the label to the window.
    label5.place(x=0, y=0)     # Set the position of the label.
    # ------------------- Header Name ---------------------
    header = Label(signup_window, text="SIGN UP System", bg="Teal", fg="white", font="Courier 22 bold")  # Create a label.
    header.pack()                   # Add the label to the window.
    header.place(x=120, y=1)     # Set the position of the label.
    # ------------------- First Name ---------------------
    firstname = Label(signup_window, text="First Name", bg="Teal", fg="white", font="Arial 15 bold")
    firstname.pack()
    firstname.place(x=30, y=60)     # Set the position of the entry.
    lastname = Label(signup_window, text="Last Name", bg="Teal", fg="white", font="Arial 15 bold")
    lastname.pack()
    lastname.place(x=30, y=100)     # Set the position of the entry.
    passwordConfirm = Label(signup_window , text="Password " ,bg= "Teal" ,fg= "white" ,font= "Arial 15 bold")
    passwordConfirm.pack()
    passwordConfirm.place(x=30, y=140)     # Set the position of the entry.
    country = Label(signup_window , text="Country  " ,bg= "Teal" ,fg= "white" ,font= "Arial 15 bold")
    country.pack()
    country.place(x=30, y=220)     # Set the position of the entry.
    phone = Label(signup_window , text="Phone Number" ,bg= "Teal" ,fg= "white" ,font= "Arial 15 bold")
    phone.pack()
    phone.place(x=30, y=180)     # Set the position of the entry.
    version = Label(signup_window , text= "Version 1.0 @Ziad" , fg= "white" , bg= "grey" , font= " Arial 15 ")
    version.pack()
    version.place(x= 130 , y= 330)
    # --------------------- Entry -------------------------------
    firstnameentry = Entry(signup_window, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "10")  # Create an entry.
    firstnameentry.pack()                   # Add the entry to the window.  
    firstnameentry.place(x=150 , y=60)     # Set the position of the entry.
    lastnameentry = Entry(signup_window, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "10")  # Create an entry.
    lastnameentry.pack()                   # Add the entry to the window.  
    lastnameentry.place(x=150 , y=100)     # Set the position of the entry.
    passwordentry = Entry(signup_window, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "15")  # Create an entry.
    passwordentry.pack()                   # Add the entry to the window.  
    passwordentry.place(x=150 , y=140)     # Set the position of the entry.
    phoneentry = Entry(signup_window, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "15")  # Create an entry.
    phoneentry.pack()                   # Add the entry to the window.  
    phoneentry.place(x=190 , y=180)     # Set the position of the entry.
    countrycombo = ttk.Combobox(signup_window, state="readonly", values=["Egypt", "USA", "Canada", "UK", "Australia"], font="Arial 15 bold", width=12)
    countrycombo.pack()
    countrycombo.place(x=150, y=220)       # Set the position of the combobox
    # ----------------------- Button ---------------------------------
    signup_1 = Button(signup_window , text= "sign up" , bg = "maroon" , fg = "white" , font = "Arial 15 bold" , cursor= "hand2" , justify= "center" , width="10" , command = signup_finish )
    signup_1.pack()
    signup_1.place(x=160, y=270)     # Set the position of the entry.

def signup_finish():
    messagebox.showinfo("signup Status", "sign up Successful!\nWelcome to our community")

def login_window():
    new_window = Toplevel(pro)
    new_window.title("Welcome")
    new_window.geometry("540x300")
    new_window.configure(bg="Teal")
    Label(new_window, text="Welcome to our community", bg="Teal", fg="white", font="Arial 15 bold").pack(pady=20)
    photo_welcome = PhotoImage(file = "F:ROS\\Tkinter for GUI\\R.gif" )
    label4 = Label(new_window, image=photo_welcome)
    label4.image = photo_welcome  # Keep a reference to the image to prevent garbage collection
    label4.pack()
    label4.place(x=20 , y=50)
# ------------------- Insert photo ---------------------
photo = PhotoImage(file="F:ROS\\Tkinter for GUI\\photo.png" )  # Create a photo.
label2 = Label(pro, image=photo)  # Create a label for the photo.   
label2.pack()                   # Add the label to the window.
label2.place(x=0, y=0)     # Set the position of the label.
# ------------------ Create a label --------------------
label1 = Label(pro, text="LOG IN System", bg="Teal", fg="white", font="Courier 20 bold")  # Create a label.
label1.pack()                   # Add the label to the window.
label1.place(x=120, y=1)     # Set the position of the label.
username = Label(pro , text = "Username" , bg = "Teal" , fg = "white" , font = "Arial 15 bold")
username.pack()
username.place(x=30, y=60)     # Set the position of the entry.
password = Label(pro , text = "Password" , bg = "Teal" , fg = "white" , font = "Arial 15 bold")
password.pack()
password.place(x=30, y=140)     # Set the position of the entry.
version = Label(pro , text= "Version 1.0 @Ziad" , fg= "white" , bg= "grey" , font= " Arial 15 ")
version.pack()
version.place(x= 160 , y= 320)
# ------------------ Create an entry --------------------
username_entry = Entry(pro, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "30")  # Create an entry.
username_entry.pack()                   # Add the entry to the window.  
username_entry.place(x=30, y=100)     # Set the position of the entry.
password_entry = Entry(pro, bg="light yellow", fg="maroon", font="Arial 15 bold" , width= "30")  # Create an entry.
password_entry.pack()                   # Add the entry to the window.  
password_entry.place(x=30, y=175)     # Set the position of the entry.
# ------------------ Create a button ------------------ 
login = Button(pro , text= "Log in" , bg = "maroon" , fg = "white" , font = "Arial 15 bold" , cursor= "hand2" , justify= "center" , width="10" , command= login )
login.pack()
login.place(x=60, y=250)     # Set the position of the entry.
signup = Button(pro , text= "sign up" , bg = "maroon" , fg = "white" , font = "Arial 15 bold" , cursor= "hand2" , justify= "center" , width="10" , command = signup )
signup.pack()
signup.place(x=210, y=250)     # Set the position of the entry.







pro.mainloop()                  # Run the main loop of the window.
