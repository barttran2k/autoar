import os
from colorama import init, Fore, Style

# Khởi tạo colorama
init()

# Tạo menu và tuỳ chọn
options = {
    "1": {
        "name": "Generic",
        "options": {
            "1": {"name": "Version (--version)", "value": ""},
            "2": {"name": "Authorized by (--authorized-by)", "value": ""},
            "3": {"name": "Daemon friendly (--daemon-friendly)", "value": ""},
        },
    },
    "2": {
        "name": "Output",
        "options": {
            "1": {"name": "Verbose (--output-verbose)", "value": ""},
            "2": {"name": "Debug (--output-debug)", "value": ""},
            "3": {"name": "Only positives (--output-only-positives)", "value": ""},
        },
    },
    "3": {
        "name": "Scope",
        "options": {
            "1": {"name": "Include (--scope-include-pattern)", "value": ""},
            "2": {"name": "Include subdomains (--scope-include-subdomains)", "value": ""},
            "3": {"name": "Exclude (--scope-exclude-pattern)", "value": ""},
            "4": {"name": "Exclude page by content (--scope-exclude-content-pattern)", "value": ""},
            "5": {"name": "Exclude binaries (--scope-exclude-binaries)", "value": ""},
            "6": {"name": "Redundant paths (--scope-redundant-path-pattern)", "value": ""},
            "7": {"name": "Auto-redundant (--scope-auto-redundant)", "value": ""},
            "8": {"name": "Directory depth limit (--scope-directory-depth-limit)", "value": ""},
            "9": {"name": "Page limit (--scope-page-limit)", "value": ""},
            "10": {"name": "Extend paths (--scope-extend-paths)", "value": ""},
            "11": {"name": "Restrict paths (--scope-restrict-paths)", "value": ""},
            "12": {"name": "URL rewrite (--scope-url-rewrite)", "value": ""},
            "13": {"name": "DOM depth limit (--scope-dom-depth-limit)", "value": ""},
            "14": {"name": "DOM event limit (--scope-dom-event-limit)", "value": ""},
            "15": {"name": "HTTPS only (--scope-https-only)", "value": ""},
        },
    },
    "4": {
        "name": "Audit",
        "options": {
        "1": {"name": "Links (--audit-links)", "value": ""},
        "2": {"name": "Forms (--audit-forms)", "value": ""},
        "3": {"name": "Cookies (--audit-cookies)", "value": ""},
        "4": {"name": "Cookies extensively (--audit-cookies-extensively)", "value": ""},
        "5": {"name": "Headers (--audit-headers)", "value": ""},
        "6": {"name": "Link template (--audit-link-template)", "value": ""},
        "7": {"name": "JSONs (--audit-jsons)", "value": ""},
        "8": {"name": "XMLs (--audit-xmls)", "value": ""},
        "9": {"name": "UI Inputs (--audit-ui-inputs)", "value": ""},
        "10": {"name": "UI Forms (--audit-ui-forms)", "value": ""},
        "11": {"name": "Parameter names (--audit-parameter-names)", "value": ""},
        "12": {"name": "With extra parameter (--audit-with-extra-parameter)", "value": ""},
        "13": {"name": "With both methods (--audit-with-both-methods)", "value": ""},
        "14": {"name": "Exclude vector (--audit-exclude-vector)", "value": ""},
        "15": {"name": "Include vector (--audit-include-vector)", "value": ""},
        }
    },
    "5": {
        "name": "HTTP",
        "options": {
        "1": {"name": "User agent (--http-user-agent)", "value": ""},
        "2": {"name": "Request concurrency (--http-request-concurrency)", "value": ""},
        "3": {"name": "Request timeout (--http-request-timeout)", "value": ""},
        "4": {"name": "Request delay (--http-request-delay)", "value": ""},
        "4": {"name": "Request redirect limit (--http-request-redirect-limit)", "value": ""},
        "5": {"name": "Request queue size (--http-request-queue-size)", "value": ""},
        "6": {"name": "Request header (--http-request-header)", "value": ""},
        "7": {"name": "Response max size (--http-response-max-size)", "value": ""},
        "8": {"name": "Cookie-jar (--http-cookie-jar)", "value": ""},
        "9": {"name": "Cookie string (--http-cookie-string)", "value": ""},
        "10": {
            "name": "Authentication",
            "options": {
            "1": {"name": "Username (--http-authentication-username)", "value": ""},
            "2": {"name": "Password (--http-authentication-password)", "value": ""},
            "3": {"name": "Type (--http-authentication-type)", "value": ""},
            },
        },
        "11": {"name": "Proxy (--http-proxy)", "value": ""},
        "12": {"name": "Proxy authentication (--http-proxy-authentication)", "value": ""},
        "13": {"name": "Proxy type (--http-proxy-type)", "value": ""},
        "14": {"name": "SSL verify peer (--http-ssl-verify-peer)", "value": ""},
        "15": {"name": "SSL verify host (--http-ssl-verify-host)", "value": ""},
        "16": {"name": "SSL certificate (--http-ssl-certificate)", "value": ""},
        "17": {"name": "SSL certificate type (--http-ssl-certificate-type)", "value": ""},
        "18": {"name": "SSL key (--http-ssl-key)", "value": ""},
        "19": {"name": "SSL key type (--http-ssl-key-type)", "value": ""},
        "20": {"name": "SSL key password (--http-ssl-key-password)", "value": ""},
        "21": {"name": "SSL CA (--http-ssl-ca)", "value": ""},
        "22": {"name": "SSL CA directory (--http-ssl-ca-directory)", "value": ""},
        "23": {"name": "SSL version (--http-ssl-version)", "value": ""},
        },
    },
    
}

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
    
# Hiển thị tuỳ chọn
def display_suboptions(selected_option):
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình
    print(Fore.GREEN + "_______________" + options[selected_option]["name"].upper() + "___________________")
    for key, value in options[selected_option]["options"].items():
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
while True:
    if not selected_option:
        display_menu()
        selected_option = input(Fore.YELLOW + "Select option: " + Style.RESET_ALL)
    else:
        display_options(selected_option)
        selected_sub_option = input(Fore.YELLOW + "Select sub-option: " + Style.RESET_ALL)
        option_name = options[selected_option]["options"][selected_sub_option]["name"]
        if options[selected_option]["options"][selected_sub_option]["options"] is not None:
            optiont = options[selected_option]["options"][selected_sub_option]["options"]
            display_suboptions(optiont)
            selected_optionsub = input(Fore.YELLOW + "Select subsub-option: " + Style.RESET_ALL)
            option_name = optiont[selected_optionsub]["name"]
            
        option_value = input_option_value(option_name)
        values[selected_sub_option] = {"name": option_name, "value": option_value}
        display_values(values)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        selected_option = ""

