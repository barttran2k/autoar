import os,json
from colorama import init, Fore, Style

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
    print(Fore.GREEN + "_______________" + options[selected_option]["name"].upper() + "___________________")
    for key, value in options[selected_option]["options"].items():
        print(Fore.BLUE + key + ". " + value["name"])
    print(Style.RESET_ALL)
    
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
    return value


# Hiển thị các giá trị đã nhập
def display_values(values):
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print(Fore.GREEN + "_______________VALUES___________________")
    for key, value in values.items():
        print(Fore.BLUE + value["name"] + ": " + Fore.YELLOW + value["value"])
    print(Style.RESET_ALL)

# Chương trình chính
selected_option = ""
values = {}
while selected_option != "16":
    try:
        if not selected_option:
            display_menu()
            selected_option = input(Fore.YELLOW + "Select option: " + Style.RESET_ALL)
        else:
            display_options(selected_option)
            selected_sub_option = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
            while True:
                if selected_sub_option in options[selected_option]["options"].keys():
                    break
                else:
                    display_options(selected_option)
                    print(Fore.RED + "Invalid sub-option. Please choose again." + Style.RESET_ALL)
                    selected_sub_option = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
            option_name = options[selected_option]["options"][selected_sub_option]["name"]
            try:
                if options[selected_option]["options"][selected_sub_option]["options"] is not None:
                    while True:
                        display_sub_options(selected_option,selected_sub_option)
                        selected_sub_option_name = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
                        if selected_sub_option_name in options[selected_option]["options"][selected_sub_option]["options"].keys():
                            break
                        else:
                            print(Fore.RED + "Invalid sub-option. Please choose again." + Style.RESET_ALL)
                    option_name = options[selected_option]["options"][selected_sub_option]["options"][selected_sub_option_name]["name"]
                    option_value = input_option_value(option_name)
                    values[selected_sub_option] = {"name": option_name, "value": option_value}
                    display_values(values)
                    input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                    selected_option = ""
            except:
                option_value = input_option_value(option_name)
                values[selected_sub_option] = {"name": option_name, "value": option_value}
                display_values(values)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
                selected_option = ""

    except:
        if KeyboardInterrupt:
            print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
            exit()
        print(Fore.RED + "Invalid option. Please choose again." + Style.RESET_ALL)
        selected_option = ""
        