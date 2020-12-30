#Random is a built-in module that can be used to make random numbers.
import random
#In a dice,every number has its own opposite number
values=[[1,6],[2,5],[3,4]]
#for loop to shuffle numbers of a nested list
for value in values:
    random.shuffle(value)
#To shuffle the lists inside the list
random.shuffle(values)
#Assigning the values
front=values[0][0]
back=values[0][1]
top=values[1][0]
bottom=values[1][1]
left=values[2][0]
right=values[2][1]
dice_list=[]
print("Please enter in the following format,\n r -To Roll right Side \n l - To Roll left Side \n u - To Roll up Side \n d -TO Roll down Side \n q - quit ")
print("Intial dice after shuffling the values : ")
while(True):
    #To print the cube
    output = '''                         {0}
                   +-----------+      
                  /|   {1}      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / {2}
        {3}       | /  {4}      | /   
                |/          |/         
                +-----------+          
                    {5}            '''.format(back, top, right, left, front, bottom)

    print(output)
    #Taking user input to rotate a cube in desired direction
    user_input=input("enter user input : ")
    #converting the user input to lower and removing spaces
    user_input = user_input.strip().lower()
    #'q'-->quit
    if user_input == 'q':
        break
    #'r'-->rotate cube towards right
    elif user_input == 'r':
        tempright=right
        right= top
        top = left
        left= bottom
        bottom= tempright
    #'l'-->rotate cube towards left
    elif user_input == 'l':
        templeft = left
        left = top
        top = right
        right = bottom
        bottom = templeft
    #'u'-->rotate the cube up
    elif user_input == 'u':
        tempfront = front
        front = bottom
        bottom = back
        back = top
        top = tempfront
    #'d'-->rotate the cube down
    elif user_input == 'd':
        tempfront = front
        front = top
        top = back
        back = bottom
        bottom = tempfront
    #Prints if user input is invalid
    else:
        print("Entered user input is Invalid,Please enter valid user input")
        print("last obtained pattern is : ")
    tup_values = ((front,back),(top,bottom),(left,right))
    dice_list.append(tup_values)
#prints all actions given by user
print("All the dice's front, back, top, bottom, left and right values are : ",dice_list)
#last position of cube
print("latest position values:",tup_values)
print("latest position:",output)
