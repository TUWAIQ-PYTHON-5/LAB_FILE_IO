conLooping = True
while conLooping:
    userInput:str=input('do you want to add a new To-Do item? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()

    if userInput == 'y':
        file=open('To-Do.txt','a+',encoding='utf-8')
        userTodo:str=input('Enter Your To Do List : \n').lower()
        file.write(userTodo+'\n')
        file.close()
    elif userInput == 'n':
        userInput:str=input('do you want to list your To-Do items ? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
        if userInput == 'y':
            file=open('To-Do.txt','r',encoding='utf-8')
            file.seek(0)
            print(file.readlines())
            file.close()
    elif userInput == 'exit':
            conLooping=False
            
