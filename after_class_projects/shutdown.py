
import os

choice = input("do you really want to shut down? ").lower()

if choice == "yes":
    os.system("shutdown /s /t 1")
else:
    print("shutdown cancelled")
