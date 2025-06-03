import hashlib
import getpass
import sys

print("!WARNING! --> Any password set using your 'initial' master password will NOT be accessible if you change it. Choose wisely.")
print("Had u changed that, you need to delete the data.json file, and hence start over !")
print("Press Ctrl-C to quit.\n")

while True:
    try:
        h1=hashlib.new("SHA256")
        master_password = getpass.getpass("Set your Password: ")
        h1.update(master_password.encode())
        value1 = h1.hexdigest()

        h2=hashlib.new("SHA256")
        master_password_confirm = getpass.getpass("Confirm your Password: ")
        h2.update(master_password.encode())
        value2 = h2.hexdigest()

        if(str(value1)==str(value2)):
            print("Password Confirmed! You can go an and access your keydock!")
            with open("hash.txt", "w") as hashtxt:
                hashtxt.write(str(value1))

            sys.exit()

        else:
            print("Password wrong! Try again!\n")

    except KeyboardInterrupt:
        print("Thank you for using Setup. See u later!")
        sys.exit()