import os
import shutil

def create_site_structure(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        copy_directory(src_dir, dest_dir, dest_dir)
    except OSError as e:
        print(f"Ошибка при создании структуры сайта: {e}")

def copy_directory(src_path, dest_path, dest_dir):
    for entry in os.listdir(src_path):
        src_entry_path = os.path.join(src_path, entry)
        dest_entry_path = os.path.join(dest_path, entry)

        if os.path.isdir(src_entry_path):
            os.makedirs(dest_entry_path, exist_ok=True)
            folder_name = os.path.basename(dest_entry_path)
            html_file_path = os.path.join(dest_entry_path, f"{folder_name}.html")
            parent_dir = os.path.dirname(dest_entry_path)
            parent_folder_name = os.path.basename(parent_dir)
            back_link = f"../{parent_folder_name}.html" if parent_folder_name else ""
            root_link = "../" * (dest_entry_path.count(os.sep) - dest_dir.count(os.sep)) + "sunpp_docs.html"
            next_folders = [f for f in os.listdir(src_entry_path) if os.path.isdir(os.path.join(src_entry_path, f))]
            next_links = [f"{folder_name}.html" for folder_name in next_folders]
            create_html_file(dest_entry_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links)
            context_dir = os.path.join(dest_entry_path, "context")
            os.makedirs(context_dir, exist_ok=True)
            copy_files(src_entry_path, context_dir)
            copy_directory(src_entry_path, dest_entry_path, dest_dir)
        else:
            # copy_files(src_path, dest_path)  не копировать файлы просто в подкаталоги
            pass

def copy_files(src_path, dest_path):
    for file_name in os.listdir(src_path):
        src_file_path = os.path.join(src_path, file_name)
        dest_file_path = os.path.join(dest_path, file_name)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dest_file_path)


#def create_html_file(dest_path, html_file_path, folder_name, next_links, back_link, root_link, dest_dir):
def create_html_file(dest_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links):
    level = dest_path.count(os.sep) - dest_dir.count(os.sep)

    style_link = "../" * level + "styles/style.css"

    icon_link = "../" * level + "icons/ivl.png"

    next_links_html = create_next_links(next_links, folder_name)

    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>{folder_name}</title>
    <link rel="stylesheet" href="{style_link}">
</head>
<body>
    <header>
        <div class="container">
            <img src="{icon_link}" alt="Логотип" />
            <nav>
                <ul>
                    <li><a href="{root_link}"><h2>На главную</h2></a></li>
                    <li><a href="{back_link}"><h2>Назад</h2></a></li>
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
                <div>
                    <h3>{folder_name}</h3>
                    <div>
                        <!-- Тут ссылки на следующие подкаталоги (их может быть от 1-го до нескольких) -->
                         {next_links_html}
                        <!-- Тут ссылка на предыдущий (Назад) -->
                        <!-- Тут ссылка в начало (На главную) -->
                    </div>
                </div>
            </div>
        </div>

    </div>
    <footer>
        <div class="container">
            <nav>
                <ul>
                    <li><a href="{root_link}"><h2>На главную</h2></a></li>
                    <li><a href="{back_link}"><h2>Назад</h2></a></li>
                </ul>
            </nav>
        </div>
    </footer>
</body>
</html>""")

'''
def create_next_links(next_links):
    links_html = ""
    for link in next_links:
        links_html += f'<a href="{link}"><h3>{os.path.splitext(link)[0]}</h3></a><br>\n'
    return links_html
'''
def create_next_links(next_links, folder_name):
    links_html = ""
    for link in next_links:
        link_folder = os.path.splitext(link)[0]

        # links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a><br>\n'

        if folder_name == ".":
            # links_html += f'<a href="{link}"><h3>{link_folder}</h3></a><br>\n'
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a><br>\n'
        else:
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a><br>\n'

    return links_html



def main():
    # Путь к исходной директории
    src_dir = "sunpp_commented"

    # Путь к целевой директории
    dest_dir = "sunpp_docs"

    # Создаем структуру сайта
    create_site_structure(src_dir, dest_dir)
    '''
    # Создаем файл sunpp_docs.html в корневой папке сайта
    sunpp_docs_path = os.path.join(dest_dir, "sunpp_docs.html")
    with open(sunpp_docs_path, "w", encoding="utf-8") as file:
        next_folders = [f for f in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, f))]
        next_links = [f"{folder}.html" for folder in next_folders]
    '''
    # Создаем файл sunpp_docs.html в корневой папке сайта
    sunpp_docs_path = os.path.join(dest_dir, "sunpp_docs.html")
    with open(sunpp_docs_path, "w", encoding="utf-8") as file:
        next_folders = [f for f in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, f))]
        next_links = [f"{folder}.html" for folder in next_folders]
        next_links_html = create_next_links(next_links, ".")
        html_template = ("""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>sunpp_docs</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <header>
        <div class="container">
            <img src="icons/ivl.png" alt="Логотип" />
            <nav>
                <ul>
                    <li><a href="sunpp_docs.html"><h2>На главную</h2></a></li>
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
                <div>
                    <h3>sunpp_docs</h3>
                    <div>
                        <!-- Тут ссылки на следующие подкаталоги (их может быть от 1-го до нескольких) -->
                        {next_links_html}
                    </div>
                </div>
            </div>
        </div>

    </div>

    <footer>
        <div class="container">
            <nav>
                <ul>
                    <li><a href="sunpp_docs.html"><h2>На главную</h2></a></li>
                </ul>
            </nav>
        </div>
    </footer>
</body>
</html>""")

        file.write(html_template.format(next_links_html=next_links_html))

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

