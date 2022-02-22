"""
Name: Kaala Bajo
lab6.py

Problem: This program creates a vignere cipher maker with a simple GUI

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def vigenere():
    #create win
    win = GraphWin("Vigenere", 600,400)
    win.setBackground("white")

    #display instructional text
    msg_encode = Text(Point(150, 100), "Message to encode")
    msg_encode.draw(win)
    msg_keyword = Text(Point(147, 170), "Enter the keyword")
    msg_keyword.draw(win)

    #display entry boxes
    entry_code = Entry(Point(340, 101), 25)
    entry_code.draw(win)
    entry_key = Entry(Point(317, 170), 20)
    entry_key.draw(win)

    #encode box and click part
    box = Rectangle(Point(250,250), Point(360,300))
    box.setFill("pink")
    box.draw(win)
    mid_box = box.getCenter()
    msg_instruct = Text(mid_box, 'Encode')
    msg_instruct.draw(win)
    win.getMouse() #click to initialize and undraw
    box.undraw()
    msg_instruct.undraw()

    #get code and key
    code = entry_code.getText()
    key = entry_key.getText()
    #make them usable
    code = code.upper()
    key = key.upper()
    code = code.replace(" ", "")
    key = key.replace(" ", "")

    #great ok now like the hard part
    #make some lists for code and key
    track_code = []
    track_key = []
    for letter in code:
        track_code.append(ord(letter) - 65)
    for letter in key:
        track_key.append(ord(letter) - 65)

    #make a new list to keep track of the number versions
    nums = []
    for i in range(len(code)):
        looped = int(track_code[i])+int(track_key[i%len(key)])
        #idk why but it wasn't running when i didn't put int so its there?
        #maybe it was due to something else but idk
        #note to self: %len(key) to loop back around and
         #%26 is because 26 letters in alphabet
        nums.append(looped % 26)

    #ciphered is a blank string that will add all our letters
    ciphered = ''
    for i in nums:
        ciphered = ciphered + chr(i + 65)

    #all thats left to do is display it
    msg_result = Text(Point(300, 250), "Resulting Message")
    msg_result.draw(win)
    msg_code = Text(Point(300, 275), ciphered)
    msg_code.draw(win)

    #done!
    msg_end = Text(Point(300, 375), "click anywhere to close")
    msg_end.draw(win)
    win.getMouse()
    win.close()
vigenere()
