import math
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
sum = num1 + num2
correct_answer = 0
incorrect_answer = 0
tries = 3
while tries != 0:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  sum = num1 + num2
  answer = int(input(f'{num1} + {num2} = '))
  if answer == sum:
    correct_answer += 1
    print(f"Correct_answers = {correct_answer}")
    print(f"incorrect_answers = {incorrect_answer}")
  else:
    incorrect_answer += 1
    tries -= 1
    print(f"incorrect_answers = {incorrect_answer}")
    print(f"Correct_answers = {correct_answer}")
