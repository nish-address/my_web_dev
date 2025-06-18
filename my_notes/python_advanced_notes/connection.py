import random
# x = random.randint(10, 99)
# y = random.randint(10, 99)
# sum = x + y


correct_answers = 0
incorrect_answers = 0

while incorrect_answers < 3:
     x = random.randint(10, 30)
     y = random.randint(10, 30)
     sum = x + y
     print(f'{x} + {y}')
     user_answer = float(input("= "))
     if user_answer == sum:
          correct_answers += 1
          print(f'correct_answers = {correct_answers}')
          print(f'incorrect_answers = {incorrect_answers}')
     elif user_answer != sum:
          incorrect_answers += 1
          print(f'correct_answers = {correct_answers}')
          print(f'incorrect_answers = {incorrect_answers}')
     elif user_answer != sum and incorrect_answers == 3:
          print(f'correct_answers = {correct_answers}')
          print(f'incorrect_answers = {incorrect_answers}')
          print('You lose! ')
          break
     elif user_answer == sum and correct_answers == 15:
          print(f'correct_answers = {correct_answers}')
          print(f'incorrect_answers = {incorrect_answers}')
          print('You win! ')
          break

          





