


ueser_question = input("Do you want to add a new To-Do item ? please answer by Yes or No :")

user_response_1 =['yes']
user_response_2 =['no']
user_response_3 =['exit']

while ueser_question !="exit" :
    if ueser_question.lower() in user_response_1 :
        type_in_to_do_item = input("what you want to type in your new To-Do item ?")
        type_in_to_do_i = type_in_to_do_item +"\n"
        file = open("To_do_item.txt", "a", encoding="utf-8")
        file.write(type_in_to_do_i) 
        file.close()
        ueser_question = input("Do you want to add a new To-Do item ? please answer by Yes or No :")
    elif ueser_question.lower() in user_response_2 :
        ueser_question = input ("do you want to list your To-Do items ?")
        if ueser_question.lower() in user_response_1 :
            file_read = open("To_do_item.txt", "r+", encoding="utf-8")
            print("Your To do list content is :")
            print(file_read.read())
            print()
            ueser_question = input("Do you want to add a new To-Do item ? please answer by Yes or No :")
else :
    print("thank you for using the To-Do program, come back again soon")
    breakpoint