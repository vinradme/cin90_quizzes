#fizzbuzz testing function

name = raw_input("Please enter your name: ")

limit = int(raw_input("Please enter maximum limit for the function: "))

def fizbuzz(name):
    print "Hello {}, how are you ?".format(name)
    for i in range(1,101):
        if i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        elif (i % 3 == 0) and (i % 5 == 0):
            print "FizzBuzz"
        else:
            print "The number {} is not divisible by 3 or 5".format(i)

fizbuzz(name)
    
