def add_new_item():
    file=open('To-Do.txt','a+',encoding='utf-8')
    userTodo:str=input('Enter Your To Do List : \n').lower()
    file.write(userTodo+'\n')
    file.close()

def read_items():
    file=open('To-Do.txt','r',encoding='utf-8')
    file.seek(0)
    print(file.readlines())
    file.close()


conLooping = True
while conLooping:
    userInput:str=input('do you want to add a new To-Do item? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
    if userInput == 'y':
        add_new_item()
    elif userInput == 'n':
        userInput:str=input('do you want to list your To-Do items ? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
        if userInput == 'y':
            read_items()
    elif userInput == 'exit':
        conLooping=False
    else:
        print('Invalid Input Try again')


