import random
from Words import words_list
def get_word():
 word = random.choice(words_list)
 return word.upper()


def play(word):
    uncompleted_word="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    attempts=6
    print(display_hangman(attempts))
    print(uncompleted_word)
    while attempts>0 and guessed==False :
       guess=input("please enter a letter or a word: ").upper()

       if len(guess)== 1 and guess.isalpha():
         if guess in guessed_letters:
            print("you already guessed the letter",guess)

         elif guess not in word:
            print("wrong letter",guess)
            attempts-=1
            guessed_letters.append(guess)
            print(display_hangman(attempts))
            print(uncompleted_word)
         else:
            print("correct guess the letter is in the word",guess)
            guessed_letters.append(guess)
            word_as_list=list(uncompleted_word)
            indicies = [i for i, letter in enumerate(word) if guess == letter]

            for i in indicies:
               word_as_list[i]=guess
            uncompleted_word="".join(word_as_list)
            print(display_hangman(attempts))
            print(uncompleted_word)
            if "_" not in uncompleted_word:
                    guessed = True


       elif len(guess)== len(word) and guess.isalpha():
          if word == guess:
             print("congratulations you guessed the word correctly",guess)
             guessed=True
             guessed_words.append(guess)
             print(display_hangman(attempts))
             print(uncompleted_word)
          else:
             print("wrong word", guess)
             guessed_words.append(guess)
             attempts-=1
             print(display_hangman(attempts)) 
             print(uncompleted_word)



       else:
          print("invalid text")
   

















def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)



if __name__ == "__main__":
    main()