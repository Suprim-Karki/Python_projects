''' Password manager '''

pwd=input("What is the master password: ")

def view():
    with open("passwords.txt","r") as f:
        f.read

def add():
    user=input("Enter username: ")
    pwd=input("Enter password: ")

    with open("passwords.txt","a") as f:
        f.write(f"{user} | {pwd}\n")

while True:
    mode = input("\nEnter add or view to add/view passwords and q to quit: ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid Input!\nTry Again")