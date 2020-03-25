# pythonbin.py
# A 1970s style OS made in the 2020s

import os
print("What Boot Option would you like?")
boot = input("1) Normal mode 2) Debug mode 3) Bash\n")
if boot == "1":
    os.system("python3 norm.py")
elif boot == "2":
    os.system("python3 debug.py")
elif boot == "3":
    os.system("python3 comp.py")
elif boot == "4":
    while True:    
        wish = input("command: ")
        os.system("wish")
