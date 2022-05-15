counter_2 = 0
repeat = 0
counter_3 = 0
while True:
    if counter_2 == 0:
        
        import time
    
        counter = 0
        counter_1 = 0
        question = 0
        name = input("hello human enter your name : ")
        print ()
        print ("hello" , name , "welcome to my guessing game")
        time.sleep(1)
        print ()
        print ("you have to guess between the numbers 1 to 20")
        time.sleep(1)
        print ()
        print ("for there is a hidden CORRECT number")
        time.sleep(1)
        print ()
        print ("you have FIVE tries")
        time.sleep(1)
        print ()
        print ()
        number = int(input("enter a number : "))
        counter += 1

        while True:
            if counter ==4:
                break
            if number == 19:
                break
            else:
                time.sleep(1)
                print ()
                print ("haha you've guessed wrongly   try AGAIN!")
                if number > 19:
                    print ("the answer is less than the number you chose")
                else:
                    print ("the answer is greater than the number you chose")
            counter +=1
            print ()
            number = int(input("enter another number : "))
        if counter < 4:
            time.sleep(1)
        if number == 19:
            print ()
            print (name,"played",counter,"out of five times")
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
            time.sleep(2)
            print()
            print()

        else:
            time.sleep(1)
            print()
            print ("this is your last try" , name )
            if number > 19:
                print ("the answer is less than the number you chose")
            else:
                print ("the answer is greater than the number you chose")
            print ()
            number = int(input("enter the right number or lose! : "))
            if number == 19:
                print()
                print (name,"played",(counter + 1),"out of 5 times")
                time.sleep(1)       
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
        
            else:
                print()
                print ("you have used up all your tries" , name , "you LOSE!!!!!")
        question = input("do you want to play again?, 'yes' or 'no' ")
        if question == "yes":
            print ("okay" , name )
            repeat  += 1
            time.sleep(2)
            print()
            print()
            break
        else:
            repeat += 2
            break
           
for i in range(1):
    i += 2
    if repeat % 2 != 0:
        print ()
        print ()
        number = int(input("enter a number : "))
        counter += 1

        while True:
            if counter_3 ==3:
                break
            if number == 6:
                break
            else:
                time.sleep(1)
                print ()
                print ("haha you've guessed wrongly   try AGAIN!")
                if number > 6:
                    print ("the answer is less than the number you chose")
                else:
                    print ("the answer is greater than the number you chose")
            counter_3 +=1
            print ()
            number = int(input("enter another number : "))
        if counter_3 < 3:
            time.sleep(1)
        if number == 6:
            print ()
            print (name,"played",(counter_3 + 1),"out of five times")
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
            time.sleep(2)
            print()
            print()
            print ("Goodbye" , name )

        else:
            time.sleep(1)
            print()
            print ("this is your last try" , name )
            if number > 6:
                print ("the answer is less than the number you chose")
            else:
                print ("the answer is greater than the number you chose")
            print ()
            number = int(input("enter the right number or lose! : "))
            if number == 6:
                print()
                print (name,"played",(counter_3 + 2),"out of 5 times")
                time.sleep(1)       
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
                print()
                print ("Goodbye" , name )
        
            else:
                print()
                print ("you have used up all your tries" , name , "you LOSE!!!!!")
        break
        
    else:
        print ("Goodbye" , name )
        break





    

