import sys
import time
from colorama import init, Fore, Style
import os
import webbrowser


ascii_art = [
    Fore.MAGENTA + "        _            _          _                                  ",
    Fore.MAGENTA + "       | |          | |        (_)                                 ",
    Fore.MAGENTA + "   __ _| |_ ___  ___| |__   ___ _ _ __ ___                         ",
    Fore.MAGENTA + "  / _` | __/ _ \/ __| '_ \ / __| | '_ ` _ \                        ",
    Fore.MAGENTA + " | (_| | ||  __/\__ \ | | | (__| | | | | | |                       ",
    Fore.MAGENTA + "  \__,_|\__\___||___/_| |_|\___|_|_| |_| |_|                       ",
    Fore.MAGENTA + "                 Boost Tools | ateshcim                            ",
    Fore.MAGENTA + "                This Tool By ateshcim | WasCode                    ",
    Fore.MAGENTA + "                     discord.gg/wascode                            ",
]
def open_discord_link():
    url = "https://discord.gg/wascode"
    webbrowser.open(url)

if __name__ == "__main__":
    open_discord_link()


def print_ascii_art():
    for line in ascii_art:
        print(line)


print_ascii_art()

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()

def clear():
  
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        clear()  
        print_ascii_art() 
        print(Fore.MAGENTA + "            If you want support, go to Discord wascode")
        print(Fore.BLUE + "____________________________________________")
        print(Fore.MAGENTA + "1 | Stock Tokens")
        print(Fore.MAGENTA + "2 | NickName")
        print(Fore.MAGENTA + "3 | Boost Server")
        print(Fore.BLUE + "____________________________________________")
        print(Fore.MAGENTA + "4 | Close Tool" + Style.RESET_ALL)

        choice = input(Fore.BLUE + "Write 1,2,3,4 To Open Tool`s | ")

        if choice == '1':
            os.system('python python/ateshcim3.py')
        elif choice == '3':
            os.system('python python/ateshcim1.py')
        elif choice == '2':
            os.system('python python/ateshcim2.py')
        elif choice == '4':
            break
        else:
            print(Fore.RED + "Write 1,2,3,4 To Open Tool`s  Only!!! " + Fore.RESET)
            time.sleep(2)  

if __name__ == "__main__":
    main()
