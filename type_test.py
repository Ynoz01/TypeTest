import random 
import curses

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

def print_sentences(sentences: tuple):
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

def type_test(sen):
    stdscr = curses.initscr()
    curses.filter()


def main():
    sentences = sentences_func()
    print("Welcome to this typing test! You will be given a block of text and need to type it as fast as possible.\n Press any key to start")
    if(input()):
        sen = print_sentences(sentences)
        type_test(sen)

if __name__ == "__main__":
    main()