"""
Name: Ka'ala Bajo
lab11.py

Problem: Plays a 3 door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.button import Button
from lab10.door import Door
from graphics import *
from random import randint

def main():
    win = GraphWin("Test", 700,700)
    win.setBackground("#75a8c7")
    exit_butt = Button(Rectangle(Point(550,50),Point(675,100)),"quit")
    exit_butt.draw(win)

    door_1 = Door(Rectangle(Point(100, 200), Point(230, 600)), "Door 1")
    door_1.color_door("#826241")
    door_1.draw(win)

    door_2 = Door(Rectangle(Point(300, 200), Point(430, 600)), "Door 2")
    door_2.color_door("#826241")
    door_2.draw(win)

    door_3 = Door(Rectangle(Point(500, 200), Point(630, 600)), "Door 3")
    door_3.color_door("#826241")
    door_3.draw(win)

    top_text = Text(Point(375,130), "I have a secret door")
    top_text.draw(win)
    bot_text = Text(Point(375,650), "Click to guess which is the secret door!")
    bot_text.draw(win)

    win_acc = 0
    loss_acc = 0
    win_counter = Button(Rectangle(Point(50,50),Point(100,100)),win_acc)
    loss_counter = Button(Rectangle(Point(100,50),Point(150,100)),loss_acc)
    win_counter.draw(win)
    loss_counter.draw(win)
    Text(Point(73,40), "wins").draw(win)
    Text(Point(123,40), "losses").draw(win)

    clicked = win.getMouse()

    while not exit_butt.is_clicked(clicked):
        bot_text.undraw()
        bot_text.setText("Click to guess which is the secret door!")
        bot_text.draw(win)

        door_list = [door_1,door_2,door_3]
        correct = door_list[randint(0,2)]
        correct.set_secret(True)
        clicked = win.getMouse()

        #door 1 stuff
        if door_1.is_clicked(clicked) and door_1.is_secret():
            door_1.color_door("green")
            top_text.setText("You Win!")
            win_acc += 1
        elif door_1.is_clicked(clicked) and not door_1.is_secret():
            door_1.color_door("red")
            correct.color_door('green')
            top_text.setText("Sorry, Incorrect!")
            loss_acc += 1

        #door 2 stuff
        elif door_2.is_clicked(clicked) and door_2.is_secret():
            door_2.color_door("green")
            top_text.setText("You Win!")
            win_acc += 1

        elif door_2.is_clicked(clicked) and not door_2.is_secret():
            door_2.color_door("red")
            correct.color_door('green')
            top_text.setText("Sorry, Incorrect!")
            loss_acc += 1

        #door 3 stuff
        elif door_3.is_clicked(clicked) and door_3.is_secret():
            door_3.color_door("green")
            top_text.setText("You Win!")
            win_acc += 1

        elif door_3.is_clicked(clicked) and not door_3.is_secret():
            door_3.color_door("red")
            correct.color_door('green')
            top_text.setText("Sorry, Incorrect!")
            loss_acc += 1
        else:
            continue
        win_counter.undraw()
        win_counter.draw(win)
        win_counter.set_label(win_acc)

        loss_counter.undraw()
        loss_counter.draw(win)
        loss_counter.set_label(loss_acc)
        bot_text.undraw()
        bot_text.setText("Click anywhere to play again!")
        bot_text.draw(win)
        win.getMouse()

        #check point. if its not, then go do the rest
        if exit_butt.is_clicked(clicked):
            win.close()
        else:
            for each_door in range(len(door_list)):
                door_list[each_door].undraw()
                door_list[each_door].draw(win)
                door_list[each_door].color_door('#826241')
                door_list[each_door].set_secret(False)

        top_text.setText("I have a secret door")

    win.close()

main()