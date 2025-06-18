# Dictionaries#

def tagalog_dictionary():
    Tagalog = {"Hello": "Kumusta ka na",
               "delicious": "Masarap",
               "bye": "kitakits"}
    Tagalog['no problem'] = "walang anuman"
    word = input(str("Enter the word: "))
    item = Tagalog[word]
    print(item)

    # sets: unorderd, no duplicates#


def creating_and_adding_keys():
    mydict = dict(name="Mary", age=27, city='Hobart')
    # dict allows you to not use " with keys#
    mydict["email"] = "nish@xyz.com"
    print(mydict)
