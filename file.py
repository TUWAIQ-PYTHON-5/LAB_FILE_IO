while True:
    print("whrite exit to end the program ")

    user_1 = input("Do you want to add a new To-Do item? answer by'y'for yes and'n'for no :")
    if user_1 == "y":
        user_item = input("Please write your new To-Do item here: ")
        to_do = open("to_do.txt", "a+", encoding="utf-8")
        to_do.writelines(f"{user_item}\n")
        to_do.close()

    elif user_1 == "n":
        answer_user = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no.")
        if answer_user == "y":
            to_do = open("to_do.txt", "r", encoding="utf-8")
            answer = to_do.read()
            print(answer)
            to_do.close()
        elif answer_user == "exit":
            break
        else:
            continue
    elif answer_user == "exit":
        print("thank you for using the To-Do program come back again soon")
        
