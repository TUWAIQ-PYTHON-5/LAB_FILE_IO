

while True:
    print("whrite exit to end the program ")

    user_answer = input("Do you want to add a new To-Do item? answer by'y'for yes and'n'for no :")
    if user_answer == "y":
        user_item = input("Please write your new To-Do item here: ")
        to_do = open("to_do.txt", "a+", encoding="utf-8")
        to_do.writelines(f"{user_item}\n")
        to_do.close()

    elif user_answer == "n":
        user_answer2 = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no.")
        if user_answer2 == "y":
            to_do = open("to_do.txt", "r", encoding="utf-8")
            answer = to_do.read()
            print(answer)
            to_do.close()
        elif user_answer2 == "exit":
            break
        else:
            continue
    elif user_answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
