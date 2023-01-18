'''

    Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
    If the user answers yes ,
         then ask the user to type in his new To-Do item . 
            Then save that To-Do item inside the a file to_do.txt on a new line.
    If the user answers no, 
        then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
    If the user answers yes for reading his To-Do list , 
        then print a list of the To-Do items one item per line.
    Then return again to ther first question and ask again, 
        you coninue this untill the user types in "exit" , 
            then you exit the program. and print to the user "thank you for using the To-Do program, 
                come back again soon"

'''
flag = True
while flag:

        show_msg =  input("do you want to add a new To-Do item ? y / n  or exit to close : ")
        if show_msg == "y":
            print("-------------------------")
            new_to_do = input("type in new To-Do item : ")
            file = open('to_do.txt', 'a+' , encoding='utf-8')
            file.write(new_to_do+'\n')
            file.close()

        elif show_msg == "n":
             print("-------------------------")
             show_list = input("do you want to list your To-Do items ?  : ")
             print("-------------------------")
             if show_list == 'y':
                files = open('to_do.txt' , 'r', encoding='utf-8') 
                print(files.read())
                print("-------------------------")
                files.close()

        elif show_msg == "exit":
                flag = False
                print("thank you for using the To-Do program, come back again soon")
                print("-------------------------")
        
        

            


        

   