import time
from name import name
from colorama.initialise import init
from command import *
import os
from dir import *
from document import *
from new import * 
from colorama import Fore, Back, Style
from colorama import init
init()

def vibor1():
    global v1
    v1 = str(input('Enter the color blue,green,red,yellow,cyan,magenta,black,white,light yellow,light black, light blue, light red, light magenta, light white, light green:'))

def vibor2():
    global v2 
    v2 = str(input('Enter the color blue,green,red,yellow,cyan,magenta,black,white,light yellow,light black, light blue, light red, light magenta, light white, light green:'))

os.system('cls||clear')

print(Fore.GREEN)

print('WELCOME my system COS')#Start
print('Enter help')
print('Youtube - https://www.youtube.com/channel/UCM2-eeYUWp7FsNWvfD1js8w\n')
print('''░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗  ░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░  ██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗  ╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝  ░╚════╝░╚═════╝░''')


while True:
    com = str(input(name + '[?]' + name + ':'))
    if com == 'clear':
        os.system('cls||clear')
    elif com == 'off':
        break
    elif com == 'restart':#restart
        os.system('cls||clear')
        print('WELCOME my system COS')
        print('Enter help')
        print('Youtube - https://www.youtube.com/channel/UCM2-eeYUWp7FsNWvfD1js8w\n')
        print('''░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗  ░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░  ██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗  ╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝  ░╚════╝░╚═════╝░''')
    elif com == 'SYSTEM':#system
        print('USER')
    elif com == 'reverse word':#rever
        revers()
    elif com == 'help':#help
        print(command)
    elif com == 'ls':#dir
        print(d)
    elif com == 'dir':#dir
        print(d)
    elif com == 'document':#document
        print(doc)
    elif com == 'stopwatch':#stopwatch
        hour = 0
        minute = 0
        second = 0
        while True:
            time.sleep(1)
            second = second + 1
            os.system("cls||clear")
            print('Time:' + str(hour) + ':' + str(minute) + ':' + str(second))
            if second == 60:
                minute = minute + 1
                second = 0
    elif com == 'edit file':#editfile
        print(doc)
        select = str(input('Enter the file name:'))
        f = str(input())
    elif com == 'rename':#rename
        newname = str(input('Enter the new name:'))
        if newname.isnumeric():
            print('The name must not be a number')
        else:
            name = newname
    elif com == 'create folder':#create folder
        foldername = str(input('Enter the new folder name:'))
        d.append(foldername)
        print(d)
    elif com == 'create file':#create file
        filename = str(input('Enter the new file name:'))
        doc.append(filename)
        print(doc)
    elif com == 'setting the theme for the text':#text color
        vibor1()
        if v1 == 'blue':
            print(Fore.BLUE)
        elif v1 == 'green':
            print(Fore.GREEN)
        elif v1 == 'red':
            print(Fore.RED)
        elif v1 == 'yellow':
            print(Fore.YELLOW)
        elif v1 == 'cyan':
            print(Fore.CYAN)
        elif v1 == 'magenta':
            print(Fore.MAGENTA)
        elif v1 == 'black':
            print(Back.WHITE)
            print(Fore.BLACK)
        elif v1 == 'white':
            print(Back.BLACK)
            print(Fore.WHITE)
        elif v1 == 'light yellow':
            print(Fore.LIGHTYELLOW_EX)
        elif v1 == 'light black':
            print(Fore.LIGHTBLACK_EX)
        elif v1 == 'light blue':
            print(Fore.BLUE)
        elif v1 == 'light red':
            print(Fore.LIGHTRED_EX)
        elif v1 == 'light magenta':
            print(Fore.LIGHTMAGENTA_EX)
        elif v1 == 'light white':
            print(Fore.LIGHTWHITE_EX)
        elif v1 == 'light green':
            print(Fore.LIGHTGREEN_EX)
        else:
            print('No color')
    elif com == 'background color setting':#background color
        vibor2()
        if v2 == 'blue':
            print(Back.BLUE)
        elif v2 == 'green':
            print(Back.GREEN)
        elif v2 == 'red':
            print(Back.RED)
        elif v2 == 'yellow':
            print(Back.YELLOW)
        elif v2 == 'magenta':
            print(Back.MAGENTA)
        elif v2 == 'black':
            print(Back.BLACK)
        elif v2 == 'white':
            print(Back.WHITE)
        elif v2 == 'light yellow':
            print(Back.LIGHTYELLOW_EX)
        elif v2 == 'light black':
            print(Back.LIGHTBLACK_EX)
        elif v2 == 'light blue':
            print(Back.BLUE)
        elif v2 == 'light cyan':
            print(Back.LIGHTCYAN_EX)
        elif v2 == 'light red':
            print(Back.LIGHTRED_EX)
        elif v2 == 'light magenta':
            print(Back.LIGHTMAGENTA_EX)
        elif v2 == 'light white':
            print(Back.LIGHTWHITE_EX)
        elif v2 == 'light green':
            print(Back.LIGHTGREEN_EX)
    elif com == 'clock':#clock
        ho = int(input('Enter the hour:'))
        mi = int(input('Enter the minute:'))
        se = int(input('Enter the second:'))

        while True:
            time.sleep(1)
            se = se + 1
            os.system('cls||clear')
            print(str(ho) + ':' + str(mi) + ':' + str(se))
            if se == 60:
                se = 0
                mi = mi + 1
            if mi == 60:
                mi = 0
                ho = ho + 1
            if ho == 24:
                se = 0
                mi = 0
                hou = 0 
    elif com == 'remove folder':#remove folder
        namefolder = str(input('Enter the folder name:'))
        if namefolder == 'DOCUMENT':
            print('ERROR')
        elif namefolder == 'SYSTEM':
            print('ERROR')
        else:
            d.remove(namefolder)
            print(d)
    elif com == 'remove file':#remove file
        namefile = str(input('Enter the file:'))
        if namefile == 'SYSTEM.txt':
            print('ERROR')
        elif namefile == 'Information.txt':
            print('ERROR')
        else:
            doc.remove(namefile)
            print(doc)
    elif com == 'calculator':#calculator
        onenumber = float(input('One number:'))
        twonumber = float(input('Two number:'))
        choice = input('+, -, *, /, %:')
        
        if choice == '+':
            c = twonumber + onenumber
            print(c)
        elif choice == '-':
            if onenumber < twonumber:
                c = twonumber - onenumber
                print(c)
            elif onenumber >= twonumber:
                c = onenumber - twonumber
                print(c)
        elif choice == '*':
            c = onenumber * twonumber
            print(c)
        elif choice == '/':
            if onenumber < twonumber:
                c = twonumber / onenumber
                print(c)
            elif onenumber >= twonumber:
                c = onenumber / twonumber
                print(c)
        elif choice == '%':
            if onenumber < twonumber:
                c = twonumber % onenumber
                print(c)
            elif onenumber >= twonumber:
                c = onenumber % twonumber
                print(c)
        else:
            print('NO command')
    else:
        print('NO command')
input()