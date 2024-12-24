import random
from colorama import Fore, Style, init
init(autoreset=True)

def pause():           #debugging
  input("")

fileLocation = "/home/johnny/Downloads/VSCODE/5_letter_words_list.txt"
contents = []
with open(fileLocation, "r") as file:
  for word in file.readlines():
    contents.append(word.strip())

keyboardRow1 = "qwertyuiop"
keyboardRow2 = "asdfghjkl"
keyboardRow3 = "zxcvbnm"
keepPlaying = True

while keepPlaying:
  secretWord = random.choice(contents)

  # variables kept for the entire game
  # making default colors for keyboard rows. resets every game, but not every round
  keyboardRow1Colors = {}
  keyboardRow2Colors = {}
  keyboardRow3Colors = {}
  for c in keyboardRow1: keyboardRow1Colors[c] = "NOTHING"
  for c in keyboardRow2: keyboardRow2Colors[c] = "NOTHING"
  for c in keyboardRow3: keyboardRow3Colors[c] = "NOTHING"
  wordFound = False
  attempts = 0
  guessedWords = []

  # game starts
  while not wordFound:
    # retriving the guess and if correct (or max attempts reached), ending the game
    wordIsOk = False
    while not wordIsOk:
      guessedWord = input("Guess a 5 letter word: ").lower()
      if guessedWord == "i give up": 
        attempts = 6
        break
      elif guessedWord in contents:  
        wordIsOk = True
      else:
        print(" That is not a valid guess")
    if guessedWord == secretWord:
      wordFound = True
      print(f"{secretWord} was the word! It took you {attempts} attempts.")
      wantsToPlayAgain = input("Do you want to play again? (y/n): ")
      if wantsToPlayAgain == "y": keepPlaying = True
      else:                       keepPlaying = False
      break
    elif attempts >= 6:
      wordFound = True
      print(f"Max amount of guesses taken. The word was {secretWord}")
      wantsToPlayAgain = input("Do you want to play again? (y/n): ")
      if wantsToPlayAgain == "y": keepPlaying = True
      else:                       keepPlaying = False
      break
      

    # variables that reset each round
    letterColors = []
    guessFormatted = ""

    # placing the correct colors in the correct places for the guess. used for actually formatting the letters in the next step.
    # looks like this: 
    #  guessedWord = train
    # letterColors = [('t', 'COLOR'), ('r', 'COLOR'), etc...]
    for i in range(5):
      c = guessedWord[i].lower()
      if c in secretWord[i]: letterColors.append((c, "GREEN"))
      elif c in secretWord:  letterColors.append((c, "YELLOW"))
      else:                  letterColors.append((c, "BLACK"))

    # actually formatting the letters with correct color. used for printing later on for the player
    for item in letterColors:
      match item[1]:
        case "GREEN":  guessFormatted += Fore.GREEN + Style.BRIGHT + item[0] + Style.RESET_ALL
        case "YELLOW": guessFormatted += Fore.YELLOW + Style.BRIGHT + item[0] + Style.RESET_ALL
        case "BLACK":  guessFormatted += Fore.BLACK + Style.BRIGHT + item[0] + Style.RESET_ALL

    # updating the keyboardRowXColors with correct colors based on the colors of the guess. used to format the keyboard in the next step
    for letter, color in letterColors:
      if    letter in keyboardRow1: keyboardRow1Colors[letter] = color
      elif  letter in keyboardRow2: keyboardRow2Colors[letter] = color
      else:                         keyboardRow3Colors[letter] = color


    # actually printing the keyboard with correct colors. used for the player to see the letters theyve guessed
    for c in keyboardRow1Colors:
      match keyboardRow1Colors[c]:
        case "NOTHING": print(c, end=" ")
        case "GREEN": print(Fore.GREEN + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "YELLOW": print(Fore.YELLOW + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "BLACK": print(Fore.BLACK + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
    print("\n", end=" ")
    for c in keyboardRow2Colors:
      match keyboardRow2Colors[c]:
        case "NOTHING": print(c, end=" ")
        case "GREEN": print(Fore.GREEN + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "YELLOW": print(Fore.YELLOW + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "BLACK": print(Fore.BLACK + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
    print("\n", end="   ")
    for c in keyboardRow3Colors:
      match keyboardRow3Colors[c]:
        case "NOTHING": print(c, end=" ")
        case "GREEN": print(Fore.GREEN + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "YELLOW": print(Fore.YELLOW + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
        case "BLACK": print(Fore.BLACK + Style.BRIGHT + c +Style.RESET_ALL, end=" ")
    print()


    ############################################################################
    guessedWords.append(guessFormatted)
    print(" Guesses:")
    for word in guessedWords:
      print(" " + word)
    print("---------------------------")
  
  attempts+=1