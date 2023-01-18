
usrAnswer:str=""

while (usrAnswer != "exit"):
    print("Do you want to add a new To-Do List?")
    usrAnswer= input("Answer by ""[y]"" for yes and ""[n]"" for no. \n")
    if (usrAnswer == "y"):
        usrItem=input("Type What you want to do: ")
        usrFile = open('to_do.txt', "a", encoding="utf-8")
        usrFile.writelines(usrItem+"\n")
        usrFile.close()

    elif (usrAnswer == "n"):
        print("Do you want to list your To-Do items?")
        follAnswer:str = input("Answer by ""[y]"" for yes and ""[n]"" for no.\n")
        if (follAnswer == "y"):
            usrFile = open('to_do.txt', "r", encoding="utf-8")
            print(usrFile.read())
            usrFile.close()
else: print("Thank you for using the To-Do program, come back again soon")

