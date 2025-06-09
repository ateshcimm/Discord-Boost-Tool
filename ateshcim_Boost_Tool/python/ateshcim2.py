import requests
import threading
import time
from colorama import Fore, Style, init
import base64
import json
import os

init(autoreset=True)

def mainHeader(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def change_nick_and_avatar_and_banner(server, nickname, token, avatar, banner):
    headers = mainHeader(token)

    r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers, json={"nick": nickname})
    nickname_changed = r.status_code == 200

   
    avatar_base64 = base64.b64encode(avatar).decode('utf-8')
    r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me", headers=headers, json={"avatar": f"data:image/png;base64,{avatar_base64}"})
    avatar_changed = r.status_code == 200

   
    banner_base64 = base64.b64encode(banner).decode('utf-8')
    r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me", headers=headers, json={"banner": f"data:image/png;base64,{banner_base64}"})
    banner_changed = r.status_code == 200

    token_display = token[:14] + "*" * (len(token) - 14)

    if nickname_changed and avatar_changed and banner_changed:
        print(f'{Fore.BLUE}[ ateshcim ]{Fore.YELLOW} Token | {Fore.CYAN}{token_display} {Fore.GREEN} a and b and name is nice{Fore.RESET}')
    else:
        print(f'{Fore.RED}[ ateshcim ] {Fore.YELLOW} Falid Error | {Fore.CYAN}{token_display}{Fore.RESET}')

def main():
    date_folder = 'python'

    
    config_path = os.path.join(date_folder, 'ateshcim.json')
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    
    server = config["server_id"]
    nick = config["nickname"]
    
  
    avatar_path = os.path.join(date_folder, 'ateshcim.png')
    with open(avatar_path, "rb") as image_file:
        avatar = image_file.read()
    
    
    banner_path = os.path.join(date_folder, 'ateshcim.png')
    with open(banner_path, "rb") as banner_file:
        banner = banner_file.read()

   
    tokens_path = os.path.join(date_folder, 'token.txt')
    tokens = open(tokens_path, 'r').read().splitlines()
    
    for token in tokens:
        threading.Thread(target=change_nick_and_avatar_and_banner, args=(server, nick, token, avatar, banner)).start()
    
    time.sleep(3)
    input(f'{Fore.MAGENTA}hi i`m ateshcim wascode team price any key for close | {Fore.RESET}')

if __name__ == "__main__":
    main()
