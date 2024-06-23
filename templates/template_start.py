PAGE_TEMPLATE_START = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>{title}</title>
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
                {sidebar_content}
            </div>
        </div>
        <div class="main-content-container">
            <div class="main-content">
                <div>
                    <h1>{title}</h1>
                    <p><i>[{full_path}]</i></p>
                    <div>
                        {main_content}
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
</html>
"""
