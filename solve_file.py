

while True:
    print("exit to end ")
    user_answers = input("Do you want to add a new To-Do item? (y/n) or exit to end:  ")
    if user_answers == "y":
        user_item = input("Please type in your new To-Do item: ")
        to_do = open("to_do.txt", "a+", encoding="utf-8")
        to_do.write(f"{user_item}")
        to_do.close()
    elif user_answers == "n":
        user_answers2 = input("please add the new item , or exit to end ? : ")
        if user_answers2 == "y":
            to_do = open("to_do.txt", "r", encoding="utf-8")
            answer = to_do.read()
            print(answer)
            to_do.close()
        elif user_answers2 == "exit":
            break
        else:
            continue
    elif user_answers == "exit":
        break
    else:
        print("your answer must be (y/n/exit)")
