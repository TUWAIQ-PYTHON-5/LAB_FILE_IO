import os
import shutil


user_awnser = ""


   


    
while user_awnser != "exit":
    user_awnser = input("do you want to add a new To-Do item ? y for yes : n for No : ")
    if user_awnser == "y":
        number_of_task = int(input("please enter number of task that you want add : ?"))
        for i in range(0 , number_of_task):
            file_name =open('example.txt'  , "a+" , encoding="utf-8") 
            file_name.writelines([ input("please enter your task" "\n") , "   TASK YOU HAVE TO DO""\n" ])
            file_name.close()


    elif user_awnser == "n":
        show_user_task= input("do you want to list your To-Do items ? : ")

        if show_user_task == "y":
            file_name = open("example.txt", "r", encoding="utf-8")
            content = file_name.read()
            print("your do lis is :" "\n" , content)
            file_name.close()

        elif show_user_task == "n":
            print("thank you for using the To-Do program, come back again soon")   
            break       
else:

    print("thank you for using the To-Do program, come back again soon")

             

       
    
    

