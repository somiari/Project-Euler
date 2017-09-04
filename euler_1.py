print("Project Euler Question 1: Multiples of 3 and 5\n\n")

hold_sum = 0

for num in range(1, 1000):
    if num%3 == 0 or num%5 == 0:
        hold_sum += num

print("The sum of all the multiples of 3 or 5 below 1000 is", hold_sum)
