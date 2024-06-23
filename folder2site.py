import os
import shutil
import html 

from templates.template_start import PAGE_TEMPLATE_START
from templates.template_dyno import PAGE_TEMPLATE_DYNO



def create_site_structure(src_dir, dest_dir):
    """
    Функция создает структуру сайта из исходной директории.
        использует рекурсивный обход дерева директорий.
  
    Args:
        src_dir (str): Путь к исходной директории.
        dest_dir (str): Путь к целевой директории.

    Returns:
        none: None

    Raises:
        OSError: Ошибка при создании структуры сайта.
    """
    try:
        os.makedirs(dest_dir, exist_ok=True)
        copy_directory(src_dir, dest_dir, dest_dir)
    except OSError as e:
        print(f"Ошибка при создании структуры сайта: {e}")



def copy_directory(src_path, dest_path, dest_dir):
    """
    Рекурсивно копирует директорию и
    создает HTML-файлы для каждой поддиректории.

    Args:
        src_path (str): Путь к исходной директории.
        dest_path (str): Путь к целевой директории.
        dest_dir (str): Путь к корневой целевой директории.

    Returns:
        None
    """
    # Создаем HTML-файл для каждой поддиректории
    for entry in os.listdir(src_path):
        src_entry_path = os.path.join(src_path, entry)
        dest_entry_path = os.path.join(dest_path, entry)

        if os.path.isdir(src_entry_path):
            # Создаем целевую директорию
            os.makedirs(dest_entry_path, exist_ok=True)  

            # Получаем имя текущей папки          
            folder_name = os.path.basename(dest_entry_path)

            # Формируем путь для HTML-файла
            html_file_path = os.path.join(dest_entry_path, f"{folder_name}.html")

            # Получаем имя родительской папки
            parent_dir = os.path.dirname(dest_entry_path)
            parent_folder_name = os.path.basename(parent_dir)

            # Формируем ссылки для возвратов назад и в  главную
            back_link = f"../{parent_folder_name}.html" if parent_folder_name else ""
            root_link = "../" * (dest_entry_path.count(os.sep) - dest_dir.count(os.sep)) + "sunpp_docs.html"

            # Получаем список поддиректорий
            next_folders = [f for f in os.listdir(src_entry_path) if os.path.isdir(os.path.join(src_entry_path, f))]
            next_links = [f"{folder_name}.html" for folder_name in next_folders]
            
             # Создаем HTML-файл для текущей директории
            create_html_file(dest_entry_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links)
            
            # Создаем директорию для контекстных файлов
            # и копируем файлы в контекстную директорию
            context_dir = os.path.join(dest_entry_path, "context")
            os.makedirs(context_dir, exist_ok=True)
            copy_files(src_entry_path, context_dir)

             # Рекурсивно обрабатываем поддиректории
            copy_directory(src_entry_path, dest_entry_path, dest_dir)



def copy_files(src_path, dest_path):
    """
    Копирует все файлы из исходной директории в целевую директорию.

    Args:
        src_path (str): Путь к исходной директории.
        dest_path (str): Путь к целевой директории.

    Returns:
        None
    """
    """ 
    for file_name in os.listdir(src_path):
        # Формируем полный путь к файлу в исходной директории
        src_file_path = os.path.join(src_path, file_name)
        # Формируем полный путь к файлу в целевой директории
        dest_file_path = os.path.join(dest_path, file_name)
        # Проверяем, является ли объект файлом (а не директорией)
        if os.path.isfile(src_file_path):
             # Копируем файл из исходной директории в целевую
            shutil.copy(src_file_path, dest_file_path)
    """
    for file_name in os.listdir(src_path):
        src_file_path = os.path.join(src_path, file_name)
        if os.path.isfile(src_file_path):
            # Читаем содержимое файла
            with open(src_file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            # Экранируем HTML-символы и оборачиваем содержимое в теги <pre>
            escaped_content = html.escape(content)
            html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{file_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        pre {{ background-color: #f0f0f0; padding: 10px; white-space: pre-wrap; word-wrap: break-word; }}
    </style>
</head>
<body>
    <h1>{file_name}</h1>
    <pre>{escaped_content}</pre>
</body>
</html>
"""            
            # Сохраняем новый HTML-файл
            new_file_name = f"{file_name}.html"
            dest_file_path = os.path.join(dest_path, new_file_name)
            with open(dest_file_path, 'w', encoding='utf-8') as file:
                file.write(html_content)


def generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files):
    sidebar_links = ""
    sidebar_links += f"<h1>{folder_name}:</h1>\n"

    sidebar_links += f"<p>"
    folder_path_rel = os.path.relpath(dest_path, dest_dir)    
    sidebar_links += f"[<i>{folder_path_rel}</i>]\n"
    sidebar_links += f"</p>"

    sidebar_links += "<div>\n"

    # Добавляем ссылки на подразделы
    if next_links:
        sidebar_links += "<h3>Подразделы:</h3>\n"
        for link in next_links:
            link_folder = os.path.splitext(link)[0]
            sidebar_links += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'

    # Добавляем ссылки на файлы в текущей папке
    if context_files:
        sidebar_links += "<h3>Файлы в папке:</h3>\n"
        sidebar_links += f"<ul>\n"
        for file in context_files:
            original_name = os.path.splitext(file)[0]  # Удаляем расширение .html
            sidebar_links += f'<li><a href="context/{file}">{original_name}</a></li>\n'
        sidebar_links += f"</ul>\n"    

    sidebar_links += f'<br>'
    if back_link:
        sidebar_links += f'<a href="{back_link}"><h3>Назад</h3></a>\n'
    sidebar_links += f'<a href="{root_link}"><h3>На главную</h3></a>\n'

    sidebar_links += "</div>\n"

    return sidebar_links

'''
def generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files):
    """
    Генерирует HTML-код для боковой панели навигации.

    Args:
        dest_path (str): Путь к текущей директории.
        folder_name (str): Имя текущей папки.
        dest_dir (str): Путь к корневой целевой директории.
        root_link (str): Ссылка на главную страницу.
        back_link (str): Ссылка для возврата назад.
        next_links (List[str]): Список ссылок на подразделы.
        context_files (List[str]): Список файлов в текущей директории.

    Returns:
        str: HTML-код боковой панели навигации.
    """
    sidebar_links = ""
    # Добавляем заголовок с именем текущей папки
    sidebar_links += f"<h1>{folder_name}:</h1>\n"

    # Добавляем относительный путь к текущей папке
    sidebar_links += f"<p>"
    folder_path_rel = os.path.relpath(dest_path, dest_dir)    
    sidebar_links += f"[<i>{folder_path_rel}</i>]\n"
    sidebar_links += f"</p>"

    sidebar_links += "<div>\n"

    """
    # Добавляем ссылки на подразделы
    for link in next_links:
        link_folder = os.path.splitext(link)[0]
        sidebar_links += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'
    """
    # Добавляем ссылки на подразделы
    if next_links:
        sidebar_links += "<h3>Подразделы:</h3>\n"
        for link in next_links:
            link_folder = os.path.splitext(link)[0]
            sidebar_links += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'

    sidebar_links += f'<br>'
    if back_link:
        sidebar_links += f'<a href="{back_link}"><h3>Назад</h3></a>\n'
    sidebar_links += f'<a href="{root_link}"><h3>На главную</h3></a>\n'
    sidebar_links += f'<br>'




    # Добавляем ссылки "Назад" и "На главную"
    sidebar_links += f'<br>'
    sidebar_links += f'<a href="{back_link}"><h3>Назад</h3></a>\n'
    sidebar_links += f'<a href="{root_link}"><h3>На главную</h3></a>\n'
    sidebar_links += f'<br>'

    # Если есть файлы в текущей директории, добавляем их список
    if context_files:
        sidebar_links += "<div style='margin-left: 20px;'>"
        sidebar_links += "<h4>Файлы в папке:</h4>\n"
        sidebar_links += f"<ul>\n"
        for file in context_files:
            original_name = os.path.splitext(file)[0]  # Удаляем расширение .html
            sidebar_links += f'<li><a href="context/{file}">{original_name}</a></li>\n'
            #sidebar_links += f'<li><a href="context/{file}.html">{file}</a></li>\n'
        sidebar_links += f"</ul>\n"    
        sidebar_links += "</div>\n"


    sidebar_links += "</div>\n"

    return sidebar_links
'''


def create_next_links(next_links, folder_name):
    """
    Создает HTML-код для ссылок на подразделы.

    Args:
        next_links (List[str]): Список имен файлов HTML для подразделов.
        folder_name (str): Имя текущей папки.

    Returns:
        str: HTML-код со ссылками на подразделы.
    """
    links_html = ""

    for link in next_links:
        # Получаем имя папки без расширения .html
        link_folder = os.path.splitext(link)[0]

        # Создаем HTML-код для ссылки
        # Примечание: условие folder_name == "." не влияет на результат
        # и может быть удалено
        if folder_name == ".":
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'
        else:
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'

    return links_html


'''
def create_html_file(dest_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links):
    """
    Создает HTML-файл для текущей директории.

    Args:
    dest_path (str): Путь к текущей директории.
    folder_name (str): Имя текущей папки.
    dest_dir (str): Путь к корневой целевой директории.
    html_file_path (str): Путь, где будет создан HTML-файл.
    root_link (str): Ссылка на главную страницу.
    back_link (str): Ссылка для возврата назад.
    next_links (List[str]): Список ссылок на подразделы.

    Returns:
    None
    """
    # Вычисляем уровень вложенности текущей директории
    level = dest_path.count(os.sep) - dest_dir.count(os.sep)

    # Формируем ссылки на стили и иконку
    style_link = "../" * level + "styles/style.css"
    icon_link = "../" * level + "icons/ivl.png"

    # Формируем полный путь к текущей папке
    full_path = os.path.relpath(dest_path, dest_dir)

    # Получаем список файлов в папке "context"
    context_dir = os.path.join(dest_path, "context")
    context_files = []
    if os.path.exists(context_dir):
        context_files = [f for f in os.listdir(context_dir) if f.endswith('.html')]


    # Формируем HTML-код для ссылок в сайдбаре
    sidebar_links = generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files)
    #sidebar_links = generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, context_files)

    # Формируем HTML-код для отображения содержимого файлов
    main_content = ""
    for file in context_files:
        file_path = os.path.join(context_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        main_content += f"<h2>{file[:-5]}</h2>\n"  # Убираем расширение .html из заголовка
        main_content += file_content

    # Добавляем ссылки на подразделы в основной контент
    if next_links:
        main_content += "<h2>Подразделы:</h2>\n<ul>\n"
        for link in next_links:
            link_folder = os.path.splitext(link)[0]
            main_content += f'<li><a href="{link_folder}/{link}">{link_folder}</a></li>\n'
        main_content += "</ul>\n"

    # Записываем сформированный HTML в файл
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(PAGE_TEMPLATE_DYNO.format(
            folder_name=folder_name,
            style_link=style_link,
            icon_link=icon_link,
            root_link=root_link,
            back_link=back_link,
            sidebar_links=sidebar_links,
            full_path=full_path,
            main_content=main_content
        ))
'''
def create_html_file(dest_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links):
    level = dest_path.count(os.sep) - dest_dir.count(os.sep)

    style_link = "../" * level + "styles/style.css"
    icon_link = "../" * level + "icons/ivl.png"

    # Формируем полный путь к текущей папке
    full_path = os.path.relpath(dest_path, dest_dir)

    # Получаем список файлов в папке "context"
    context_dir = os.path.join(dest_path, "context")
    context_files = []
    if os.path.exists(context_dir):
        context_files = [f for f in os.listdir(context_dir) if f.endswith('.html')]

    # Формируем HTML-код для ссылок в сайдбаре
    sidebar_links = generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files)

    # Формируем HTML-код для отображения содержимого файлов
    main_content = ""
    for file in context_files:
        file_path = os.path.join(context_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        main_content += f"<h2>{os.path.splitext(file)[0]}</h2>\n"  # Убираем расширение .html из заголовка
        main_content += file_content

    # Записываем сформированный HTML в файл
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(PAGE_TEMPLATE_DYNO.format(
            folder_name=folder_name,
            style_link=style_link,
            icon_link=icon_link,
            root_link=root_link,
            back_link=back_link,
            sidebar_links=sidebar_links,
            full_path=full_path,
            main_content=main_content
        ))


# Формируем HTML-код для отображения списка файлов
def generate_sidebar_content(folder_name, full_path, next_links, context_files):
    """
    Генерирует HTML-содержимое для боковой панели.

    Args:
        folder_name (str): Имя текущей папки.
        full_path (str): Полный путь к текущей папке.
        next_links (List[str]): Список ссылок на подразделы.
        context_files (List[str]): Список файлов в текущей директории.

    Returns:
        str: HTML-код для боковой панели.
    """
    # Добавляем заголовок с именем текущей папки
    sidebar_content = f"<h1>{folder_name}</h1>\n"
    # Добавляем полный путь к текущей папке
    sidebar_content += f"<p><i>[{full_path}]</i></p>\n"   

    sidebar_content += "<div>"
    # Добавляем ссылки на подразделы
    for link in next_links:
        link_name = os.path.splitext(link)[0]
        sidebar_content += f'<h3><a href="{link_name}/{link}">{link_name}</a></h3>\n'
    
    # Если есть файлы в текущей директории, добавляем их список
    if context_files:
        sidebar_content += "<ul aria-label='Файлы в папке'>\n"
        for file in context_files:
            original_name = os.path.splitext(file)[0]  # Удаляем расширение .html
            sidebar_content += f'<li><a href="context/{file}">{original_name}</a></li>\n'
            #sidebar_content += f'<li><a href="context/{file}.html">{file}</a></li>\n'
        sidebar_content += f"</ul>\n"
    sidebar_content += "</div>\n"

    return sidebar_content



def main():
    """
    Основная функция создания структуры сайта
        на основе существующего
        каталога с подкаталогами и файламии,
        а также для генерации HTML-файлов в соответствующих папках.

        1 Сначала создается структура сайта с помощью функции create_site_structure().
        2 Затем создается папка "context" в корневой папке сайта и в нее копируются файлы из исходной директории.
        3 Генерируется главная страница сайта (sunpp_docs.html) с использованием шаблона PAGE_TEMPLATE_START.
        4 Для главной страницы создается боковая панель с помощью функции generate_sidebar_content().
        5 В конце функции копируются папки styles, scripts и icons в корневую папку сайта. 
        6 Обратите внимание!!!, что main_content оставлен пустым.
        7 Последние две строки (if __name__ == "__main__":) обеспечивают,
            что функция main() будет вызвана только если скрипт запущен напрямую, а не импортирован как модуль.
    """
    # Путь к исходной директории
    src_dir = "sunpp_commented"

    # Путь к целевой директории
    dest_dir = "sunpp_docs"

    # Создаем структуру сайта
    create_site_structure(src_dir, dest_dir)

    # Создаем папку "content" в корневой папке сайта и копируем туда файлы из корневой папки исходного каталога
    root_context_dir = os.path.join(dest_dir, "context")
    os.makedirs(root_context_dir, exist_ok=True)
    copy_files(src_dir, root_context_dir)

    # Вычисляем folder_name и full_path для корневой страницы
    folder_name = "sunpp_docs"
    full_path = os.path.basename(dest_dir)

    # Получаем список файлов в папке "context"
    root_context_dir = os.path.join(dest_dir, "context")
    context_files = []
    if os.path.exists(root_context_dir):
        context_files = os.listdir(root_context_dir)

    # Создаем файл sunpp_docs.html в корневой папке сайта
    sunpp_docs_path = os.path.join(dest_dir, "sunpp_docs.html")

    # Определяем next_links
    next_folders = [f for f in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, f))]
    next_links = [f"{folder}.html" for folder in next_folders]
        
    # Создаем содержимое главной страницы    
    with open(sunpp_docs_path, "w", encoding="utf-8") as file:
        sidebar_content = generate_sidebar_content(folder_name, full_path, next_links, context_files)
        file.write(PAGE_TEMPLATE_START.format(
            title=folder_name,
            style_link="styles/style.css",
            icon_link="icons/ivl.png",
            root_link="sunpp_docs.html",
            back_link="",
            sidebar_content=sidebar_content,
            full_path=full_path,
            main_content=""  # Пока оставляем пустым
        ))
#-------------------------------------------------------------------------------

    # Копируем папки styles, scripts и icons в корневую папку сайта
    styles_dest = os.path.join(dest_dir, "styles")
    if os.path.exists(styles_dest):
        shutil.rmtree(styles_dest)
    shutil.copytree(os.path.join(os.getcwd(), "styles"), styles_dest)

    scripts_dest = os.path.join(dest_dir, "scripts")
    if os.path.exists(scripts_dest):
        shutil.rmtree(scripts_dest)
    shutil.copytree(os.path.join(os.getcwd(), "scripts"), scripts_dest)

    icons_dest = os.path.join(dest_dir, "icons")
    if os.path.exists(icons_dest):
        shutil.rmtree(icons_dest)
    shutil.copytree(os.path.join(os.getcwd(), "icons"), icons_dest)

if __name__ == "__main__":
    main()

