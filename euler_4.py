print("Project Euler Question 4: Largest palindrome product\n\n")

result = 0


def ispalindrome(string):

    position = -1
    hold_word = ""

    for char in string:
        hold_word += string[position]
        position -= 1

    return string == hold_word

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = num1 * num2

        candidate = str(product)

        if ispalindrome(candidate):
            if int(candidate) > result:
                result = int(candidate)
            else:
                continue
        else:
            continue

print(result)