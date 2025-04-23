''' Password manager '''
''' IN terminal , pip install cryptography'''
from cryptography.fernet import Fernet

# def write_key():
#     key= Fernet.generate_key()
#     with open ("key.key","wb") as f:
#         f.write(key)
# write_key()

def load_key():
    with open ("key.key","rb") as f:
        data=f.read()
    return data

master_pwd = input("What is the master password: ")
key=load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username,psw=data.split("|")
            print(f"Username: {username}  Password: {fer.decrypt(psw.encode()).decode()}")

def add():
    user=input("Enter username: ")
    pwd=input("Enter password: ")

    with open("passwords.txt","a") as f:
        f.write(f"{user} | {fer.encrypt(pwd.encode()).decode()}\n")

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