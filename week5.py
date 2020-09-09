num1 = int(input("\n\nEnter first number: "))
num2 = int(input("Enter second number: "))

list = []
odd = 0
even = 0


if num1 < num2:  # **CHECK IF NUM 1 > NUM2

    print(f"\nThe numbers between {num1} and {num2} are:")

    for i in range(num1, num2 + 1):

        list.append(i)

    print(*list, sep=", ")

    for i in set(list):  # **GET THE ODD AND EVEN NUMBERS IN THE LIST

        if i % 2:
            odd += 1

        else:
            even += 1

    print(
        f"\nThere are {even} even numbers and {odd} odd numbers between {num1} and {num2}")


elif num1 > num2:   # **IF NUM 1 > NUM 2 READ IN REVERSE

    print(f"\nThe numbers between {num1} and {num2} are:")

    for i in reversed(range(num2, num1 + 1)):

        list.append(i)

    print(*list, sep=", ")

    for i in set(list):  # **GET THE ODD AND EVEN NUMBERS IN THE LIST

        if i % 2:
            odd += 1

        else:
            even += 1

    print(
        f"\nThere are {even} even numbers and {odd} odd numbers between {num1} and {num2}")
