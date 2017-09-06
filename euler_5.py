print("Project Euler Question 5: Smallest multiple\n\n")


def checknum(number):
    return try_num % 3 == 0 and try_num % 4 == 0 and try_num % 7 == 0 and try_num % 8 == 0 and try_num % 9 == 0 \
           and try_num % 11 == 0 and try_num % 13 == 0 and try_num % 16 == 0 and try_num % 17 == 0 and try_num % 19 == 0 and try_num % 20 == 0


try_num = 40
switch = False

while switch is not True:
    if checknum(try_num):
        print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", try_num)
        switch = True
    else:
        try_num += 20
