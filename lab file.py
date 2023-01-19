
#file= open("to_do.txt","w"")

print("welcome to our program to exit type exit:")
while True:
  user_aswere=input("Do you want to add a new To-Do item? Enter y for yes and n for no or type exit to exit : " )
  if user_aswere== "y":
     to_do_list=input("TYPE YOUR TO DO ITEM :") 
     file= open("to_do.txt","a")
     file.writelines(to_do_list+'\n')
     file.close()
  elif user_aswere=="no" :     
   user_aswere_2= input("Do you want to list your To-Do items ? answer y for yes and n for no :")     
   if user_aswere_2=="y":
      file= open("to_do.txt","r") 
      content=file.readlines()
      for item in content:
        print(item)
      file.close()
 
  elif user_aswere=="exit":
    break

print ("thank you for using the To-Do program, come back again soon")





