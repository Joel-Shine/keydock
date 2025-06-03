# keydock
A command line utility, that can securely store all your passwords, hassle-free.

**How to use keydock**
----------------------
First run the 'setup_password.py' file as we need to set a master password inorder to access all our passwords. This has to be done only once.
**IMPORTANT NOTE**--> All passwords set by your intial master password cannot be accessed if you change your master password. So set up wisely.

Next, you can run the 'keydock.py' file and start entering, deleting or editing password for your various websites, accounts etc. It has autocompletion feature, helping you to seamlessly access all your passwords, securely and quickly.

**Working Principle**
---------------------
Firstly, keydock will create a hash (according to SHA256) of your master password, which is stored in a file and should not be deleted. Next, everytime you run 'keydock.py', it will create a 
base64 string of your master password, which will essentially acts as a key to encrypt passwords of your individual websites and store them securely in a json file. The main takeaway is that, this key is 
generated only on memory and hance cannot be accessed by other people in any way, unless they have a keylogger installed on your computer. This way, it stores all your passwords in an encrypted format, locally,
and without having to go to google password manager for everything.
