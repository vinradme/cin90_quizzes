#Function to add numbers
def add(a, b):
    c = a + b
    print "The answer is: {0} + {1} = {2}".format(a, b, c) 

#Function to subtract numbers
def subtract(a, b):
    c= a - b
    print "The answer is: {0} - {1} = {2}".format(a, b, c)

#Function to multiply numbers
def multiply(a, b):
    c = a * b
    print "The answer is: {0} * {1} = {2}".format(a, b, c)

#Function to divide numbers
def divide(a, b):
    c = a / b
    print "The answer is: {0} / {1} = {2}".format(a, b, c)

#Function to capture and execute the user's choice
def choice():
    operation = int(raw_input("""Select operation: \n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n Enter choice (1/2/3/4):"""))

    if operation == 1:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        add(float(a), float(b))

    elif operation== 2:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        subtract(float(a), float(b))

    elif operation == 3:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        multiply(float(a), float(b))

    elif operation== 4:
        a= raw_input("Enter the first number: \n")
        b= raw_input("Enter the second number: \n")
        divide(float(a), float(b))
    else:
        print "Please select a valid operation"
        choice()


if __name__ == '__main__':
    choice()   
