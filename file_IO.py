import os

while True:
    print("type exit if you want close the program")
    userInput = input("Do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no. ")
    if userInput == "y":
        newItem = input("Please type in your new To-Do item: ")
        to_do_file = open("to_do.txt", "a+", encoding="utf-8")
        to_do_file.write(f"{newItem}\n")
        to_do_file.close()
    elif userInput == "n":
        listTheItems = input("Do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no. ")
        if listTheItems == "y":
            to_do_file = open("to_do.txt", "r", encoding="utf-8")
            content_to_do = to_do_file.read()
            print(content_to_do)
            to_do_file.close()
        elif listTheItems == "exit":
            break
        else:
            continue
    elif userInput == "exit":
        break
    else:
        print("Please answer with y/n")