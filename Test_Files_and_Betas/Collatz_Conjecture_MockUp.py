#Collatz Conjecture Program MockUp
#Created by Lewis Watson
#Just saving this here incase I need to debug stuff.


def Select_Number():
    n = int(input("Select the number you wish to calculate? "))
    return n

def Calculate():
    n = Select_Number();

    while n != 1:
        n = (n-1)
        print (n)

    print ("The number has reached 1")

Calculate();

