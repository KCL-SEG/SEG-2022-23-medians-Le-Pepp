"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


if len(numbers) % 2 != 0:
    print(f'The median of the list is {numbers[len(numbers)//2]}')
else:
    x = len(numbers)//2
    print(f'The median of the list is {(numbers[x] + numbers[x - 1])/2}')
