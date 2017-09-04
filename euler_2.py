print("Project Euler Question 2: Even Fibonacci Numbers\n\n")

fib1 = 0
fib2 = 1
fib_hold = 0
result = 0
count = 0

while (fib_hold < 4000000):

    fib_hold = fib1 + fib2
    fib1 = fib2
    fib2 = fib_hold
    count += 1

    if (fib_hold%2 == 0):
        result += fib_hold
    
print("The sum of the even-valued Fibonacci numbers less than 4 million is:", result)
print("\n\nSummed up to the", count, end='th' " term")
