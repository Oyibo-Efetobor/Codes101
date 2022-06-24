#JESUS IS LORD
#follow my instagram @tobor._

# To find the roots of a quadratic equation using Almighty Formula
def find_roots():
    a = int(input("input value a ; "))
    b = int(input("input value b ; "))
    c = int(input("input value c ; "))

    n1 = ( -b )
    n2 = (( b**2 ) - ( 4 * a * c ))
    n3 = ( n2 ** 0.5 )

    first = (( n1 + n3) // ( 2 * a))
    second = (( n1 - n3) // ( 2 * a))
    print ()
    print ( " the first answer is = " , first )
    print ( " the second answer is = " , second )
find_roots()


   
