from colorama import init, Fore, Style

init()
while True:
    print(''' ____             _  _______ _____ __  __ 
|  _ \           | ||__   __/ ____|  \/  |
| |_) | __ _  ___| |__ | | | |    | \  / |
|  _ < / _` |/ __| '_ \| | | |    | |\/| |
| |_) | (_| | (__| | | | | | |____| |  | |
|____/ \__,_|\___|_| |_|_|  \_____|_|  |_|\n''')
    print(Fore.RED + "________________Load Script______________\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Auto XSS, SQLi, CSRF" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Full Script" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Exit" + Style.RESET_ALL)
    print(Fore.RED + "_________________________________________" + Style.RESET_ALL)
    print()
    print()
    choice = input(Fore.YELLOW + "Choice: " + Style.RESET_ALL)
    if choice == '1':
        print(Fore.RED + "________________Auto XSS, SQLi, CSRF______________\n" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. XSS" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. SQLi" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. CSRF" + Style.RESET_ALL)
        print(Fore.RED + "__________________________________________________" + Style.RESET_ALL)
        print()
        print()
        choice = input(Fore.YELLOW + "Choice: " + Style.RESET_ALL)
        if choice == '1':
            import autoXSS
        elif choice == '2':
            import autoSQLi
        elif choice == '3':
            import autoCSRF
    elif choice == '2':
        import scriptArachni
    elif choice == '3':
        break
print(Fore.RED + "Exitting...\n" + Style.RESET_ALL)
