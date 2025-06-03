from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
import sys
import os
from cryptography.fernet import Fernet
import getpass
import json
import hashlib
import base64
import platform
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
import time

### Entering the master password to access the database !

h=hashlib.new("SHA256")

master_password = getpass.getpass("Password: ")

h.update(master_password.encode())

value = h.hexdigest()

with open("hash.txt") as hashtxt:
  the_hash = hashtxt.read()

if(the_hash==str(value)):
    print("Authentication Successfull !")

    def string_to_base64_key(input_string):
        encoded_string = input_string.encode('utf-8')
        hashed_string = hashlib.sha256(encoded_string).digest()
        base64_encoded = base64.b64encode(hashed_string).decode('utf-8')
        return base64_encoded

    base64_key = string_to_base64_key(master_password)

else:
    print("Wrong! Denied access to password manager.")
    sys.exit()

def bottom_toolbar():
    return HTML('Press <b><style bg="#be2100">Ctrl-C</style></b> to quit.')

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})



if platform.system()=="Windows":
    os.system("cls")
else:
    os.system("clear")

###### database related------------------------------------------------

print_formatted_text(FormattedText([
    ('#00be80', 
'''
██╗  ██╗███████╗██╗   ██╗██████╗  ██████╗  ██████╗██╗  ██╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝
█████╔╝ █████╗   ╚████╔╝ ██║  ██║██║   ██║██║     █████╔╝ 
██╔═██╗ ██╔══╝    ╚██╔╝  ██║  ██║██║   ██║██║     ██╔═██╗ 
██║  ██╗███████╗   ██║   ██████╔╝╚██████╔╝╚██████╗██║  ██╗
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝    v1.0
'''
     ),
]))

key=str(base64_key)

f = Fernet(key)

passdict={}
autolist=[]

while True:
    try:
        with open('data.json','r') as file:
            dic = json.load(file)

            for key in dic.keys():
                autolist.append(key)

    except json.decoder.JSONDecodeError:
        print("")

    html_completer = WordCompleter(autolist)

    try:
        print("\nDo you want to get(g), add(a), edit(e) , list(l) or remove(r) new password? (Press 'q' to quit)")
        ans = prompt("> ", bottom_toolbar=bottom_toolbar)

        if ans=="a":
            item=prompt("What is the password for? > ", bottom_toolbar=bottom_toolbar, completer=html_completer, style=style)
            password = getpass.getpass("Password: ")

            try:
                passdict[item]=str(f.encrypt(password.encode()))
            except KeyError:
                print("Sorry! wrong item name. Try later.")
                continue
        
            try:
                with open('data.json','r') as file:
                    dic = json.load(file)
                    dic.update(passdict)

                with open('data.json','w') as file1:
                    json.dump(dic, file1)

            except json.decoder.JSONDecodeError:
                with open('data.json','w') as file2:
                    json.dump(passdict, file2)

        elif ans=="l":
            print("Listing all items for which passwords are saved:\n")
            try:
                with open('data.json','r') as file:
                    dic = json.load(file)

                    i=0
                    for key in dic.keys():
                        i+=1
                        print_formatted_text(FormattedText([
                            ('#d1e4de', str(i)),
                            ('', '. '),
                            ('#00be80 bold', key),
                        ]))

            except json.decoder.JSONDecodeError:
                print("No passwords in data to list. Try again later.")

        elif ans=="r":
            item=prompt("For what do you want to remove your password? > ", bottom_toolbar=bottom_toolbar, completer=html_completer, style=style)
        
            try:
                with open('data.json','r') as file:
                    dic = json.load(file)

                    try:
                        dic.pop(item)
                    except KeyError:
                        print("Sorry! wrong item name. Try later.")
                        continue

                with open('data.json','w') as file1:
                    json.dump(dic, file1)

            except json.decoder.JSONDecodeError:
                print("No passwords in data. Try again later.")

            print("\nPassword for "+item+" successfully removed !")

        elif ans=="e":
            item=prompt("For what do you want to edit your password? > ", bottom_toolbar=bottom_toolbar, completer=html_completer, style=style)
        
            password = getpass.getpass("Enter New Password: ")
        
            try:
                with open('data.json','r') as file:
                    dic = json.load(file)
                    
                    try:
                        dic.pop(item)
                    except KeyError:
                        print("Sorry! wrong item name. Try later.")
                        continue

                    passdict[item]=str(f.encrypt(password.encode()))
                    dic.update(passdict)

                with open('data.json','w') as file1:
                    json.dump(dic, file1)

            except json.decoder.JSONDecodeError:
                print("No passwords in data. Try again later.")

            print("\nPassword for "+item+" successfully edited !")

        elif ans=="g":
            item=prompt("For what do you want to retrieve your password? > ", bottom_toolbar=bottom_toolbar, completer=html_completer, style=style)

            try:
                with open('data.json', 'r') as openfile:
                    json_object = json.load(openfile)
                
                try:
                    password = json_object[item].replace("b'","").replace("'","")
                except KeyError:
                    print("Sorry! wrong item name. Try later.")
                    continue

                password = password.encode()

                password = str(f.decrypt(password)).replace("b'","")
                password = password.replace("'","")

                print("Your password = "+password)

            except json.decoder.JSONDecodeError:
                print("No passwords in data. Try again later.")

        elif ans=="q":
            if platform.system()=="Windows":
                print("\n\nThank you for using KeyDock!")
                time.sleep(1.5)
                os.system("cls")

            else:
                print("\n\nThank you for using KeyDock!")
                time.sleep(1.5)
                os.system("clear")

            sys.exit()

        else:
            print("Sorry, wrong input. Try again.")

        autolist.clear()


    except KeyboardInterrupt:
        if platform.system()=="Windows":
            print("\n\nThank you for using KeyDock!")
            time.sleep(1.5)
            os.system("cls")
        else:
            print("\n\nThank you for using KeyDock!")
            time.sleep(1.5)
            os.system("clear")

        sys.exit()