
my_list = ['John', 'Toby', 'Rody', 'Jules']
print(my_list[0])
print(my_list[-1])

def list_sorting():
    list = ["ken", "Jim"]
    print(sorted(list))

def add_items_to_list():
    mylist = list()
    mylist.append("Apple")
    print(mylist)


def check_items():
    mylist = ["Apple", "Banana"]
    if "Banana" in mylist:
        print("yes")
    else:
        print("No")


def sclicing_list():
    mylist = [1, 2, 3, 4, 5, 6, 7]
    a = mylist[1:4]
    print(a)

# if you don't mention the end index
# it's going to continue till the end

def step_index():
    mylist = [1, 2, 3, 4, 5, 6, 7]
    a = mylist[::2]
    print(a)


# It's gonna jump one number

def list_comprehension():
    list = [1, 2, 3]
    new_list = [i * i for i in list]
    print(new_list)


# creating a new list with variations

def list_of_numbers_less_than():
    n = 3
    list = [i for i in range(n) if i >= 0]
    print(list)

    # Tuples#


def unpacking_tuples():
    my_tuple = ("Nish", 20, "Hobart")
    name, age, city = my_tuple
    print(name)
    print(age)
    print(city)


def tuples_item_assignment():
    my_tuple = (1, 2, 3, 4, 5, 6)
    a, *b, c = my_tuple
    print(a)
    print(b)
    print(c)


# the * assigns all elements in between #
# to make a list so b = [2,3,4,5] #
