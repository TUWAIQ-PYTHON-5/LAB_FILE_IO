import os
the_awnser = ""
    
while the_awnser != "exit":
    the_awnser = input("do you want to add a new To-Do item ? ")
    if the_awnser == "y":
        list_items = int(input("please enter number that you want add : ?"))
        for i in range(0 , list_items):
            file_name =open('ToDo.txt'  , "a+" , encoding="utf-8") 
            file_name.writelines([ input("please enter your task" "\n") , "\n" ])
            file_name.close()


    elif the_awnser == "n":
        show_list_items= input("do you want to list your To-Do items ?")

        if show_list_items == "y":
            file_name = open("ToDo.txt", "r", encoding="utf-8")
            content = file_name.read()
            print("your do lis is :" "\n" , content)
            file_name.close()

        elif show_list_items == "n":
            print("thank you for using the To-Do program, come back again soon")
            break       
else:

    print("thank you for using the To-Do program, come back again soon")
