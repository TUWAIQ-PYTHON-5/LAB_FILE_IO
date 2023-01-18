import os
print(os.getcwd())



def new_item():
    file=open("to-do-list.tx",'a',encoding="utf-8")
    Todolist=input("Enter Your To Do List :").lower()
    file.write(Todolist)
    file.close()

def read_items():
    file=open("to-do-list.txt","r",encoding="utf-8")
    file.seek(0)
    print(file.readlines())
    file.close()


answer = True
while answer:
    userInput=input('do you want to add a new To-Do item? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
    if userInput == 'y':
        new_item()
    elif userInput == 'n':
        userInput=input('do you want to list your To-Do items ? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
        if userInput == 'y':
            read_items()
    elif userInput == 'exit':
        answer=False
    else:
        print("Invalid Input")
    