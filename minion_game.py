def minion_game(string):
    score = {'Kevin': 0,'Stuart': 0}
    vowels = "AEIOU"
    string_length = len(string)
    for i in range(string_length):
        if string[i] in vowels:
            score['Kevin'] += (string_length - i)
        else:
            score['Stuart'] += (string_length - i)
    if score['Kevin'] > score['Stuart']:
        print("Kevin wins with a score of:",score['Kevin'])
    elif score['Stuart'] > score['Kevin']:
        print("Stuart wins with a score of:",score['Stuart'])
    elif score['Kevin'] == score['Stuart']:
        print("Draw")
      
#Main Program
string = input("Input a word for the minion game (in caps): ")
minion_game(string)