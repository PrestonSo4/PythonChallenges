#www.101computing.net/word-unscramble-challenge/
from random import shuffle
def scramble(word):
  letters=list(word)
  shuffle(letters)
  scrambledWord = "".join(letters)
  return scrambledWord
words = ["mouse","keyboard","monitor","printer","harddrive","speakers", "aberacadabera"]
shuffle(words)
def main():
    score = 0
    total = 0
    for word in words:
        if len(word) < 4:
            points = 1
        elif len(word) < 7:
            points = 2
        elif len(word) < 10:
            points = 3
        else:
            points = 5
        total += points
        scrambled = scramble(word)
        print("Word: " + str(scrambled) + " | Points: " + str(points))
        guess = input('Guess: ')
        if guess == word:
            print('You got it correct!!')
            score += points
        else:
            print('Sorry, that is incorrect. The word was: ' + word)
    print('Final Score: ' + str(points) + '/' + str(total))
main()
