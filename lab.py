'''
question = input("do you want to add a new To-Do item?")

while question:
    if question == "y":
        print("v")
        break
    elif question=="n":
        print("b")
        break
    else:
        print("")
        break
'''
qustion=input("do you want to add a new To-Do item  :")
while qustion =="y":

 file = open("to_do.txt", "w", encoding="utf-8")
 word=file.write("i love my city")
 file.close()
 print(input("what the type of new To-Do:"))
else:
 while qustion=="n":
    print(input("do you want to list your To-Do items :"))
while qustion =="y":
    print(file.write("i\n love\n my\n city"))
    break
qustion=input("do you want to add a new To-Do item  :")
print(exit)