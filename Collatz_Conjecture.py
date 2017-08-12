#Collatz Conjecture Program
#Created by Wobble107

def Select_Number():
    n = int(input("Select the number you wish to calculate? "))
    return n

def Calculate():
    n = Select_Number();

    while n != 1:
        if (n % 2 == 0):
            n = (n/2)
            print (str(n) + " (Even)")
        else:
            n = (3*n+1)
            print (str(n) + " (Odd)")

    print ("The number has reached 1")
    print()
    Calculate();

Calculate();


