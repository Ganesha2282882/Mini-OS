import os


os.system("cp -R Program-Files backups")
os.system("cp -R Downloads backups")
os.system("cp -R Docs backups")
os.system("cp -R Desktop backups")
os.system("cp MAIN.sh backups")
print("[Debugged Version] Mini OS 1.0 | Based off of GNU bash https://www.gnu.org/software/bash/!")
while True:
    
    com = input("DB/DOS/Mini OS>    ")

    os.system(com)

if com == "help":
    os.system("cat help.txt")

