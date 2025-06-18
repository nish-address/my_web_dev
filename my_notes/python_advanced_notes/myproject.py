'''
my_dict = {
     'Tiger': 'animal that lives in the forest',
     'whale': 'animal that lives in the sea',
     'Hawk': 'bird that flies'
    
}

question = input('Enter your animal: ')
if question == 'Tiger':
     print(my_dict['Tiger'])
elif question == 'Whale':
     print(my_dict['Whale'])
elif question == 'Hawk':
     print(my_dict['Hawk'])

'''
#count vowels in a string
#Dict {}
#tuples []


vowels = ['a', 'e', 'i', 'o','u']
count = 0

letter = input('Enter your word: ')

for single_letter in letter:
     if single_letter in vowels:
          count += 1

print(count)









     
     

