def user_information(ussnm, pssd):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    ussnm_ = ussnm+ " task.txt"

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
    print("Your account has been created successfully, please login to continue")
    login()

def login():
    print("Please Enter the username by which you wanna logIn you acount")
    user_nm = input("Enter Username: ")
    pssd_wr = (input("enter the password: "))+'\n'
    try:
        usernm = user_nm + " task.txt"
        f_ = open(usernm, "r")
        k = f_.readlines(0)[0]
        f_.close()

        if pssd_wr == k:
            print(
                "1--to view your data \n2--To add task \n3--Update\
                task status \n4--View task status")
            a = input()

            switcher = {
                1: view_data(usernm),
                2: add_task(usernm),
                3: update_task(user_nm),
                4: view_task(user_nm)
            }
        else:
            print("SIR YOUR PASSWORD OR USERNAME IS WRONG , Plz enter Again")
            login()
    except Exception as e:
        print(e)
        login()


def view_data(usernm):
    f_ = open(usernm, "r")
    k = f_.readlines()
    f_.close()
    print(k)

def add_task(usernm):
    f_ = open(usernm, "a")
    task = input("Enter the task you want to add: ")
    f_.write("\n")
    f_.write(task)
    f_.close()

def update_task(usernm):
    f_ = open(usernm, "r")
    k = f_.readlines()
    f_.close()
    print(k)
    task = input("Enter the task you want to update: ")
    f_ = open(usernm, "a")
    f_.write("\n")
    f_.write(task)
    f_.close()

def view_task(usernm):
    f_ = open(usernm, "r")
    k = f_.readlines()
    f_.close()
    print(k)

def main():
    print("1--to login \n2--to signup \n3--to main")
    a = input()
    switcher = {
        1: signup(),
        2: login(),
        3: main()
    }

if __name__ == "__main__":
    main()