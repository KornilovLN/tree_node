#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import platform

CSS = '''
html, body {
    height: 100%;
    margin: 10;
    background-color: #c4c0b6; /* Цвет фона для всего окна */
}

header {
    background: #B0DDDD;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0; /* Добавляем небольшой отступ сверху и снизу */
    border: 2px solid #74a2c0; /* Добавляем бордер */

}

sidebar {
    height: 300px;
    border: 2px solid #7c7c55; /* Добавляем бордер */

}

.main {
    background: #dbda74;
    height: 300px;
    border: 2px solid #7c7c55; /* Добавляем бордер */

}

footer {
    background: #b4b69b;
    height: 70px;
    border: 2px solid #aaaa7d; /* Добавляем бордер */

}

header .container,
footer .container {
    display: flex;
    align-items: center;
    height: 100%;
}

.h2 {
    text-align: center;
}

.main-content h2 {
    text-align: center;
}


header .container {
    display: flex;
    align-items: center;
/*    height: 70px; */ /* Установите желаемую высоту для header */
}


.container {
    width: 100%;
    height: 100%;
    display: flex;
    max-width: 1600px; 
    padding: 0 15px;
    margin: 10px auto;   
}

.container:after {
    content: "";
    display: table;
    clear: both;
  }

.logo {
    margin-right: auto; /* Выталкивает логотип влево */
    display: flex;
    justify-content: center; /* Это выровняет логотип по горизонтали */
    align-items: center; /* Это выровняет логотип по вертикали */
    height: 100vh; /* Это установит высоту логотипа на 100% от высоты окна */    
}

.logo img {
    height: 32px; /* Устанавливаем высоту логотипа */
    /*margin-top: -5px;*/ /* Приподнимаем логотип над серединной линией */
}

nav {
    display: flex;      /* Используем flexbox для навигации */
}

nav ul {
    display: flex;      /* Размещаем элементы списка в строку */
    margin: 0;
    padding: 0;
    list-style: none;
}

nav li {
    margin-left: 40px;  /* Отступ между элементами списка */
}

nav a {
    text-decoration: none;
    line-height: 1;     /* Сбрасываем line-height для ссылок */
    padding: 10px;      /* Добавляем отступы для ссылок */
}

.sidebar-container {
    width: 17%;
    height: 100%;
    float: left;
    background-color: #cfd3b7; /* Цвет фона для контейнера сайдбара */
    overflow: auto; /* для полос прокрутки */
    padding: 20px; /* Отступ для контейнера сайдбара */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Тень */
    
    border: 2px solid #aaaa7d; /* Добавляем бордер */
}

.main-content-container {
    width: 83%;
    height: 100%;
    float: right;    
    background-color: #dbdfcb; /* Цвет фона для контейнера основного содержимого */
    overflow: auto; /* для полос прокрутки */
    padding: 20px; /* Отступ для контейнера основного содержимого */

    border: 2px solid #aaaa7d; /* Добавляем бордер */
}

.sidebar-container, .main-content-container {
    box-sizing: border-box;
}

.sidebar {
    width: 200px;
    padding: 20px;
    background-color: #cfd3b7;   
}

.sidebar h2 {
    text-align: center;
}

.sidebar-menu {
    list-style-type: none;
    padding: 0;
    margin: 0;

    text-align: left; /* Прижимаем текст к левому краю */
  }
  
  .sidebar-menu > li {
    margin-bottom: 10px;
  }
  
  .sidebar-menu a {
    display: block;
    padding: 5px 10px;
    text-decoration: none;
    color: #333;
  }
  
  .sidebar-menu a:hover {
    background-color: #ddd;
  }
  
  .submenu {
    list-style-type: none;
    padding-left: 20px;
    margin: 5px 0;
    display: none;
  }
  
  .submenu.open {
    display: block;
  }



.container div {    
    float: left;
    margin-bottom: 15px;
}

.col-1-2 {
    width: 50%;  
}

.col-1-3 {
    width: 33.3333333333%;
}

.col-1-4 {
    width: 25%;
}

.col-2-3 {
    width: 66.6666666667%;
}                           
'''

def techinfo():
    print("__________________________")
    print("Сведения о платформе:")
    print(sys.version_info)
    print("SYS version: ", sys.version)

    print("Python Version: ", platform.python_version())
    print("Python Executable Path: ", sys.executable)
    print("__________________________\n")
    '''
    #!/usr/bin/env python3
    #!/home/leon/anaconda3/bin/python3
    '''

def selfdoc():
    print(
        ''' 
           ======================================================           
           Демонстрационная программа динамического создания HTML
            страниц из дерева каталогов с использованием
            класса TreeNode
           Программа запускается как python tree_node.py
            и создает общий каталог first (с файлом first.html),
            в котором будут созданы вложенные одна в одну 
            директории second, third, fourth, fifth, sext, sevent,
           Каталог styles и файл style.css также будут созданы в
            корневом каталоге first.

           Скелет программы примерно такой:

            # База разработки
            # с созданием и обходом дерева узлов и файлов
            class TreeNode:
                def __init__(self, value):
                    self.value = value
                    self.left = None
                    self.right = None
                    
                def pre_order(self, node):
                    if node:
                        print(node.value)
                        self.pre_order(node.left)
                        self.pre_order(node.right)    

            # создаем уровни дерева        
            tree = TreeNode("первый")
            tree.left = TreeNode("второй")
            tree.right = TreeNode("третий")
            tree.left.left = TreeNode("четвертый")
            tree.left.right = TreeNode("пятый")

            # выводим значения узлов дерева
            tree.pre_order(tree)  
           ======================================================
        '''
    )

def About():
    print(
        """
            _________________________________

            author: Kornilovstar
                    class  8
                    school 242
            e-mail: ln.Kornilovstar@gmail.com
            github: github.com/KornilovLN
            _________________________________
        """
    )


class TreeNode:
    def __init__(self, value, file_name, level=0):
        self.value = value          # Значение узла
        self.file_name = file_name  # Имя файла
        self.level = level          # Уровень вложенности узла
        self.left = None            # Левый поддерево
        self.right = None           # Правый поддерево

        # Сразу создаем директорию и файл стилей корневого узла
        if file_name == "first":
            self.create_styles_directory_and_file()


    # Создаем директорию и файл стилей корневого узла
    def create_styles_directory_and_file(self):
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
            print(f"File 'style.css' already exists at {style_file}")


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

        content = f'''
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
        
        # Формируем относительный путь к корню 
        # (Для случая first.html не ставим ../ в начале)
        if path.count(os.sep):  
            root_path = "../" * (path.count(os.sep) + 1) + "first.html"        
            content += f'<a href="{root_path}">На главную</a><br>\n'

        # Для отладки    
        # print(path.count(os.sep), end="\n")

        pth = ""
        if path.count(os.sep):
            pth += '../'*(path.count(os.sep)+1)
            pthscr = pth + 'scripts/script.js'
            scr = '\n<script src="'+pthscr+'"></script>\n'

            content += scr

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

if __name__ == "__main__":
    # Выводим документацию
    selfdoc()
    # Выводим сообщение об авторе
    About()
    # Выводим информацию о среде
    techinfo()

    # Запускаем программу
    main()                                 
