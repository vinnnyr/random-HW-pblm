import random

global file_object
global lines

def start(fileName):
    global file_object
    global lines

    file_object = open(fileName,"r")
    print("File opened")
    lines = file_object.readlines()
    file_object.close() #Done with reading lines

def choose():
    global lines
    random.shuffle(lines)
    choice = lines.pop()
    print(choice)

loop = False

try:
    fileName = raw_input("What is file name of HW problems? (include .txt)")
    start(fileName)
    loop=True
except IOError:
    print("Invalid File Name!")
    pass

while loop:
    try:
        cmd = raw_input('Ready for next pblm?')
        if cmd == "y":
            choose()
        pass
    except KeyboardInterrupt:
        loop = False
    except IndexError:
        print("All Done!")
        loop = False
        
