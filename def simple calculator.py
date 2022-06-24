# JESUS IS LORD
#follow my instagram @tobor._

# A simple calculator
value = 0
import time
def calculator(value):
    print("This is s calculator used to 'ADD', 'SUBTRACT', 'MULTIPLY' and 'DIVIDE'")
    time.sleep(1)
    number = int(input("enter first number : "))
    time.sleep(1)

    while True:
        q = input("if you wish to ADD enter 'a'\nif you wish to subtract enter 's'\nif you wish to multiply enter 'm'\nif you wish to divide enter 'd'\nenter:  ")
        if q == 'a':
            break
        if q == 'm':
            break
        if q == 'd':
            break
        if q == 's':
            break
        else:
            print("operator doesn't exist!!!")
            print()
        
    number_1 = int(input("enter the second number: "))
    print()
    if q == 'a':
        value = number + number_1
    elif q == 's':
        value = number - number_1
    elif q == 'm':
        value = number * number_1
    elif q == 'd':
        value = number / number_1
    return value
time.sleep(1)
print("the answer is: ", calculator(value))
