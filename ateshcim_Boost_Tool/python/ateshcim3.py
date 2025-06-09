from colorama import Fore as color
from colorama import init
from time import sleep
import time
import datetime
from datetime import datetime

init(convert=True)

class Main:

    @staticmethod
    def _time():
        return time.strftime("%H:%M:%S", time.gmtime())
    
    @staticmethod
    def sprint(content: str) -> None:
        print(f"[{color.MAGENTA}{Main()._time()}{color.RESET}] {content}")

 
    @staticmethod
    def findToken(token):
        if ':' in token:
            token_chosen = None
            tokensplit = token.split(":")
            for thing in tokensplit:
                if '@' not in thing and '.' in thing and len(thing) > 30:
                    token_chosen = thing
                    break
            if token_chosen is None:
                print(f"Error finding token")
                return None
            else:
                return token_chosen
        else:
            return token

    @staticmethod
    def removeToken(token: str):
        with open('python/ateshcim.txt', "r") as f:
            Tokens = f.read().split("\n")
            for t in Tokens:
                if len(t) < 5 or t == token:
                    Tokens.remove(t)
            open("python/ateshcim.txt", "w").write("\n".join(Tokens))

    @staticmethod
    def write(file, token: str):
        with open(file, "a") as f:
            f.write(token + "\n")
            f.close()

    @staticmethod
    def remove(file, token: str):
        with open(file, "a") as f:
            f.pop(token)
            f.close()

    @staticmethod
    def getAllTokens(filename):
        all_tokens = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                token = line.strip()
                token = Main().findToken(token)
                if token is not None:
                    all_tokens.append(token)
        return all_tokens

def SORTER():
    
    tokens = Main().getAllTokens("python/ateshcim.txt")
    start_time = int(datetime.now().strftime("%S"))
    total_hits = 0
    for token in tokens:
        Main().sprint(f"[{color.GREEN}SUCCESS{color.RESET}] Pulled token -> {color.LIGHTBLACK_EX}{token}{color.RESET}")
        total_hits += 1
        
        with open("python/token.txt", "a") as f:
            f.write(token + "\n")
            f.close()

    with open("python/ateshcim.txt", "w") as file: 
        file.truncate(0) 
        file.close()
    
    finished_time = int(datetime.now().strftime("%S"))
    elapsed = abs(start_time - finished_time)
    Main().sprint(f"[{color.RED}Hi I`m ateshcim wascode Team{color.RESET}] Complete | Time / {elapsed} | Total /{total_hits}")
    sleep(3)

if __name__ == "__main__":
    SORTER()
