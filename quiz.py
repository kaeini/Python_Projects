#Quiz Maker, fully functional. Gets questions without duplicate entries. Answer checking has been implemented.
import random

def get_questions():
  if questions_answered == 10:
     print(f"{name} you have answered all the questions! You got a score of: {score} out of 10")
     if score <= 3:
       print("Wow, that was awful. Better work on your general knowledge!")
       exit()
     elif score >= 4 and score <= 6:
       print("That was alright, still a few gaps in there though.")
       exit()
     elif score >= 7 and score <= 9:
       print("Wow! Impressive showing. That's quite a range of general knowledge you have.")
       exit()
     elif score == 10:
       print("Perfect! Fair play to you. :)")
       exit()
  else:
    with open('questions.txt','r') as f:
      file = f.read().splitlines()
      line_num = 0
      questions = random.choice(file)
      if questions in question_list:
        f.close()
        get_questions()
      else:
          for line in file:
            line_num += 1
            if line.find(questions) >= 0:
              global question_number
              question_number = line_num
          question_list.append(questions)
          ask_questions()
        
def ask_questions():
  global questions_answered
  print(question_list[questions_answered])
  answer = input("Answer: ")
  choice = check_answer(answer)

  if choice == True:
    print(f"{name} you are correct!")
    questions_answered += 1
    global score
    score += 1
    get_questions()

  elif choice == False:
    print("That is wrong!")
    questions_answered += 1
    get_questions()


def check_answer(answer):
  with open('answers.txt','r') as ans:
    lines = ans.readlines()
    if answer.lower() == lines[question_number-1].strip():
      return True
    else:
      return False
      
    
  
#Main Program
question_list = []
question_number = 0
questions_answered = 0
score = 0
name = input("What is your name: ")
get_questions()
      