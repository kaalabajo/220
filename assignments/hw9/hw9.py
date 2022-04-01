"""Name: Ka'ala Bajo
lab9.py

Problem: Plays 2 versions of hangman

Certification of Authenticity:
I certify that this assignment is entirely my own work."""
from random import randint
from graphics import *

def get_words(file_name):
    in_f = open(file_name, "r")
    words = []
    for i in (in_f.readlines()):
        words.append(i)
    return(words)

def get_random_word(words):
    for i in range(len(words)):
        words[i] = words[i].strip().replace("\n","")
    return words[randint(0,len(words)-1)]


def letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def already_guessed(letter, guesses):
    for a_letter in guesses: #list guesses
        if a_letter == letter:
            return True
    return False

def make_hidden_secret(secret_word, guesses):
    underscored = []
    for count in range(len(secret_word)):
        underscored.append("_")
    for i in range(len(secret_word)):
        for j in guesses:
            if j == secret_word[i]:
                underscored[i] = secret_word[i]
    worded = " ".join(underscored)
    return(worded)


def won(guessed):
    return "_" not in guessed


def play_graphics(secret_word):
    win = GraphWin("Hangman",1000,500)
    win.setBackground("light blue")

    guesses = []
    printed_guesses = ""
    remaining = 6
    body_acc = 0

    head = Circle(Point(800,150), 50)
    chest = Line(Point(800,200),Point(800,350))
    arm_1 = Line(Point(800,240), Point(725,220))
    arm_2 = Line(Point(800,240), Point(875,220))
    leg_1 = Line(Point(800,350),Point(750,415))
    leg_2 = Line(Point(800,350), Point(850,415))
    body_parts = [leg_2,leg_1,arm_2,arm_1,chest,head]
    gallow_1 = Line(Point(950,50),Point(950,450)).draw(win)
    gallow_2 = Line(Point(950,50),Point(800,50)).draw(win)
    gallow_3 = Line(Point(800,50),Point(800,100)).draw(win)
    gallow_4 = Line(Point(970,450),Point(800,450)).draw(win)

    intro = "h a n g m a n   b u t   a e s t h e t i c"
    header = Text(Point(500,30), intro)
    header.setSize(18)
    header.draw(win).setFill("white")


    guess_text = Text(Point(400,120), "your guess: ")
    guess_text.setSize(18)
    guess_text.setFill("pink3")
    guess_text.setStyle('bold')
    guess_text.draw(win)

    enter_box = Entry(Point(510, 122), 6)
    enter_box.setFill('white')
    enter_box.draw(win)

    while not won(make_hidden_secret(secret_word, guesses)):
        player_guess = enter_box.getText()

        #get the text
        if not already_guessed(player_guess,guesses):
            printed_guesses += player_guess
            guesses.append(player_guess)
        if not letter_in_secret_word(player_guess,secret_word):
            remaining = remaining-1
            body_parts[remaining].draw(win)
            body_acc += 1

        if won(make_hidden_secret(secret_word, guesses)):
            underscored.setText(secret_word)
            underscored.setSize(30)
            underscored.setFill('pink4')
            underscored.draw(win)
            winning = Text(Point(500, 40), "YOU WIN! | click to close :)")
            winning.setSize(25)
            winning.setTextColor('pink4')
            winning.draw(win)
            break
        if body_acc == 6:
            underscored.setText("the word was " + secret_word)
            underscored.setSize(30)
            underscored.setFill('pink4')
            underscored.draw(win)

            loser = Text(Point(500,450),"YOU LOSE | CLICK TO CLOSE")
            loser.setSize(25)
            loser.setFill('red')
            loser.draw(win)
            break
        #display letters guessed
        guessed = Text(Point(500, 150), printed_guesses)
        guessed.draw(win)
        underscored = Text(Point(500, 250), make_hidden_secret(secret_word, guesses))
        underscored.setSize(30)
        underscored.draw(win)

        remaining_print = Text(Point(875,30), "guesses left: {}".format(remaining))
        remaining_print.setTextColor("pink3")
        remaining_print.setSize(16)
        remaining_print.draw(win)
        win.getMouse()

        guessed.undraw()
        remaining_print.undraw()
        underscored.undraw()


    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guesses = []
    remaining = 6
    while not won(make_hidden_secret(secret_word,guesses)):
        print("already guessed: {}".format(guesses))
        print("guesses remaining: {}".format(remaining))
        print(make_hidden_secret(secret_word,guesses)+"\n")

        player_guess = input('guess a letter: ')
        if not already_guessed(player_guess,guesses):
            guesses.append(player_guess)
        else:
            print('(you already guessed that)\n')

        if letter_in_secret_word(player_guess,secret_word):
            pass
        else:
            remaining -= 1

        if remaining == 0:
            print('take an L, you lose\nthe word was {}'.format(secret_word))
            break
    if won(make_hidden_secret(secret_word,guesses)):
        print('winner!\n{}'.format(secret_word))


if __name__ == '__main__':
    pass
    #play_command_line(secret_word)
    #play_graphics(secret_word)
