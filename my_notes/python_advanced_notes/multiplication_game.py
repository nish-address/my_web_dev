import random

correct_answers = 0
incorrect_answers = 0

while True:  
     x = random.randint(1, 10)
     y = random.randint(1, 10)
     product = x * y

     print(f'{x} * {y} = ?')
     user_input = float(input(''))

     if user_input == product and incorrect_answers != 5:
          correct_answers += 1
          print(f"correct_answers = {correct_answers}")
          print(f"incorrect_answers = {incorrect_answers}")

     elif user_input != product and incorrect_answers != 5:
          incorrect_answers += 1
          print(f"correct_answers = {correct_answers}")
          print(f"incorrect_answers = {incorrect_answers}")

     elif user_input != product and incorrect_answers == 5:
          print('You Lose!')
          print(f"correct_answers = {correct_answers}")
          print(f"incorrect_answers = {incorrect_answers}")
          break

     elif user_input == product and correct_answers == 20:
          print('You win!')
          print(f"correct_answers = {correct_answers}")
          print(f"incorrect_answers = {incorrect_answers}")
          break
     
     else:
          print('Some bug in the system')
          print(f"correct_answers = {correct_answers}")
          print(f"incorrect_answers = {incorrect_answers}") 
          break
          
          