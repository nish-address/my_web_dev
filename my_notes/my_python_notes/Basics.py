def loop():
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("Done with loop")


# check the odd numbers in a range:
def oddloop():
    starting_number = 1
    max_limit = float(input("Enter max limit: "))
    while starting_number <= max_limit:
        print(starting_number)
        starting_number += 2

        print("Action completed")


# table of 3 not complete
def table3():
    c = 1
    maxi = float(input("Enter the table times: "))
    while c <= maxi:
        print("3 * " + str(c) + " = " + str(3 * c))
        c += 1

        print("Here is a table of 3")


def list_Function():
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    friends = ["Kevin", "karen", "Jim", "Oscar", "Toby"]

    print(friends)


# friends.extend(lucky_numbers)
# friends.append("Creed")

def grade_calculator():
    score = float(input("Enter your score: "))
    if score >= 90 and score <= 100:
        print("Grade : A")
    elif score >= 80 and score < 90:
        print("Grade : B")
    elif score >= 70 and score < 80:
        print("Grade : C")
    elif score >= 60 and score < 70:
        print("Grade : D")
    else:
        print("Grade : F")


# if 90 <= score <=100 : also a method


def basic_odd_even():
    x = int(input("What's x? "))
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def main1():
    '''
def is_even1(n):
    return True if n % 2 == 0 else False

def is_even2(n):
    return n % 2 == 0 '''


def mainodd():
    x = int(input("What's x? "))
    if is_odd(x):
        print("Odd")
    else:
        print("Even")


def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False





def lesson1():
    while True:
        try:
            x = float(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break

    print(f"x is {x}")
