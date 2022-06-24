# JESUS IS LORD
# follow my instagram @tobor._
def collatz_conjecture(c, zero): #define the collatz conjecture function
    c0_1 = c + zero
    c0 = int(c0_1)
    counter = 0
    counter_1 = 0 
    while True :
        if c0 % 2 == 0:            #If the number is even it is divided by 2, if it is odd it multiplied by 3 and added to 1
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        counter += 1
        print (c0)
        if c0 == 1:              #The process continues until the answer is 1
            counter_1 += 1
            print()
            return counter
            
print(collatz_conjecture(c = input("enter the 'c' value: "), zero = input("enter the '0' value: ")))
print("steps were taken")
