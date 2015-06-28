def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n - 2)

list_of_numbers = range(1,10)
fib_sequence = []

for number in list_of_numbers:
    fib_sequence.append(fibonacci(number))


print fib_sequence