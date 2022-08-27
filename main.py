import subprocess
import requests
import json
import os
from MeowerBot import Client
from colorama import Fore, Style
import notify2

c = Client("bot-username-goes-here","bot-password-goes-here",False) 

os.system('clear')

def sendmessage(title, message):
    notify2.init("Test")
    notice = notify2.Notification(title, message, '/home/sus/Downloads/icon_21.2ef6b9a3.svg')
    notice.show()
    return

def on_raw_msg(msg:dict):
        print(f'{Style.DIM}{Fore.YELLOW}MESSAGE: {Fore.RESET}{msg["u"]}: {msg["p"]}{Style.RESET_ALL}')
        msgu = msg["u"]
        msgp = msg["p"]
        sendmessage(msgu, msgp)
                
def on_login():
    print(f'{Fore.YELLOW}MEOWER: {Fore.RESET}Connected!')
    c.send_msg('Connected to Meower. Hello world!')
    

def on_error(error):
    print(f'{Fore.RED}ERROR: {Fore.RESET}{error}')
      
c.callback(on_raw_msg)
c.callback(on_error)
c.callback(on_login)

c.start()
