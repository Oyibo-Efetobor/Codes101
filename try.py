
initial_counter = 0
initial_counter_1 = 0
initial_tries = 0
initial_tries_1 = 0
question_2 = 0
import time
time.sleep(1)
print("guess from numbers 1 to 10")
time.sleep(1)


print()
print("whoever has lesser tries wins!!!!")
print()
time.sleep(1)
print("goodluck")
number = ''
answer = ''
counter = 0
counter_1 = 0
tries = 0
tries_1 = 0
last_try = 0
time.sleep(1)
import random
player1 = input("enter your name player 1: ")
print()
player2 = input("enter your name player 2: ")
print()
print()
while True:
    if question_2 == 50:
        break
        
    while True:
        if player1 == player2:
            print("name already in use")
            print()
            time.sleep(1)
            player2 = input("enter another name player 2: ")
        if player1 != player2:
            break
    print()
    time.sleep(1)
    print("okay",player1)    
    number = int(input("enter a number: "))

    print()
    answer = random.randint(1, 10)
    while True:
        while True:
            if number > answer:
                time.sleep(1)
                print("the answer is less")
                print()
                tries += 1
                
                break
            elif number < answer:
                time.sleep(1)
                print("the answer is more")
                print()
                tries += 1
                break
            else:
                tries += 1
                print("correct")
                print ()
                
                print ( "|"," ","|"," ","||"," ","|","","| ")
                print ( "","|","|"," ","|","","|","","|","","| ")
                print ( "","","|","  ","|","","|","","|","","| ")
                print ( "","","|","  ","|","","|","","|","","| ")
                print ( "","","|","   ","||","  ","||"," ")
                print ( "","               "," ")
                print ( "","|"," ","|","","|","","|","","|",""," ")
                print ( "","|","|","|","","|","","||","|",""," ")
                print ( "","||","||","","|","","|","||",""," ")
                print ( "","|"," ","|","","|","","|","","|",""," ")
                print ( ""*20 )
                
                counter += 1
                break
        if counter >= 1:
            break
        
       
        number = int(input("enter a number: "))
    print()
    answer = random.randint(1, 10)
    time.sleep(1)
    print("okay",player2)
    while True:
        while True:
            
            number = int(input("enter a number: "))
            
            if number > answer:
                time.sleep(1)
                print("the answer is less")
                print()
                tries_1 += 1
                break
            elif number < answer:
                time.sleep(1)
                print("the answer is more")
                print()
                tries_1 += 1
                break
            else:
                tries_1 += 1
                print("correct")
                print ()
                
                print ( "|"," ","|"," ","||"," ","|","","| ")
                print ( "","|","|"," ","|","","|","","|","","| ")
                print ( "","","|","  ","|","","|","","|","","| ")
                print ( "","","|","  ","|","","|","","|","","| ")
                print ( "","","|","   ","||","  ","||"," ")
                print ( "","               "," ")
                print ( "","|"," ","|","","|","","|","","|",""," ")
                print ( "","|","|","|","","|","","||","|",""," ")
                print ( "","||","||","","|","","|","||",""," ")
                print ( "","|"," ","|","","|","","|","","|",""," ")
                print ( ""*20 )
                
                counter_1 += 1
                break
        if counter_1 >= 1:
            break
        
        
    print()
    print()
    if tries > tries_1:
        print(player2,"wins!!!!")
    elif tries == tries_1:
        print("it's a tie")
    else:
        print(player1,"wins!!!!")
    time.sleep(1)
    print()
    time.sleep(1)
    question = input("do you wish to play again?\nif yes enter 'y' if no enter 'n': ")
    if question == "y":
        question_2 += 1
        counter = initial_counter
        counter_1 = initial_counter_1
        tries = initial_tries
        tries_1 = initial_tries_1
    else:
        exit(0)
       
    
        















    
