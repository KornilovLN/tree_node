# tree_node
## Little site-template generator

```
Программа tree_node.py из исходной папки с содержимым

    ├── LICENSE
    ├── materials
    │   ├── about.txt
    │   ├── selfdoc.txt
    │   ├── style.css
    │   └── techinfo.txt
    ├── __pycache__
    │   ├── utils.cpython-312.pyc
    │   └── utils.cpython-38.pyc
    ├── README.md
    ├── scripts
    │   ├── foother.js
    │   ├── script_header_menu.js
    │   ├── script_menu.js
    │   ├── script_page_links.js
    │   └── script_sidebar_menu.js
    ├── tree_node.py
    ├── tree.txt
    └── utils.py

Создает каталог first и в нем размещает всю заданную
  структуру файлов и папок сайта, где корневой файл first.html
  находится в папке сайта first.

Затем, все папки вложенные населяются соответствующими файлами 
*.html

В файлах *.html внутри тега <head> добавляются таблицы стилей,
  которые находятся в папке materials.
  а также скрипты, которые находятся в папке scripts, помещаются
  в конце формируемого html кода.

Все ссылки навигации в каждом файле html помещаются в тег <body>
  и включают как ссылки на следующие страницы сайта, так и на
  предидущие (например: "Назад" и "На главную")

Ссылки навигации также будут в дальнейше отрабатываться из скриптов
  в панеле навигации слева и сверху и снизу страницы

Сейчас сайт создается только для локального использования,
  и пока окончательно не отработаны вопросы дизайна,
  хотя вариант таблицы CSS размещен в папке styles сайта

В дальнейшем сайт будет перенесен под управление сервером  
```

Как выглядит каталог программы и созданного в нем каталога
  с сайтом

```
.
├── first
│   ├── first.html
│   ├── scripts
│   │   ├── foother.js
│   │   ├── script_header_menu.js
│   │   ├── script_menu.js
│   │   ├── script_page_links.js
│   │   └── script_sidebar_menu.js
│   ├── second
│   │   ├── fifth
│   │   │   ├── fifth.html
│   │   │   ├── sevent
│   │   │   │   └── sevent.html
│   │   │   └── sext
│   │   │       └── sext.html
│   │   ├── fourth
│   │   │   └── fourth.html
│   │   └── second.html
│   ├── styles
│   │   └── style.css
│   └── third
│       └── third.html
├── LICENSE
├── materials
│   ├── about.txt
│   ├── selfdoc.txt
│   ├── style.css
│   └── techinfo.txt
├── __pycache__
│   ├── utils.cpython-312.pyc
│   └── utils.cpython-38.pyc
├── README.md
├── scripts
│   ├── foother.js
│   ├── script_header_menu.js
│   ├── script_menu.js
│   ├── script_page_links.js
│   └── script_sidebar_menu.js
├── tree_node.py
├── tree.txt
└── utils.py
```
