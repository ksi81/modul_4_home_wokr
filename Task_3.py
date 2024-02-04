#Третє завдання
#для зміни поточної директорії: cd /Users/sleeper/Documents/GoIt-Python/HomeWork_4/modul_4_home_wokr
# Зауск вірутального отченні: python3 -m venv venv

import os
import sys
from colorama import Fore, Style, init

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        
        if level == 0:
            print(f'{Fore.CYAN}{Style.BRIGHT}{os.path.basename(root)}{Style.RESET_ALL}')
        else:
            print(f'{indent}{Fore.YELLOW}{Style.BRIGHT}{os.path.basename(root)}{Style.RESET_ALL}/')
            
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{subindent}{Fore.WHITE}{file}{Style.RESET_ALL}')
        for dir_name in dirs:
            print(f'{subindent}{Fore.CYAN}{Style.BRIGHT}{dir_name}{Style.RESET_ALL}/')

if __name__ == "__main__":
    # Шлях до директорії
    directory_path = "/Users/sleeper/Documents/GoIt-Python/HomeWork_4/modul_4_home_wokr"

    # Ініціалізація colorama
    init()

    # Виведення структури директорії
    list_files(directory_path)
