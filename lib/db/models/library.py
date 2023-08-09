import os, time, sys

book_pic = ["book.txt","book2.txt","book3.txt","book.txt"]
reading = ["reading.txt","reading2.txt"]

def load_animation(filenames, delay = 1, repeat = 4):
    frames = []
    for name in filenames:
        with open(name, 'r', encoding = 'utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(''.join(frame))
            time.sleep(delay)
            os.system('clear')
load_animation(book_pic, delay = 0.4)
load_animation(reading, delay = 1)