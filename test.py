import os,json
from colorama import init, Fore, Style
import keyboard
import re

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(regex.match(url))
    
# Khởi tạo colorama
init()

# Tạo menu và tuỳ chọn
options = json.loads(open("options.json", "r",encoding='utf-8').read())

# Hiển thị menu
def display_menu():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print(Fore.GREEN + "_______________MENU___________________")
    for key, value in options.items():
        print(Fore.BLUE + key + ". " + value["name"])
    print(Style.RESET_ALL)


# Hiển thị tuỳ chọn
def display_options(selected_option):
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    if selected_option.isnumeric():
        print(Fore.GREEN + "_______________" + options[selected_option]["name"].upper() + "___________________")
        for key, value in options[selected_option]["options"].items():
            print(Fore.BLUE + key + ". " + value["name"])
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "_______________" + options[selected_option]["name"].upper() + "___________________")
        
# Hiển thị tuỳ chọn con
def display_sub_options(selected_option,selected_sub_option):
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print(Fore.GREEN + "_______________" + options[selected_option]["name"].upper() + "___________________")
    for key, value in options[selected_option]["options"][selected_sub_option]["options"].items():
        print(Fore.BLUE + key + ". " + value["name"])
    print(Style.RESET_ALL)

# Nhập giá trị cho tuỳ chọn
def input_option_value(option_name):
    value = input(Fore.YELLOW + option_name + " = " + Style.RESET_ALL)
    return value.strip()


# Hiển thị các giá trị đã nhập
def display_values(values):
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print(Fore.GREEN + "_______________VALUES___________________")
    for key, value in values.items():
        print(Fore.BLUE + value["name"] + ": " + Fore.YELLOW + value["value"])
    print(Style.RESET_ALL)

def processNumber(selected_option):
    choice = selected_option
    try:
        selected_sub_option = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
        selected_option = selected_option.upper()
        while True:
            if selected_sub_option in options[selected_option]["options"].keys():
                break
            else:
                display_options(selected_option)
                print(Fore.RED + "Invalid sub-option. Please choose again." + Style.RESET_ALL)
                selected_sub_option = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
                selected_option = selected_option.upper()
        option_name = options[selected_option]["options"][selected_sub_option]["name"]
        try:
            if options[selected_option]["options"][selected_sub_option]["options"] is not None:
                while True:
                    display_sub_options(selected_option,selected_sub_option)
                    selected_sub_option_name = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
                    selected_option = selected_option.upper()
                    if selected_sub_option_name in options[selected_option]["options"][selected_sub_option]["options"].keys():
                        break
                    else:
                        print(Fore.RED + "Invalid sub-option. Please choose again." + Style.RESET_ALL)
                option_name = options[selected_option]["options"][selected_sub_option]["options"][selected_sub_option_name]["name"]
                option_arg = options[selected_option]["options"][selected_sub_option]["options"][selected_sub_option_name]["arg"]
                option_value = input_option_value(option_name)
                values[selected_option] = {"name": option_name, "value": option_value, "arg":option_arg}
                # args.append(values[selected_option])
                display_values(values)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                selected_option = ""

        except:
            if choice != "1":
                option_value = input_option_value(option_name)
                option_arg = options[selected_option]["options"][selected_sub_option]["arg"]
                values[selected_option] = {"name": option_name, "value": option_value, "arg":option_arg}
                # args.append(values[selected_option])
                display_values(values)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                selected_option = ""
            else:
                option_value = ""
                option_arg = options[selected_option]["options"][selected_sub_option]["arg"]
                values[selected_option] = {"name": option_name, "value": option_value, "arg":option_arg}
                # args.append(values[selected_option])
                display_values(values)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                selected_option = ""
                
    except Exception as e:
        print(Fore.RED + "Invalid option. Please choose again. \n"+ e + Style.RESET_ALL)

def processString(selected_option):
    if selected_option != "U":
        option_value = input_option_value(options[selected_option]["name"])
        values[selected_option] = {"name": options[selected_option]["name"], "value": option_value}
        # args.append(values[selected_option])
        display_values(values)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        selected_option = ""
    elif selected_option == "U":
        option_value = input_option_value(options[selected_option]["name"])
        while True:
            if is_valid_url(option_value):
                break
            else:
                print(Fore.RED + "Invalid URL..." + Style.RESET_ALL)
                option_value = input_option_value(options[selected_option]["name"])

        values[selected_option] = {"name": options[selected_option]["name"], "value": option_value} 
        display_values(values)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        selected_option = ""

def showAllValues():
    for key, value in values.items():
        print(Fore.BLUE + value["name"] + ": " + Fore.YELLOW + value["value"])
    print(Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

def processCommand(values):
    cmd = "./archni "
    if os.name == "nt":
        cmd = "./archni.exe "    
    for key, value in values.items():
        cmd += key + "=" + value["value"] + " "
    os.system(cmd)
    
# Chương trình chính
selected_option = ""
values = {}
args = []
while True:
    if keyboard.is_pressed('ctrl+c'):
        print(Fore.RED + "Exiting....." + Style.RESET_ALL)
        exit(1)
    if selected_option == "E" or selected_option == "e":
                print(Fore.RED + "Exiting....." + Style.RESET_ALL)
                exit(1)
    try:
        if not selected_option:
            display_menu()
            selected_option = input(Fore.YELLOW + "Select option: " + Style.RESET_ALL)
            selected_option = selected_option.upper()
        else:
            display_options(selected_option)
            if selected_option.isnumeric():
                processNumber(selected_option)
                selected_option = ""
            elif selected_option != "R" and selected_option !="S" and not selected_option.isnumeric():
                processString(selected_option)
                selected_option = ""
            elif selected_option == "R":
                if len(values) == 0:
                    input(Fore.RED + "Please select at least one option.\nEnter to continue" + Style.RESET_ALL)
                    selected_option = ""
                elif len(values) >= 1 and "U" in values.keys() and values["U"]["value"] != "":
                    cmd = "./archni.exe " + values["U"]["value"] + " "
                    for key, value in values.items():
                        if key != "U":
                            cmd += value['arg'] + " " + value["value"] + " "
                    selected_option = ""
                    input(cmd)
                    
                else:
                    input(Fore.RED + "Please input URL value.\nEnter to continue" + Style.RESET_ALL)
                    selected_option = ""
            elif selected_option == "S":
                showAllValues()
                selected_option = ""
    except:
        if keyboard.is_pressed('ctrl+c'):
            print(Fore.RED + "Exiting....." + Style.RESET_ALL)
            exit()
        if selected_option not in options.keys():
            selected_option = ""

