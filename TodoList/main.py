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
           

       
    
    

