print("Project Euler Question 6: Sum square difference\n\n")


def sumofsquare(a, b):
    return sum(i**2 for i in range(a, b))


def squareofsum(m, n):
    return sum(i for i in range(m, n))**2


print(squareofsum(1, 101) - sumofsquare(1, 101))