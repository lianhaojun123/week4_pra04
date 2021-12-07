numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    get_number()
    print(f"The first number is {numbers[0]} ")
    print(f"The second number is {numbers[1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / 5}")
    def_user(usernames)


def get_number():
    for i in range(5):
        number = float(input("numbers: "))
        numbers.append(number)
    return numbers


def def_user(usernames):
    username = input("Enter your names: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
