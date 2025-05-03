import random
def hangman():
    words = ["python" , "developer" , "hangman" ,"programming" , "script"]
    word = random.choice(words)
    guessed = ["_"]* len(word)
    attempts =6

    while attempts > 0 and "_" in guessed:
         print("word:"," ".join(guessed))
         guess = input ("guess a letter: ").lower()
         if guess in word :
              for i,char in enumerate(word):
                  if char == guess:
                      guessed[i]=guess
                  else:
                      attempts -= 1
                      print("worng!{attempts} attemps left.")
                      if "_" not in guessed:
                          print("congratulations! you gussed the word:",word)
                      else:
                          print("game over! the word was:", word)
                          hangman()