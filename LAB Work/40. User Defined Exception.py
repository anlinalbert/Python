# User defined exception

class InvalidLogin(Exception) :
    pass

username = "anlin"
password = "password"

try :
    uname = input("Enter the username: ")
    passw = input("Enter the password: ")

    if username == uname and password == passw :
       pass
    else :
        raise InvalidLogin("Invalid login credentials")
except InvalidLogin as i :
    print("Error :", i)