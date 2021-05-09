from random import randint

EASY_LEVEL_TURNS = 10     # Global constant can be used any where
HARD_LEVEL_TURNS = 5     # Global constant can be used any where

# turns = 0    # global variable :
# if don't use global turns :
# Need to pass it in the function check_answer :

#Function to check user's guess against actual answer -means passing 2 parameters :

def check_answer(guess, answer, turns):   
  #Docstring :
  """ Checks answer against guess . Returns the number of turns remaining : """
  if guess > answer :

    # global turns     # This is global turn, so add this if want to modify

    print(" Too high ! ")
    #turns -= 1          # minus 1 time back if a guess is wrong
    # if don't use it, use return -1 :
    return turns -1

  elif guess < answer :
    print(" Too low ! ")
   # turns -=1           # minus 1 time back if a guess is wrong
    return turns -1
  else :
    print(f"You got it ! The answer was {answer}")

# Make a function to set difficulty :

def set_difficulty ():

  level = input("Choose a difficulty.Type 'easy' or 'hard':  ")

  if level == "easy" :
      return EASY_LEVEL_TURNS               # turns = EASY_LEVEL_TURNS
  else :
      return HARD_LEVEL_TURNS              # turns = HARD_LEVEL_TURNS  

def game () :  # because all variables below are global, so the function game is put
# Choosing a random number between 1 and 100:
  print("Welcome to the Guessing Game ! ")
  print (" I am thinking of a number between 1 and 100 ")
  answer = randint (1, 100)

  print(f" Pssst, the correct answer is {answer}")

  turns = set_difficulty ()      # calling function

  # if print turns here, it keeps running, not stop : so put it in while Loop
 # print(f" You have {turns} attempts remaining to guess the numbers.")


  #Repeat the guessing functionality if they get it wrong :

  guess = 0    # Set a variable for Guess at beginning
  while guess !=answer :

    print(f" You have {turns} attempts remaining to guess the numbers.") 

                                  # Let user guess a number :
    guess = int(input("Make a guess : "))

   # check_answer(guess,answer,turns)  # then pass turns in here also

    turns = check_answer(guess,answer,turns)
   
    if turns == 0 :
      print(" You have run of guesses, you lose !!! ")

      return     # means to stop the game here

    elif guess != answer :
        print(" Guess again : ")  

  #Function to check user's guess against actual answer
  # Track the number of turns and reduce by 1 if they got it wrong 
game()        # calling the function game
