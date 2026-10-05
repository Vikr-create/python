def largest(*number):
    maximum = number[0]

    for numbers in number:
        if numbers > maximum:
            maximum = numbers

    print("Largest number:", maximum)


largest(10, 20, 30, 40)