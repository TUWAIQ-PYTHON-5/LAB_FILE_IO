def add_new_item(userInput:str):
    file=open('To-Do.txt','a+',encoding='utf-8')
    userTodo:str=input('Enter Your To Do List : \n').lower()
    file.write(userTodo+'\n')
    file.close()
    return file
    #userInput:str=input('do you want to add a new To-Do item? \"y\" for yes and \"n\" for no. or exit to cloes : ').lower()
    #return userInput

def user_input_no(userInput:str):
    file=open('To-Do.txt','r',encoding='utf-8')
    file.seek(0)
    print(file.readlines())
    file.close()
