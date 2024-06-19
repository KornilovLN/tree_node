# utils.py
import sys
import platform
import os

def techinfo():
    with open(os.path.join(os.path.dirname(__file__), 'materials/techinfo.txt'), 'r') as f:
        techinfo_text = f.read()

    print(techinfo_text)
    print("__________________________")
    print("Сведения о платформе:")
    print(sys.version_info)
    print("SYS version: ", sys.version)
    print("Python Version: ", platform.python_version())
    print("Python Executable Path: ", sys.executable)
    print("__________________________\n")

def selfdoc():
    with open(os.path.join(os.path.dirname(__file__), 'materials/selfdoc.txt'), 'r') as f:
        selfdoc_text = f.read()

    print(selfdoc_text)

def About():
    with open(os.path.join(os.path.dirname(__file__), 'materials/about.txt'), 'r') as f:
        about_text = f.read()

    print(about_text)

def read_css_file(file_path):
    try:
        with open(file_path, 'r') as f:
            css_content = f.read()
        return css_content
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return ""    
    
def Hi():
    # Выводим документацию
    selfdoc()
    # Выводим сообщение об авторе
    About()
    # Выводим информацию о среде
    techinfo()        