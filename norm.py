import os

print("Mini OS 1.0 | Based off of GNU bash https://www.gnu.org/software/bash/!")
while True:
    
    com = input("#/DOS/Mini OS>    ")

    os.system(com)

if com == "help":
    os.system("cat help.txt")

