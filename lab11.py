


file = open("To-Do.txt","a+",encoding="utf-8")

while True:
    user=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no or write 'exit' to end: ")
    if user == "y":
        add_words = input(" writ in To-Do for a new item: ")
        file.writelines(add_words)
        file.writelines("\n")
    elif user == "n":
        user2=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no or write 'exit' to end: ")
        if user2 == "y":
         file.seek(0)
         print(file.readline())
        elif user2 == "exit":
            break
    elif user == "exit":
        break


file.close()
print("\n thank you for using the To-Do program, come back again soon")


