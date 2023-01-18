

#file= open("to_do.txt","w"")

user_aswere=input("Do you want to add a new To-Do item? Enter y for yes and n for no : " )

while user_aswere== "y":
    file= open("to_do.txt","a")
    to_do_list=input("TYPE YOUR TO DO ITEM :")  
    file.writelines(to_do_list+'\n')
    if to_do_list=="":
        file.close()
        print ("thank you for using the To-Do program, come back again soon")
        break
        
   
       


user_aswere2= input("Do you want to list your To-Do items ? answer y for yes and n for no :")
while user_aswere2=="y":
     file= open("to_do.txt","r")
     content=file.readlines()
     print(content)
     break
     if user_aswere2=="n":   
       user_aswere=input("Do you want to add a new To-Do item? Enter y for yes and n for no : " )

 

       
       

