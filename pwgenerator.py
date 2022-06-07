# password generator by akarta
# import modules

import random
import time
try:
    from colorama import *
except ImportError:
    raise SystemExit('Please run › pip install colorama')


# password content
minu = "qwertyuiopasdfghjklzxcvbnm"
upper = minu.upper()
number = "0123456789"
simbols = "()[]{},.;:"

total = minu + upper + number + simbols
# What the password should be for
title = input("What the password should be for: ")
try:
    # Length of the password
    length = int(input("Length? "))

    # the password
    pw = "".join(random.sample(total, length))
except ValueError:
    raise SystemExit('Please, put a number < 73')

print("Generating a new password...")
time.sleep(2)
print(f"{Fore.GREEN}The password has been successfully generated")
# Write the variable title and the variable pw into the name of the chosen file.
file = "credentials.txt"  # if the file does not exist it will create one automatically
f = open(file, "a+")  # a+ = append mode
f.write("\r\n\n" + "Password for: " + title + " \npassword: " + pw)  # content written to the file
f.close()
input(f'{Fore.WHITE}Press enter to finish...')
