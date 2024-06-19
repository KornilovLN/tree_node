#!/usr/bin/python3
# -*- coding: utf-8 -*-

#--------------------------------------------------
#--- <<< Новая ветка разработки tree_node_2 >>> !!!
#--------------------------------------------------

import os
import sys
import platform
import shutil

import utils

# Путь к файлу style.css в текущей директории - там, где и tree_node
# и его надо перенести в папку генерируемого сайта (сложно, но на будущее)
styles_css_path = os.path.join(os.path.dirname(__file__), 'materials', 'style.css')

# Читаем содержимое файла styles.css в переменную для дальнейшего переноса
# его в папку styles генерируемого проекта
CSS = utils.read_css_file(styles_css_path)


# Путь к директории со скриптами в текущей директории - там, где и tree_node
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')


class TreeNode:
    def __init__(self, value, file_name, level=0):
        self.value = value          # Значение узла
        self.file_name = file_name  # Имя файла
        self.level = level          # Уровень вложенности узла
        self.left = None            # Левый поддерево
        self.right = None           # Правый поддерево
        self.glPath = ""  # Инициализируем glPath как атрибут класса

        # Сразу создаем директорию и файл стилей корневого узла
        if file_name == "first":
            self.create_styles_directory_and_file(file_name)

        # Определяем путь к папке scripts в текущей директории
        #scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
        

    # Создаем директорию и файл стилей корневого узла
    def create_styles_directory_and_file(self, file_name):
        # Определяем путь к директории и файлу
        styles_dir = os.path.join(self.file_name, 'styles')
        style_file = os.path.join(styles_dir, 'style.css')
        
        # Создаем директорию, если она не существует
        if not os.path.exists(styles_dir):
            os.makedirs(styles_dir)
            print(f"Directory 'styles' created at {styles_dir}")
        else:
            print(f"Directory 'styles' already exists at {styles_dir}")
        
        # Создаем пустой файл style.css, если он не существует
        if not os.path.exists(style_file):
            with open(style_file, 'w') as file:
                # Записываем в файл стили
                file.write(CSS)
            print(f"File 'style.css' created at {style_file}")
        else:
            print(f"File 'style.css' not finded at {style_file}")
        #    print(f"File 'style.css' already exists at {style_file}")

        '''
        # Получаем путь к корневой папке first
        first_dir = os.path.dirname(file_name)
        # Создаем путь к папке scripts в корневой папке first
        dest_scripts_dir = os.path.join(first_dir, 'scripts')
        # Копируем папку scripts в корневую папку first
        shutil.copytree(scripts_dir, dest_scripts_dir)
        '''

    # Создаем HTML файл для текущего узла
    def pre_order(self, node, path="", parent_file_name="", level=0):
        if node:            
            # Обновляем уровень узла
            node.level = level
            
            # Создаем HTML файл для текущего узла
            self.create_html_file(node, path, parent_file_name)

            # Рекурсивный обход левого и правого поддерева
            if node.left:
                self.pre_order(node.left, os.path.join(path, node.file_name), node.file_name, level + 1)
            if node.right:
                self.pre_order(node.right, os.path.join(path, node.file_name), node.file_name, level + 1)

    # Создаем папку для текущего узла и страницу в нем
    def create_html_file(self, node, path, parent_file_name):   

        # Формируем относительный путь к styles/styles.css
        # (Для случая first.html не ставим ../ в начале)
        style_p = ""
        if node.level > 0:
            style_p = "../" * node.level + "styles/style.css"
        else:
            style_p = "styles/style.css"
        style_p = f'<link rel="stylesheet" href="{style_p}">\n'    
        
        # Для отладки
        # print("level = ", node.level, end="\n")

        # Формируем относительный путь к возврату назад 
        back_path = ""
        if parent_file_name:
            back_path = f'../{parent_file_name}.html'
        
        # Формируем относительный путь к корню (Для first.html не ставим ../ в начале)
        root_path = ""
        if node.level > 0:
            root_path = "../" * node.level + "first.html"
        else:
            root_path = "first.html"

        content=f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>{node.value}</title>
    {style_p}
</head>
<body>\n

    <header>
        <div class="container">
            <img src="icons/ivl.png" alt="Логотип" />
                <nav>             
                    <ul>
                    <li><a href="{root_path}"><h2>На главную</h2></a></li>
                    <li><a href="{back_path}"><h2>Назад</h2></a></li>
                    <li><a href="#" data-url="contacts.html"><h2>Контакты</h2></a></li>
                    </ul>
                </nav>
          </div>
    </header>

    <div class="container">        
        <div class="sidebar-container">
            <div class="sidebar">
                <h3>Карта документа</h3>
            </div>
        </div>


        <div class="main-content-container">
            <div class="main-content">
                <!-- Здесь будет загружаться содержимое вызываемых из меню страниц -->
                <!--content-->    
'''

        # Заголовок в теле страницы    
        content += f"<h1>{node.value}</h1>\n\n"
        content += f"<p>Level: {node.level}</p>\n"

        # Формируем относительный путь к левому и правому поддереву
        if node.left:
            content += f'<a href="{node.left.file_name}/{node.left.file_name}.html">L:\t{node.left.value}</a><br>\n'
        if node.right:
            content += f'<a href="{node.right.file_name}/{node.right.file_name}.html">R:\t{node.right.value}</a><br>\n'
        
        content += "<br>\n"

        # Формируем относительный путь к возврату назад 
        if parent_file_name:
            content += f'<a href="../{parent_file_name}.html">Назад</a><br>\n'

        content += f'<a href="{root_path}">На главную</a><br>\n'    
        

        # Формируем ссылки на скрипты, которые лежат в директории scripts
        pscr = 'scripts/script_sidebar_menu.js'
        pth=""
        if node.level > 0:    
            pth = '../'*(path.count(os.sep)+1)
        content += '\n<script src="'+pth+pscr+'"></script>\n'

        pscr = 'scripts/script_header_menu.js'
        pth = ""
        if node.level > 0:    
            pth = '../'*(path.count(os.sep)+1)
        content += '\n<script src="'+pth+pscr+'"></script>\n'

        # Закрываем оборваную часть тела страницы
        content +=f'''
            </div>
        </div>    
    </div>  

    <footer>
        <div class="container">
            <nav>              
                <ul> 
                    <li><a href="{root_path}"><h2>На главную</h2></a></li>
                    <li><a href="{back_path}"><h2>Назад</h2></a></li>
                    <li><a href="#" data-url="contacts.html"><h2>Контакты</h2></a></li>
                </ul>           
            </nav>
        </div>
    </footer>   
'''

        # Закрываем тело страницы
        content += f''' 
       
</body>
</html>'''
        # Создаем директорию, если ее нет
        full_path = os.path.join(path, node.file_name)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
                
        # Имя файла совпадает с именем папки
        file_path = os.path.join(full_path, f"{node.file_name}.html")
                
        # Записываем контент в файл
        with open(file_path, "w") as file:
            file.write(content)

        # Для отладки пишем в консоль    
        print(f"Created {file_path}")

#----------------------------------------------------------------------

# Копирование папки scripts с содержимым в папку сайта first
def copy_scripts_to_first_dir():
    # Получаем путь к корневой папке first
    first_dir = os.path.join(os.getcwd(), 'first')

    # Создаем путь к папке scripts в корневой папке first
    dest_scripts_dir = os.path.join(first_dir, 'scripts')

    # Определяем путь к исходной папке scripts
    scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')

    # Удаляем существующую папку scripts (если она существует)
    if os.path.exists(dest_scripts_dir):
        shutil.rmtree(dest_scripts_dir)

    # Копируем папку scripts в корневую папку first
    shutil.copytree(scripts_dir, dest_scripts_dir)

#----------------------------------------------------------------------
def main():

    # Создаем дерево сайта и его каталогов
    tree = TreeNode("Главная страница", "first")                 
    tree.left = TreeNode("Раздел (L)", "second")           
    tree.right = TreeNode("Раздел (R)", "third")           
    tree.left.left = TreeNode("Раздел (LL)", "fourth")   
    tree.left.right = TreeNode("Раздел (LR)", "fifth")       
    tree.left.right.left = TreeNode("Раздел (LRL)", "sext")  
    tree.left.right.right = TreeNode("Раздед (LRR)", "sevent")

    # Генерация HTML файлов по всему дереву
    tree.pre_order(tree)  

    # Копирование папки scripts с содержимым в папку сайта first
    copy_scripts_to_first_dir()
     

if __name__ == "__main__":

    utils.Hi()

    main()                                 
