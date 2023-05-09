#!/usr/bin/python3
import subprocess, re, os
from datetime import datetime
from colorama import init, Fore, Style
import webbrowser

init()


def is_valid_url(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
        # domain
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(regex.match(url))
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
print( arachni_version + Style.RESET_ALL)

# Nhập url cần scan
url = input("Nhập URL: ")
while True:
    if is_valid_url(url):
        break
    else:
        print(Fore.RED + "Invalid URL..." + Style.RESET_ALL)
        url = input(Fore.YELLOW + "Input URL: " + Style.RESET_ALL)
filename = re.search("(?<=://)([a-zA-Z0-9\-\.]+)", url).group(
    1
) + datetime.now().strftime("%d%m%H%M%S")

print("Auto login: (y/n)")
autoLogin = ""
if input() == "y":
    urllogin = input(Fore.YELLOW + "Input URL: " + Style.RESET_ALL)
    while True:
        if is_valid_url(url):
            break
        else:
            print(Fore.RED + "Invalid URL..." + Style.RESET_ALL)
            urllogin = input(Fore.YELLOW + "Input URL: " + Style.RESET_ALL)
    parameter = input(Fore.YELLOW + "Input parameter: " + Style.RESET_ALL)
    check = input(Fore.YELLOW + "Input check: " + Style.RESET_ALL)
    autoLogin = '--plugin=autologin:url=' + urllogin + ',parameters="' + parameter + '",check="' + check + '" '

scope_include_pattern = url.split("?")[0]
# Chạy lệnh arachni để kiểm tra XSS trên trang web
command = (
    "./arachni/bin/arachni "
    + url
    + " --checks=*csrf* --report-save-path ./report/"
    + filename
    + ".afr " + autoLogin + " --scope-include-pattern=^"
    + scope_include_pattern
)
process = subprocess.Popen(
    command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
)
while process.poll() is None:
    output = process.stdout.readline().decode().rstrip()
    print(output)
process.communicate()
cmd_genHTML = (
    "./arachni/bin/arachni_reporter ./report/"
    + filename
    + ".afr --reporter=html:outfile=./report/"
    + filename
    + ".html.zip && unzip ./report/"
    + filename
    + ".html.zip -d ./report/"
    + filename
    + " && rm ./report/"
    + filename
    + ".html.zip"
)
process = subprocess.Popen(
    cmd_genHTML, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
)
while process.poll() is None:
    output = process.stdout.readline().decode().rstrip()
    print(output)
process.communicate()

idpath = "report/" + filename + "/index.html"
if os.path.exists(idpath):
    webbrowser.open(idpath, new=2)
    input("DONE!!!\nPlease Enter to continue")
else:
    print("Lỗi trong quá trình kiểm tra")
    input("DONE!!!\nPlease Enter to continue")
