import os
while True:  
 user_input = input("do you want to add a new To-Do item? ")
 if user_input== 'y':
    file = open("to_do.txt", "w", encoding="utf-8")
    user2=input("Write  your new To-Do item:") 
    file.write(user2)
    file.write("\n")
    file.close()
 elif user_input=='n':
     user_input2=input("do you want to list your To-Do items ?") 
    
 if user_input2=='y':
    user_input2=input("do you want to list your To-Do items ?")
    file = open("to_do.txt", "w", encoding="utf-8")
    list_item=file.read()
    list_item=file.read("\n")
    os.remove("lst_do.txt")
    print("list of to_do.txt is : ",list_item )
    file.close()   
    if user_input=='exit':
     print("thank you for using the To-Do program, come back again soon")
    break 
    


    
      
