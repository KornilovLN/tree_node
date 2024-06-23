import os
import shutil

from templates.template_start import PAGE_TEMPLATE_START
from templates.template_dyno import PAGE_TEMPLATE_DYNO



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



def copy_files(src_path, dest_path):
    for file_name in os.listdir(src_path):
        src_file_path = os.path.join(src_path, file_name)
        dest_file_path = os.path.join(dest_path, file_name)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dest_file_path)


def generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files):
    sidebar_links = ""
    sidebar_links += f"<h1>{folder_name}:</h1>\n"

    sidebar_links += f"<p>"
    folder_path_rel = os.path.relpath(dest_path, dest_dir)    
    sidebar_links += f"[<i>{folder_path_rel}</i>]\n"
    sidebar_links += f"</p>"

    sidebar_links += "<div>\n"

    for link in next_links:
        link_folder = os.path.splitext(link)[0]
        sidebar_links += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'
    
    sidebar_links += f'<br>'
    sidebar_links += f'<a href="{back_link}"><h3>Назад</h3></a>\n'
    sidebar_links += f'<a href="{root_link}"><h3>На главную</h3></a>\n'
    sidebar_links += f'<br>'

    
    if context_files:
        sidebar_links += "<div style='margin-left: 20px;'>"
        sidebar_links += "<h4>Файлы в папке:</h4>\n"
        sidebar_links += f"<ul>\n"
        for file in context_files:
            sidebar_links += f"<li>{file}</li>\n"
        sidebar_links += f"</ul>\n"    
        sidebar_links += "</div>\n"


    sidebar_links += "</div>\n"

    return sidebar_links


def create_next_links(next_links, folder_name):
    links_html = ""

    for link in next_links:
        link_folder = os.path.splitext(link)[0]

        if folder_name == ".":
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'
        else:
            links_html += f'<a href="{link_folder}/{link}"><h3>{link_folder}</h3></a>\n'

    return links_html



def create_html_file(dest_path, folder_name, dest_dir, html_file_path, root_link, back_link, next_links):
    level = dest_path.count(os.sep) - dest_dir.count(os.sep)

    style_link = "../" * level + "styles/style.css"
    icon_link = "../" * level + "icons/ivl.png"
    next_links_html = create_next_links(next_links, folder_name)

    # Формируем полный путь к текущей папке
    full_path = os.path.relpath(dest_path, dest_dir)

    # Получаем список файлов в папке "context"
    context_dir = os.path.join(dest_path, "context") if dest_path != dest_dir else os.path.join(dest_dir, "context")
    context_files = []
    if os.path.exists(context_dir):
        context_files = os.listdir(context_dir)

    # Формируем HTML-код для отображения списка файлов
    context_files_html = ""
    if context_files:
        context_files_html = "<div style='margin-left: 20px;'><h4>Файлы в папке:</h4>\n"
        
        context_files_html += f"<ul>\n"
        for file in context_files:
            context_files_html += f"<li>{file}</li>\n"
        context_files_html += f"</ul>"

        context_files_html += "</div>"

    # Формируем HTML-код для ссылок в сайдбаре
    sidebar_links = generate_sidebar_links(dest_path, folder_name, dest_dir, root_link, back_link, next_links, context_files)

    # Формируем HTML-код для ссылок в центральной панели
    revers_content_links = f'<a href="{root_link}"><h3>На главную</h3></a>\n'
    revers_content_links += f'<a href="{back_link}"><h3>Назад</h3></a><br>\n'

    print(f"context_files_html: {context_files_html}")

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
                {sidebar_links}                
            </div>
        </div>

        <div class="main-content-container">
            <div class="main-content">
                <div>
                    <h1>{folder_name}</h1>
                    <p><i>[{full_path}]</i></p>
                    <div>
                        <!-- Пока не решили - быть тут ссылкам или нет      
                         {revers_content_links}                  
                         {next_links_html}
                         
                         {context_files_html}                        
                        --> 
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


# Формируем HTML-код для отображения списка файлов
def generate_sidebar_content(folder_name, full_path, next_links, context_files):
    sidebar_content = f"<h1>{folder_name}</h1>\n"
    sidebar_content += f"<p><i>[{full_path}]</i></p>\n"   

    sidebar_content += "<div>"
    for link in next_links:
        link_name = os.path.splitext(link)[0]
        sidebar_content += f'<h3><a href="{link_name}/{link}">{link_name}</a></h3>\n'
    
    if context_files:
    
        sidebar_content += "<ul aria-label='Файлы в папке'>\n"

        for file in context_files:
            file_path = f"context/{file}"
            #sidebar_content += f'<li><a href="{file_path}" target="content-frame" onclick="setTimeout(function() {{ resizeIframe(document.getElementsByName(\'content-frame\')[0]); }}, 100);">{file}</a></li>\n'
            sidebar_content += f'<li><a href="{file_path}" >{file}</a></li>\n'
            
        sidebar_content += f"</ul>\n"

    sidebar_content += "</div>\n"

    return sidebar_content


def main():
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

