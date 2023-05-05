import os

report_dir = "report"
dirnames = [name for name in os.listdir(report_dir) if os.path.isdir(os.path.join(report_dir, name))]

print("List of directories in report folder:")
for name in dirnames:
    print(name)
