def user_information(ussnm, pssd):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    ussnm_ = ussnm+ "task.txt"

    f = open(ussnm_, "a")
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write("\nAddress: ")
    f.write(address)
    f.write("\nAge: ")
    f.write(age)
    f.write("\n")
    f.close()

def signup():
    print("Please Enter the username by which you wanna access you acount")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    user_information(username, password)



