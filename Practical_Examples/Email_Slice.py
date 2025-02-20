#  Email slice 
thename  = input("Enter your name : ").strip().capitalize()
email = input("Enter your email : ").strip().capitalize()

if email.find("@") != -1:                   # if email.find("@") != -1:  is same as if "@" in email
    theusername = email[:email.index("@")]
    thewebsite = email[email.index("@"):]
    print(f" Hello {thename}  \n email is {email}")
    print(f" Your user name is {theusername} \n Your website is {thewebsite}")
else :
    print("Invalid email")
