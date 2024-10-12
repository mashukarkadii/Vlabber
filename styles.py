style_main="""
            QWidget {
                background-color: #282c34; /* Темно-серый фон */
                font-family: "Roboto";
                color: #eee; /* Светло-серый текст */
            }
            QPlainTextEdit {
                background-color: #333;
                border: none;
                padding: 10px;
                font-family: "Roboto";
                font-size: 14px;
                line-height: 1.5;
                color: #eee; /* Светло-серый текст */
            }
            QPushButton {
                background-color: #3498db; /* Синий цвет */
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9; /* Темнее при наведении */
            }
            QLineEdit {
                border: 1px solid #555; /* Темно-серый контур */
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                background-color: #333;
                color: #eee; /* Светло-серый текст */
            }
            QFrame {
                border-top: 1px solid #555;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QSplitter::handle {
                background-color: #555;
                width: 4px;
            }
            QListWidget {
                background-color: #222; 
                border: 1px solid #333;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #333; 
                font-family: "Roboto"; 
                font-size: 14px;
                background-color: #333;
                color: #eee; /* Светло-серый текст */
            }
            QListWidget::item:selected {
                background-color: #444; 
                color: white; /* Белый текст при выделении */
            }
            QListWidget::item:hover {
                background-color: #444;
                color: white; /* Белый текст при наведении */
            }
            QScrollArea {
                background-color: #282c34; /* Фон для QScrollArea */
            }
            QPlainTextEdit {
                background-color: #333; /* Фон для QPlainTextEdit */
                border: none;
                padding: 10px;
                font-family: "Roboto";
                font-size: 14px;
                line-height: 1.5;
                color: #eee; /* Светло-серый текст */
            }
        """


chat_window = """
            QPlainTextEdit {
        background-color: #333; /* Фон для QPlainTextEdit */
        border: none;
        padding: 10px;
        font-family: "Roboto";
        font-size: 19px;
        line-height: 1.5;
        color: #eee; /* Светло-серый текст */
    }
        """


   


contact_list = """
            QListWidget {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
                font-family: "Roboto";
                font-size: 14px;
            }
            QListWidget::item:selected {
                background-color: #eee;
            }
        """