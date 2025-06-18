 # Advanced Python#


def strip_function():
    name = "Eren Yeager"
    name = name.strip("Yeager")
    print(name)










def calculating_time():
    from timeit import default_timer as timer

    start = timer()
    my_string = "Hello"
    for i in my_string:
        print(i)
    stop = timer()
    print(stop - start)

    # Formatting a string#


def method_1():
    var = "Tom"
    var2 = 25
    var3 = 2.5
    my_string = "Hello %s" % var
    my_string2 = "the number is %d" % var2
    my_string3 = "the number is %f" % var3
    # %s for string, %d for decimal
    # and %f for float
    print(my_string)
    print(my_string2)
    print(my_string3)


def method_2():
    var = "Tom"
    var2 = 25
    my_string = "{} is {} years old".format(var, var2)
    print(my_string)
    # use {:.xf} to get only x digits}


def best_method():
    var = "Tom"
    var2 = 25
    var3 = 50.12345678
    my_string = f"{var} is {var2} years old"
    my_string2 = f"He weighs {var3:.2f} kg"
    print(my_string + "\n" + my_string2)
    # use {var:.xf} to get only x digits}


                                #Collections#

def counter():
    from collections import Counter
    string = "aaabbbbccccc"
    my_counter = Counter(string)
    print(my_counter)
    print(type(my_counter))
    print(my_counter.items())
    print(my_counter.keys())
    print(my_counter.values())
    print(my_counter.most_common(1))
    # GIVES US THE MOST COMMON#
    print(my_counter.most_common(2))
    # GIVES US THE 2 MOST COMMON#
    print(my_counter.most_common(1)[0])
    # GIVES US THE MOST COMMON TUPLE INSTEAD OF LIST#
    print(my_counter.most_common(1)[0][0])


# GIVES US THE MOST COMMON ELEMENT#

                                # NAMED_TUPLES#
def named_tuples():
    from collections import namedtuple
    point = namedtuple('point', 'x,y')
    pt = point(1, 2)
    print(pt.x, pt.y)
    print(pt)

                                #ITERTOOLS#

def product():
    from itertools import product
    a = [1, 2]
    b = [3, 4]
    prod = product(a, b)
    print(list(prod))

def product_with_repeat():
    a = [1,2]
    b = [3]
    prod = product(a, b, repeat = 2)
    print(list(prod))

def permutations():
    from itertools import permutations
    a = [1,2,3]
    perm = permutations(a)
    print(list(perm))
    perm_with_2_elements = perm = permutations(a, 2)
    print(list(perm_with_2_elements))
    #Order matters, therefore (1,2) != (2,1)
    #Use length to specify number of elements 2 = (a, b) and 3 = (a, b, c) and so on

def combinations():
    from itertools import combinations
    a = [1, 2, 3]
    comb = combinations(a, 2)
    print(list(comb))
    # Order doesn't matter in combinations so, (1,2) == (2,1)
    # Length is mandatory, here in (a, 2) length = 2

def combinations_with_replacement():
    from itertools import combinations, combinations_with_replacement
    a = [1, 2, 3]
    comb = combinations_with_replacement(a, 2)
    print(list(comb))
    # Combination_with_replacement has (1,1) (2,2) (3,3) (4,4) meaning repitition of elements

def accumulation():
    from itertools import accumulate
    import operator
    a = [1,2,3,4]
    acc_add = accumulate(a)
    acc_multiply = accumulate(a, func=operator.mul)
    acc_subtract = accumulate(a, func=operator.sub)
    print(list(acc_add))
    print(list(acc_multiply))
    print(list(acc_subtract))

def groupby():
    from itertools import groupby
    a = [1,2,3,4]
    group_obj = groupby(a, key = lambda x: x<3)
    for key, value in group_obj:
        print(key, list(value))


def group_example():
    from itertools import groupby

    persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
               {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

    group_obj = groupby(persons, key=lambda x:x['age'])
    for key, value in group_obj:
        print(key, list(value))

#more itertools are count, cycle and repeat: check the notes for these:

# LAMBDA FUNCTIONS
# lambda aruments: expression
def lambda_func():

    add10 = lambda x:x+10
    print(add10(5))

    mult = lambda x,y: x*y
    print(mult(2,7))

    #to sort a list based off thier sums using sorted list comprehensions
    points2D = [(1,2), (15,1), (5, -1), (10,4)]
    points2D_sorted = sorted(points2D, key=lambda x:x[0] +x[1])
    print(points2D_sorted)

# map(func, seq)
def using_map():
    a = [1,2,3,4]
    b = map(lambda x:x*2, a)
    print(list(b))
    # or you can list comprehension syntax which is way easier
    c = [i*2 for i in a]
    print(c)

# filter(func, sequence)
def using_filter():
    a = [1,2,3,4,5,6]
    b = filter(lambda x: x%2==0, a)
    print(list(b))
    #or you can list comprehension syntax which is way easier
    c = [i for i in a if i%2==0]
    print(c)

#reduce(func, sequence)
#repeatedly applies a functions and returns a single value
def using_reduce():
    from functools import reduce
    a = [1,2,3,4]
    product_a = reduce(lambda x,y: x*y, a)
    print(product_a)
    #In this case it multiplies all elements because we used X*Y

#EXCEPTIONS AND ERRORS

def raising_exception():
    x = -5
    if x<0:
        raise Exception('x should ne positive')

def using_assert():
    y = -1
    assert(y>=0), 'y is not positive'

def error_handling():
    try:
        a = float(input("Enter a number: "))
        b = 10 / a
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(b)
    finally:
        print("cleaning up...")
#If we use 0 there will be zerodivision error
#If we use string such as "a" ValueError
#else will print the answer
#finally will run always whether there's an exception or not

def defining_errors_with_messages():
    class ValueTooHighError(Exception):
        def __init__(self, message, value):
            self.message = message
            self.value = value

    x = int(input("Enter the value of x: "))
    def test_value(x):
        if x > 100:
            raise ValueTooHighError("is too high", x)

    try:
        test_value(x)
    except ValueTooHighError as e:
        print(e.value, e.message)
