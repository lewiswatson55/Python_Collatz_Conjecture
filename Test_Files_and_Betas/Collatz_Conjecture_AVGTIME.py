#Collatz Conjecture Program
#Created by Lewis Watson (aka Wo)
#This is for testing the average time taken to work down to 1 from any number. 

from time import clock
it_count = 0
n = 0

def Calculate(n):
    global it_count
    it_count = 0

    start = clock()
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            #print (n) #Prints All Numbers (Slows Program Speed)
            it_count += 1
        else:
            n = (n//2)
            #print (n) #Prints All Numbers (Slows Program Speed)
            it_count += 1

    end = clock()
    return format(end-start, ".10f")


def loop(number):
    avgtime = 0
    for x in range(0, number):
        time = Calculate(179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368);
        avgtime = float(avgtime) + float(time)
        
    print (avgtime/number)
        
        
    


