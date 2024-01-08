import os
import time
from colorama import Fore, Style
from tools.numbers.comp import sumofdigits, ispal
from tools.numbers.simp import add_numbers, subtract_numbers
from tools.col import myzip

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def main():
    simp_called = False  # Flag to track if a function in simp module is called
    
    while True:
        print("\nChoose a function to use:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Sum of digits")
        print("4. Check if a number is a palindrome")
        print("5. Zip two lists")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"The sum is: {add_numbers(num1, num2)}")
            simp_called = True

        elif choice == '2':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print(f"The difference is: {subtract_numbers(num1, num2)}")
            simp_called = True

        elif choice == '3':
            num = int(input("Enter a number: "))
            print(f"The sum of digits is: {sumofdigits(num)}")
            simp_called = True

        elif choice == '4':
            num = int(input("Enter a number: "))
            if ispal(num):
                print(f"{num} is a palindrome.")
            else:
                print(f"{num} is not a palindrome.")
            simp_called = True

        elif choice == '5':
            list1 = input("Enter the first list (comma-separated): ").split(',')
            list2 = input("Enter the second list (comma-separated): ").split(',')
            print(f"The zipped list is: {myzip(list1, list2)}")
            simp_called = True

        elif choice == '6':
            if not simp_called:  # Check if a function in simp module was called
                raise Exception("Cannot call functions in comp module without calling at least one function in simp module.")

            print("Exiting...")
            countdown(3)
            break

        else:
            clear_screen()
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6." + Style.RESET_ALL)
            countdown(3)
            clear_screen()

        cont = input("\nDo you wish to continue? (yes/no): ")
        if cont.lower() != 'yes':
            print("Exiting...")
            countdown(3)
            break

if __name__ == "__main__":
    clear_screen()
    main()
