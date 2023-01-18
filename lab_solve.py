user_inputt = input("Do you want to add a new To-Do item? Answer by y for yes and n for no : \n")
yes_choices = ['y']
no_choices = ['n']
exit_choices = ['exit']

while user_inputt !='exit':

    if user_inputt.lower() in yes_choices:

        file_write = open("to_do.txt", "a", encoding="utf-8")
        user_write = input("Type what you want to do : ")
        file_write.write(user_write + "/n")
        file_write.close()
        user_inputt = input("Do you want to add a new To-Do item? Aanswer by y for yes and n for no : \n")

    elif user_inputt.lower() in no_choices:

        user_inputt = input("Do you want to list your To-Do items ? Answer y for yes and n for no : \n")

        if user_inputt.lower() in yes_choices:

            file_read = open("to_do.txt", "r", encoding="utf-8")
            content = file_read.readlines()
            print("content of to_do.txt is : ", content)
            file_read.close()
            user_inputt = input("Do you want to add a new To-Do item? Answer by y for yes and n for no : \n")

    else:
        print("Thank you for using the To-Do program, come back again soon")
        breakpoint()