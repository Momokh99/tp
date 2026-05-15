def authentification(usr:str,pas:str):
    if usr == REAL_usr and pas == REAL_pass:
        return 1
    return 0


username = input("enter your user name")
password = input("enter your password")

while username == "":
    print("")
    username = input("enter your user name")
while password == "":
    print("")
    password = input("enter your password")

REAL_pass = "azerty"
REAL_usr = "moha"

auth =  authentification(username,password)
if auth == 1:
    print("succeded")
else:
    print("failed")