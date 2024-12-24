import random
from colorama import Fore, Style, init
init(autoreset=True)


# def pause():           #debugging
#   input("")


fileLocation = "/home/johnny/Downloads/VSCODE/5_letter_words_list.txt"
contents = []
with open(fileLocation, "r") as file:
  for word in file.readlines():
    contents.append(word.strip())
secretWord = random.choice(contents)

# allLeters = list("qwertyuiopasdfghjklzxcvbnm")      #failed attempt
keyboardRow1 = "q w e r t y u i o p"
keyboardRow2 = " a s d f g h j k l "
keyboardRow3 = "   z x c v b n m   "
newKeyboardRow1 = keyboardRow1
newKeyboardRow2 = keyboardRow2
newKeyboardRow3 = keyboardRow3

wordFound = False
attempts = 1
guessedWords = []

#########################################################################################

while not wordFound:
  wordIsOk = False
  while not wordIsOk:
    guessedWord = input(Style.RESET_ALL + "Guess a 5 letter word: ").lower()
    if guessedWord in contents: 
      wordIsOk = True
    else: print(" That is not a valid guess")
  
  if guessedWord == secretWord or attempts > 5:
    wordFound = True    

  coloredGuess = ""
  guessedWordColors = ""
  x=0
  for c in guessedWord:
    if c == secretWord[x]:
      coloredChar = Fore.GREEN + Style.BRIGHT + c + Style.RESET_ALL
      # coloredChar = f"G{c}"            #failed attempt again
      guessedWordColors += "1"
    elif c in secretWord:
      coloredChar = Fore.YELLOW + Style.BRIGHT + c + Style.RESET_ALL
      # coloredChar = f"Y{c}"            #failed attempt again
      guessedWordColors += "2"
    else:
      coloredChar = Fore.BLACK + Style.BRIGHT + c + Style.RESET_ALL
      # coloredChar = f"B{c}"            #failed attempt again
      guessedWordColors += "3"
    coloredGuess += coloredChar
    

    # replaces the letter in the keyboard with a capital so later it can change it into the correct color
    if   c in keyboardRow1.lower(): newKeyboardRow1 = newKeyboardRow1.replace(c, c.upper())
    elif c in keyboardRow2.lower(): newKeyboardRow2 = newKeyboardRow2.replace(c, c.upper())
    elif c in keyboardRow3.lower(): newKeyboardRow3 = newKeyboardRow3.replace(c, c.upper())

    '''# debugging
    print(f"LETTER COLORS: {guessedWordColors}")
    print(f"C: {c}")
    print(f"COLORED C: {coloredChar}")
    print(f"guessedWordColors[x]: {guessedWordColors[x]}")
    pause()
    print("KEYBOARD RIGHT NOW:")
    print(f"  {newKeyboardRow1}")
    print(f"  {newKeyboardRow2}")
    print(f"  {newKeyboardRow3}")
    pause()'''

    '''# failed attempt 
    # lettersToChangeWithFormatting = []
    # lettersToChangeWithFormatting.append(coloredChar)'''

    '''# failed attempt again
    #this detects for any capitals in the keyboard row and replaces it with the correct color
    lettersRow1 = ""
    for l in newKeyboardRow1:
      if l != l.lower() and l.lower() in allLeters: 
        match guessedWordColors[x]:
          case "1": lettersRow1 += Fore.GREEN + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "2": lettersRow1 += Fore.YELLOW + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "3": lettersRow1 += Fore.BLACK + Style.BRIGHT + l.lower() + Style.RESET_ALL
      else: lettersRow1 += l
      # # replacing any capitals in the OG keyboard (otherwise this part will change the color again)
      # index = keyboardRow1.index(l)
      # keyboardRow1 = keyboardRow1[:index] + l.lower() + keyboardRow1[index+1:]

    lettersRow2 = ""
    for l in newKeyboardRow2:
      if l != l.lower() and l.lower() in allLeters: 
        match guessedWordColors[x]:
          case "1": lettersRow2 += Fore.GREEN + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "2": lettersRow2 += Fore.YELLOW + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "3": lettersRow2 += Fore.BLACK + Style.BRIGHT + l.lower() + Style.RESET_ALL
      else: lettersRow2 += l
      # index = keyboardRow2.index(l)
      # keyboardRow2 = keyboardRow2[:index] + l.lower() + keyboardRow2[index+1:]
    
    lettersRow3 = ""
    for l in newKeyboardRow3:
      if l != l.lower() and l.lower() in allLeters: 
        match guessedWordColors[x]:
          case "1": lettersRow3 += Fore.GREEN + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "2": lettersRow3 += Fore.YELLOW + Style.BRIGHT + l.lower() + Style.RESET_ALL
          case "3": lettersRow3 += Fore.BLACK + Style.BRIGHT + l.lower() + Style.RESET_ALL
      else: lettersRow3 += l
      # index = keyboardRow3.index(l)
      # keyboardRow3 = keyboardRow3[:index] + l.lower() + keyboardRow3[index+1:]

    print("THE KEYBOARD USED TO PRINT: ")
    print(f"  {lettersRow1}")
    print(f"  {lettersRow2}")
    print(f"  {lettersRow3}")
    # print("OG KEYBOARD NOW: ")
    # print(f"  {keyboardRow1}")
    # print(f"  {keyboardRow2}")
    # print(f"  {keyboardRow3}")
    print("-----------------------------------------------------")
    pause()'''
    x+=1

  '''another failed attempt
  lettersRow1 = keyboardRow1
  lettersRow2 = keyboardRow2
  lettersRow3 = keyboardRow3
  x=0
  for c in lettersToChangeWithFormatting:
    for l in keyboardRow1:
      if l not in guessedWord:
        print(l, end="")
      else:
        if   c == "G": print(Fore.GREEN + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "Y": print(Fore.YELLOW + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "B": print(Fore.BLACK + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
    print()
    for l in keyboardRow2:
      if l not in guessedWord:
        print(l, end="")
      else:
        if   c == "G": print(Fore.GREEN + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "Y": print(Fore.YELLOW + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "B": print(Fore.BLACK + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
    print()
    for l in keyboardRow3:
      if l not in guessedWord:
        print(l, end="")
      else:
        if   c == "G": print(Fore.GREEN + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "Y": print(Fore.YELLOW + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")
        elif c == "B": print(Fore.BLACK + Style.BRIGHT + lettersToChangeWithFormatting[x+1] + Style.RESET_ALL, end="")




  # for item in lettersToChangeWithFormatting: 
  #   print(lettersToChangeWithFormatting)'''
    
############################################################################
  attempts+=1


  guessedWords.append(coloredGuess)

  print("---------------------------")
  print(newKeyboardRow1)
  print(newKeyboardRow2)
  print(newKeyboardRow3)
  print(" Guesses:")
  for word in guessedWords:
    print(" " + word)

#########################################################################################

if attempts > 5:
  print(f"Max amount of guesses taken. The word was {secretWord}")
else:
  print(f"{secretWord} was the word! It took you {attempts} attempts.")