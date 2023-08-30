for i in range(99999999999999999999999999999999999):

  question_1 = 'Как расшифровывается VR?'
  question_2 = 'Как называется столица Люксембурга?'
  question_3 = 'Сколько городов в России?'

  answer_1 = 'виртуальная реальность'
  answer_2 = 'Люксембург'
  answer_3 = '1119'

  result = 0

  print(question_1)
  user_answer = input()
  if user_answer == answer_1:
    result += 1
    print('ответ верный')

  print(question_2)
  user_answer = input()
  if user_answer == answer_2:
    result += 1
    print('ответ верный')

  print(question_3)
  user_answer = input()
  if user_answer == answer_3:
    result += 1
    print('ответ верный')

  print('ты ответил на', result, 'балов')

  print('хотите пройти игру заново')
  print('0 - да, 1 - нет')
  last_answer = int(input('Введите ответ: '))
  if last_answer == 1:
    break
