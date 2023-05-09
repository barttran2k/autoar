#!/usr/bin/python3
import subprocess,re,os
from datetime import datetime
import webbrowser

# Nhập url cần scan
url = input("Nhập URL: ")
filename =  re.search("(?<=://)([a-zA-Z0-9\-\.]+)", url).group(1) + datetime.now().strftime("%d%m%H%M%S")

# Chạy lệnh arachni để kiểm tra XSS trên trang web
command = "./arachni/bin/arachni " + url + " --checks=xss* --report-save-path ./report/"+ filename + ".afr "
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
while process.poll() is None:
    output = process.stdout.readline().decode().rstrip()
    print(output)
process.communicate()
cmd_genHTML = './arachni/bin/arachni_reporter ./report/' + filename + '.afr --reporter=html:outfile=./report/' + filename + \
                                '.html.zip && unzip ./report/' + filename + '.html.zip -d ./report/' + \
                                filename+' && rm ./report/' + filename + '.html.zip'
process = subprocess.Popen(
    cmd_genHTML, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
while process.poll() is None:
    output = process.stdout.readline().decode().rstrip()
    print(output)
process.communicate()

idpath = "report/"+filename+"/index.html"
if os.path.exists(idpath):
    webbrowser.open(idpath,new=2)
    input("DONE!!!\nPlease Enter to continue")
else:
    print("Lỗi trong quá trình kiểm tra")
    input("DONE!!!\nPlease Enter to continue")