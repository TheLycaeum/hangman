# Introduction

Simple implementation of the hangman game using TDD

- Features
  - Should pick a random word from the dictionary at
    =/usr/share/dict/words= (sudo apt-get install
    dictionaries-common if you don't have this file). The word
    should have atleast 8 characters.
  - The user should be prompted to enter a letter. At each turn the
    following information should be presented.
    1. The word masked with _ for unguessed letters and the actual
       letter for guessed letters.
    2. The number of remaining turns (You will start with 8 turns)
    3. The letters which have been guessed already (correct and wrong)
  - If the user enters a letter that was already guessed, just say so
    and repeat the turn (don't update anything).
  - If the user enters a correct letter, update the masked word,
    the list of guessed letters and go the next turn
  - If the user enters a wrong letter, reduce the number of
    remaining turns, update the list of guessed letters and go to
    the next turn
  - If the user successfully guesses the word before 8 wrong turns,
    print "Congratulations!" and quit.
  - If the user does not guess the word before 8 wrong turns, print
    "You failed. The secret word was ..." and exit.

   e.g

   Suppose the secret word is elephant, the transcript might be like this

        The secret word is : --------
        You have 8 turns left
        Letters guessed : 
        What is your guess? 

Suppose the user types x

      Sorry 'x' is not there in the word
      The secret word is : --------
      You have 7 turns left
      Letters guessed : x
      What is your guess?

Suppose the user types e

      'e' is there in the word
      The secret word is : e-e-----
      You have 7 turns left
      Letters gussed : e x
      What is your guess?


Suppose the user types x again

      You have already guessed 'x'
      The secret word is : e-e-----
      You have 7 turns left
      Letters guessed : e x
      What is your guess?


And so on till the end.

