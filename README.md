# Roll-Dice

## About
- Roll Dice is a program to roll dices specified in a simple and intuitive way.
- Dice are used in many games of chance as a way of picking random numbers on which to bet, and are used in board or role-playing games to determine the number of spaces to move, results of a conflict, etc. 
- The most common type of die is a six-sided cube with the numbers 1-6 placed on the faces. The value of the roll is indicated by the number of "spots" showing on the top. For the six-sided die, opposite faces are arranged to always sum to seven.
- This gives two possible mirror image arrangements in which the numbers 1, 2, and 3 may be arranged in a clockwise or counterclockwise order about a corner.

## Input
- The first input contains **r** which denotes **one rotation of the dice to the right side**
- The next input contains **l** which denotes **one rotation of the dice to the left side**
- The next input contains **u** which denotes **one rotation of the dice to the top or up side**
- The next input contains **d** which denotes **one rotation of the dice to the bottom or down side**
- The next input contains **q** which denotes **quit**

## Output
- It displays the intial outcome of the dice.
- It displays all the outcomes of the dice.
- It displays the outcome of the latest move.
- It displays the latest out come of dice in diagramtically.

## Sample Input
```
Please enter in the following format,
 r -To Roll right Side 
 l - To Roll left Side 
 u - To Roll up Side 
 d -TO Roll down Side 
 q - quit 
Intial dice after shuffling the values : 
enter user input : r
enter user input : l
enter user input : u
enter user input : d
enter user input : s
enter user input : q
```

## Sample Output
```
                         2
                   +-----------+      
                  /|   4      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  5      | /   
                |/          |/         
                +-----------+          
                    3    
                    
                         2
                   +-----------+      
                  /|   6      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 4
        3       | /  5      | /   
                |/          |/         
                +-----------+          
                    1                     
   
                           2
                   +-----------+      
                  /|   4      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  5      | /   
                |/          |/         
                +-----------+          
                    3            
   
                           4
                   +-----------+      
                  /|   5      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  3      | /   
                |/          |/         
                +-----------+          
                    2            
                   
                   
                         2
                   +-----------+      
                  /|   4      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  5      | /   
                |/          |/         
                +-----------+          
                    3            
  
  Entered user input is Invalid,Please enter valid user input
  last obtained pattern is : 
                         2
                   +-----------+      
                  /|   4      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  5      | /   
                |/          |/         
                +-----------+          
                    3            



All the dice's front, back, top, bottom, left and right values are :  [((5, 2), (6, 1), (3, 4)), ((5, 2), (4, 3), (6, 1)), ((3, 4), (5, 2), (6, 1)), ((5, 2), (4, 3), (6, 1)), ((5, 2), (4, 3), (6, 1))]
latest position values: ((5, 2), (4, 3), (6, 1))
latest position:                          2
                   +-----------+      
                  /|   4      /|   
                 / |         / |      
                +--+--------+  +      
                |  /        |  / 1
        6       | /  5      | /   
                |/          |/         
                +-----------+          
                    3            
```               


#### Contributors
[Uday Kiran Boyapati](https://github.com/udaykiran-boyapati), [RaviKiran Reddy Kaatasani](https://github.com/ravikiranreddy-kaatasani), [Sathish Kumar Kamshettigari](https://github.com/sathishpatel20276), [Hruday Varma Dantuluri](https://github.com/Hruday-Dantuluri), [Shivani Kotla](https://github.com/shivani1929), [Anvitha Chinthapanti](https://github.com/Anvitha777/python), [Subhan Shaik](https://github.com/Shaik-Subhan) have contributed to this project.
