from math import sqrt


def practice():
    print(" Hello World ")
    character_name = "John"
    character_age = "75"
    print("I once knew a man named " + character_name + ", ")
    print("He liked the name " + character_name + ", but he didn't like the fact that he was " + character_age + ". ")
    print(3 * 3)
    box_height = 100
    box_length = 20
    print(box_length * box_height)
    my_num = 12
    print(my_num / 3)
    num1 = input("Enter a number:")
    num2 = input("Enter another number:")

    name = (input("Enter your name:"))
    print("Hello " + name + "!")
    print("How are you?")
    being = (input(""))
    print("That's good!")

    print("Funtions")


def intro():
    print(3 * 5)
    print(3 * (2 + 2))
    my_num = 12
    print(my_num / 3)
    print(str(my_num) + " is a bad number. ")
    print(sqrt(16))
    print(abs(-3))
    print(pow(4, 2))
    print(max(3, 1))
    print(min(3, 1))
    print(round(1.234))
    # Important : from math import *

    name = input("Enter your name:")
    print("Hello " + name + "!")

    num1 = input("Enter a number:")
    num2 = input("Enter another number:")
    addition = float(num1) + float(num2)
    subtraction = float(num1) - float(num2)
    multiplication = float(num1) * float(num2)
    division = float(num1) / float(num2)


def say_hi():
    print("Hello User")


def say_hello(name, age):
    print("Hello " + name + ", you are " + age)

    say_hello("Mike", "35")
    say_hello("Steve", "70")


def cube(num):
    return num * num * num

    result = cube(3)
    print(result)


def basic_calculator():
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) + float(num2)
    print(result)


def madlibs_game():
    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")
    print("Roses are " + color)
    print(plural_noun + " are blue")
    print("I love " + celebrity)


def list():
    friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
    print(friends)
    print(friends[0])
    print(friends[-1])
    print(friends[1:])
    print(friends[1:3])
    friends[0] = "Mike"
    print(friends[0])


def square():
    my_num = input("Enter a number: ")
    my_result = (pow(float(my_num), 2))
    print(my_result)


def max_value():
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(max(float(num1), float(num2)))


def cube():
    num = input("Enter a number: ")
    print(pow(float(num), 3))


def mad_libs():
    character_name = input("Enter a character name: ")
    character_age = input("Enter the age: ")
    color = input("Enter his favorite colour: ")
    print("There once was a man named " + character_name + ", ")
    print("He was " + character_age + ". ")
    print("His favorite colour was " + color + ". ")


def If_statement():
    is_male = True
    is_tall = True

    if is_male and is_tall:
        print("You are a tall male")
    elif is_male and not (is_tall):
        print("You are a short male")
    elif not (is_male) and is_tall:
        print("You are not a male but are tall")
    else:
        print("You are not a male and not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

    print(max_num(3, 4, 5))


def second_calculator():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator")


def personal_info():
    your_name = input("Enter your name: ")
    your_age = input("Enter your age: ")
    your_favorite_color = input("Enter your favorite color: ")
    print("You are " + your_name + ". ")
    print("You are " + your_age + ". ")
    print("Your favorite color is " + your_favorite_color + ". ")
    print("See I know everything about you. ")




# GRADE TELLER:
def gradeteller():
    x = float(input("Enter your grade: "))
    if 100 >= x >= 90:
        print("Grade : A ")
    elif 90 >= x >= 80:
        print("Grade: B ")
    elif 80 >= x >= 70:
        print("Grade: C ")
    elif 70 >= x >= 60:
        print("Grade: D ")
    else:
        print("Grade: F ")

       