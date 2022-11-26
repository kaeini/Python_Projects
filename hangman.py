import random
def choose_word():
  with open("my_dictonary.txt","r") as f:
    all_text = f.read()
    words = list(map(str, all_text.split()))
    word_choice = random.choice(words)
    f.close()
    hang_man_game(word_choice)
    

def hang_man_game(word_choice):
  print("Welcome to hang_man!")
  allowed_guesses = 8
  guesses = []
  done = False
  while not done:
    for letter in word_choice:
      if letter.lower() in guesses:
        print(letter, end=" ")
      else:
        print("_", end=" ")
      print("")
    guess = input(f"Guess a word in the letter, you have {allowed_guesses} left: ")
    guesses.append(guess.lower())
    if guess.lower() not in word_choice.lower():
      allowed_guesses -= 1
    if allowed_guesses == 0:
      print(f"You lost! The word was {word_choice}")
      break
   
    done = True
    for letter in word_choice:
      if letter.lower() not in guesses:
        done = False
  if done:
    print(f"You win! The letter was {word_choice}")
    

#Main Program
choose_word()
