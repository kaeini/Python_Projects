import random


def Generate_Simple_Questions():
  num1 = random.randint(1, 9)
  num2 = random.randint(1, 9)
  return num1, num2


def Generate_Complex_Questions():
  div1 = random.randint(1, 4)
  div2 = random.randint(1, 2)
  if div1 < div2:
    div1, div2 = div2, div1
  return div1, div2


def Check_Simple_Questions(num1, num2, operators, answer):
  if operators == ['+']:
    if answer == num1 + num2:
      print("Correct!")
      Score()
    else:
      print(f"Wrong! The answer was: {num1 + num2}")
  elif operators == ['-']:
    if answer == num1 - num2:
      print("Correct!")
      Score()
    else:
      print(f"Wrong! The answer was: {num1 - num2}")
  elif operators == ['*']:
    if answer == num1 * num2:
      print("Correct!")
      Score()
    else:
      print(f"Wrong! The answer was: {num1 * num2}")


def Check_Complex_Questions(div1, div2, operators, answer):
  if operators == ['/']:
    if answer == div1 / div2:
      print("Correct!")
      Score()
    else:
      print(f"Wrong! The answer was {div1 / div2}")


def Score():
  global score
  score += 1

def Textfile(name,classes,score):
  with open('Scores.txt','a') as f:
    text = [f"Score: {score}", f"Name: {name}", f"Class: {classes}"]
    f.write("\n")
    for line in text:
      f.write(line)
      f.write("\n")
    f.close()


def Questions():
  name = input("What is your name: ")
  classes = int(input("What class number are you in (1-3): "))
  for i in range(11):
    if i == 10:
      print(f"{name} from class {classes} you got a score of {score}")
      Textfile(name, classes, score)
      exit()
    else:
      operators = '+', '-', '*', '/'
      operators = random.sample(operators, 1)
      if operators != ['/']:
        num1, num2 = Generate_Simple_Questions()
  
        if operators == ['+']:
          print(f"What is {num1} + {num2}")
          answer = int(input("Answer: "))
          Check_Simple_Questions(num1, num2, operators, answer)
  
        elif operators == ['-']:
          print(f"What is {num1} - {num2}")
          answer = int(input("Answer: "))
          Check_Simple_Questions(num1, num2, operators, answer)
  
        elif operators == ['*']:
          print(f"What is {num1} * {num2}")
          answer = int(input("Answer: "))
          Check_Simple_Questions(num1, num2, operators, answer)
  
      else:
        div1, div2 = Generate_Complex_Questions()
        print(f"What is {div1} / {div2}")
        answer = float(input("Answer: "))
        Check_Complex_Questions(div1, div2, operators, answer)


#Main Program
score = 0
Questions()
