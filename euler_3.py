print("Project Euler Question 3: Largest prime factor\n\n")


count = 0

super_num = 600851475143

multiply = 1

num = 2

while(multiply != super_num):
    for divisor in range(2, num+1):
        if(num%divisor == 0):
            count += 1
    if(count == 1):
        if(super_num%num == 0):
            multiply *= num
            print(num)
    count = 0
    num += 1
