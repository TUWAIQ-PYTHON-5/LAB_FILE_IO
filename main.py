
userResponse = input("do you want to add a new To-Do item?(y/n/exit): ")
while userResponse != "exit" :
    if userResponse == "y" :
        toDoListItems = input("Enter a new To Do item: ")
        file = open("to_do.txt", "a", encoding="utf-8")
        content = file.write(toDoListItems + "\n")
        file.close()
    elif userResponse == "n" :
        repeatToDoList = input("do you want to list your To-Do items?(y/n): ")
        if repeatToDoList == "y" :
            file = open("to_do.txt", "r", encoding="utf-8")
            content = file.readlines()
            for item in content :
                print(item ,end="")
            file.close()
    userResponse = input("do you want to add a new To-Do item?(y/n/exit): ")
else :
    print("thank you for using the To-Do program, come back again soon")



