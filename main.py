from colorama import init, Fore, Style
import subprocess, re, os
from templateScan import ArachniScanner
init()
# Ch3ck report f0ld3r
if not os.path.exists("report"):
    os.makedirs("report")
    print("Created 'report' folder.")
else:
    print("'report' folder already exists.")
    
while True:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(''' ____             _  _______ _____ __  __ 
|  _ \           | ||__   __/ ____|  \/  |
| |_) | __ _  ___| |__ | | | |    | \  / |
|  _ < / _` |/ __| '_ \| | | |    | |\/| |
| |_) | (_| | (__| | | | | | |____| |  | |
|____/ \__,_|\___|_| |_|_|  \_____|_|  |_|\n''')
    try:
        status_ar = subprocess.check_output(['./arachni/bin/arachni', '--version']).decode('utf-8')
        match = re.search(r'Arachni ([\d\.]+)', status_ar)
        arachni_version = ""
        if match:
            arachni_version = "Arachni version: "+Fore.YELLOW+(match.group(1))
        else:
            arachni_version = "Arachni not found"
    except:
        arachni_version = "Arachni not found"   
    print(arachni_version + Style.RESET_ALL)
    print(Fore.RED + "________________Load Script______________\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Auto XSS, SQLi, CSRF" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Full Script" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Exit" + Style.RESET_ALL)
    print(Fore.RED + "_________________________________________" + Style.RESET_ALL)
    print()
    print()
    choice = input(Fore.YELLOW + "Choice: " + Style.RESET_ALL)
    scan = ArachniScanner()
    if choice == '1':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(Fore.RED + "________________Auto XSS, SQLi, CSRF______________\n" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. XSS" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. SQLi" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. CSRF" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Back" + Style.RESET_ALL)
        print(Fore.RED + "__________________________________________________" + Style.RESET_ALL)
        print()
        print()
        choice = input(Fore.YELLOW + "Choice: " + Style.RESET_ALL)
        if choice == '1':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            scan.scanXSS()
        elif choice == '2':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            scan.scanSQL()
        elif choice == '3':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            scan.scanCSRF()
    elif choice == '2':
        import scriptArachni
    elif choice == '3':
        break
print(Fore.RED + "Exitting...\n" + Style.RESET_ALL)
