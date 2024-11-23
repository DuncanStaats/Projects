'''
Name: Duncan Staats
Date:11/22/2024
Assignment: Loop Fun Project
Description: Work with Loops to understand them better
'''

def main():
    # Part 1 - get user input
    while True:
        try:
            height = int(input("Enter a box height (between 3 and 10): "))
            if 3 <= height <= 10:
                break
            print("That number is out of bounds: Try again.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            width = int(input(f"Enter a box width between ({height + 1} and 20): "))
            if height < width <= 20:
                break
            print("That number is out of bounds: Try again.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Part 2a - print numbers
    total = 0
    count = 0

    print(f"\nThe integers from {height} to {width} are:")

    for num in range(height, width + 1 ):
        print(num, end = " ")
        total = num + total
        count = count + 1

    print()

    # Part 2b - calculate and print average of the numbers
    average = total / count

    print(f"\nAnd the average of those numbers is {average:.1f}.\n")

    # Part 3 - print the hollow box
    print("*" * width)
    
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    print("*" * width)

    print()

    # Part 4 - print the triangular shape
    for row in range(1, height + 1):
        for star in range(2 * row):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()# don't change this
