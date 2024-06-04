import random 
import time
import curses 
from curses import wrapper



def sentences_func():
    sentences = (
    "The sun sets in the west, painting the sky with hues of orange and pink.",
    "She opened the old book, and a world of magic and mystery unfolded before her eyes.",
    "The cat curled up on the windowsill, basking in the warmth of the afternoon sun.",
    "He traveled to distant lands, seeking adventure and new experiences.",
    "The sound of the ocean waves was a soothing lullaby, easing her into a peaceful sleep.",
    "In the heart of the forest, they discovered a hidden waterfall cascading into a crystal-clear pool.",
    "The aroma of freshly baked bread filled the kitchen, making everyone’s mouth water.",
    "With a determined look, she crossed the finish line, completing her first marathon.",
    "The old man shared stories of his youth, filled with wisdom and nostalgia.",
    "A rainbow appeared after the storm, a symbol of hope and renewal.",
    "The children built a sandcastle on the beach, complete with towers and a moat.",
    "He gazed at the stars, wondering about the mysteries of the universe.",
    "The garden was in full bloom, a riot of colors and fragrances.",
    "She played the piano with such emotion, it brought tears to the audience’s eyes.",
    "The puppy chased its tail in endless circles, a ball of boundless energy.",
    "The artist painted a masterpiece, capturing the essence of the bustling city.",
    "The first snow of the season blanketed the town in a pristine, white layer.",
    "She whispered a secret wish into the well, hoping it would come true.",
    "The mountain peak stood tall and majestic, challenging climbers to conquer it.",
    "The scent of pine trees and fresh earth filled the air, reminding him of childhood summers."
    )
    return sentences

def random_sentences(sentences: tuple):
    """"
    print("pick number of sentences: \n")
    bulk, run, counter, sen = int(input()), True, 0, ""

    while run:
        if(counter <= bulk):
            sen_random = random.choice(sentences)
            counter += 1
            sen += sen_random + " "
        else:
            run = False

    print(sen)
    return sen
    """
    sen_random = random.choice(sentences)
    return sen_random

def colors():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
def draw_string(window, strs, posX, posY):
    window.clear()
    window.addstr(posX, posY, strs)
    window.refresh()
    window.getch()

def draw_char(window, chars, posY, posX, right):
    if right:
        window.addch(posY, posX, chars, curses.color_pair(1))
    else:
        window.addch(posY, posX, chars, curses.color_pair(2))
    window.refresh()

def delete_char(window,replacer, posY, posX):
    window.delch(posY, posX)
    window.insch(posY, posX, replacer)
    window.refresh()

def draw_wpm(window, t, n, wpm_list):
    t = time.time() - t
    wpm = 60.0/t
    if(n == 0):
        wpm_list.append(wpm)
        window.addstr(1, 5, f"{wpm}")
    else:
        wpm_list.append(wpm)
        res = 0
        for i in wpm_list:
            res += i
        
        res = res/n
        window.addstr(1, 5, f"{res}")
    window.refresh()
    return time.time()


def type_test(sen, window):

    colors()
    right = True
    counter = 0
    curses.filter()
    t = time.time()
    wpm_list: list = []
    while counter <= len(sen):
        key = window.getch()
        
        if counter == len(sen):
            break

        if not key == 8 and not key ==32:
            
            if sen[counter] == chr(key):
                right = True
            else:
                right = False

            draw_char(window, key, 0, counter, right)
            counter += 1

        elif counter >= 1 and key == 8:
            counter -= 1
            replacer = sen[counter]
            delete_char(window, replacer, 0, counter)
        elif key == 32 or key == 44 or key == 46:
            draw_char(window, key, 0, counter, right)
            counter += 1
            t = draw_wpm(window, t, counter+1, wpm_list)
        
    

def main(window):
    curses.curs_set(0)
    sen_tup = sentences_func()
    welcome_message = "Welcome to this typing test! You will be given a block of text and need to type it as fast as possible.\n Press any key to start."
    draw_string(window, welcome_message, 0, 0)
    random_s = random_sentences(sen_tup)
    draw_string(window, random_s, 0 , 0)
    window.addstr(1, 0, "WPM: ")
    window.refresh()
    type_test(random_s, window)




if __name__ == "__main__":
    wrapper(main)