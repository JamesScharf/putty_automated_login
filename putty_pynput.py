from pynput.keyboard import Key, Controller
from time import sleep


def type_word(word):
    for char in word:
        keyboard.press(char)
        keyboard.release(char)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


while True:
    # open up putty
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # now navigate putty
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    # ssh should now be set

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keybard.release(key.tab)

    keyboard.press(Key.down)
    keyboard.release(Key.dow)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    username = "alexandra"
    password = "hacking1972"

    type_word(username)
    sleep(3)
    type_word(password)
    sleep(3)

    type_word("exit")
