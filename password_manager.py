''' Password manager '''

pwd=input("What is the master password: ")

while True:
    mode = input("\nEnter add or view to add/view passwords and q to quit: ").lower()
    if mode=="q":
        break
    if mode=="view":
        pass
    elif mode=="add":
        pass
    else:
        print("Invalid Input!\nTry Again")