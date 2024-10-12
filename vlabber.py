from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                QVBoxLayout, QHBoxLayout, QPlainTextEdit, QListWidget, 
                QFrame, QScrollArea, QMessageBox, QSplitter,
                QListWidgetItem, QLabel, 
                QWidget)
from PyQt5.QtCore import Qt, QTimer, QThread
from PyQt5.QtGui import QFont
import styles
import start
import API
import CryptoGraphy
import random
from PyQt5.QtCore import Qt


class GetChatUpdatesThread(QThread):
    def __init__(self, args = dict):
        super().__init__()
        self.chat_updates = None
        self.args = args

    def run(self):
        rsp = API.api(args=self.args)
        response = rsp.getChatUpdates()
        self.chat_updates = response.json()


class GetUpdatesThread(QThread):
    def __init__(self, args = dict):
        super().__init__()
        self.updates = None
        self.args = args

    def run(self):
        rsp = API.api(args=self.args)
        response = rsp.getUpdates()
        self.updates = response.json()

class Vlabber(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vlabber")
        self.resize(800, 600) 
        self.setStyleSheet(styles.style_main)
        self.user_id_label = QLabel(f"Твой ID: {start.getId()}")
        self.user_id_input = QLineEdit()

        self.CRYPT_KEY = "s09df8sd890f7w348rjw09efusdf89g"

        self.user_id_input.setPlaceholderText("Введите ID пользователя с которым хотели бы поговорить")
        self.start_button = QPushButton("Начать диалог")
        self.start_button.clicked.connect(self.start_chat)
  
  
        self.chat_area = QFrame(self)
        self.chat_area.setFrameShape(QFrame.StyledPanel)
        self.chat_area.setStyleSheet("background-color: white;") # Установите белый фон для chat_area

        self.chat_window = QPlainTextEdit(self.chat_area) 
        self.chat_window.setReadOnly(True)
        self.chat_window.setStyleSheet(styles.chat_window)
    


        self.scroll_area = QScrollArea(self.chat_area)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.chat_window)
        self.scroll_area.setStyleSheet("border: none;")


        self.message_input = QLineEdit(self)
        self.message_input.setPlaceholderText("Сообщение")
        self.message_input.returnPressed.connect(self.send_message)


        self.send_button = QPushButton("Отправить", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setEnabled(False) 

  
        self.contact_list = QListWidget(self)
        self.contact_list.setStyleSheet(styles.contact_list)
        self.contact_list.itemClicked.connect(self.display_chat)
        self.contact_list.setStyleSheet(styles.contact_list)
        

        layout = QVBoxLayout()

     
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.user_id_label)
        top_layout.addWidget(self.user_id_input)
        top_layout.addWidget(self.start_button)
        layout.addLayout(top_layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.contact_list) # Добавляем список контактов слева
        splitter.addWidget(self.scroll_area) # Добавляем окно чата справа
        layout.addWidget(splitter)
        

        message_layout = QHBoxLayout()
        message_layout.addWidget(self.message_input)
        message_layout.addWidget(self.send_button)
        layout.addLayout(message_layout)


        self.setLayout(layout)

        self.lastes_updates = []
        
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.get_updates) 
        self.update_timer.setInterval(1000)  


        self.count_update = 0


        self.update_chats = QTimer()
        self.update_chats.timeout.connect(self.update_contact_list)
        self.update_chats.setInterval(15000)
        self.update_chats.start()

        self.start_id = start.getId()
        self.update_contact_list()

    def update_contact_list(self):
        if self.start_id:
            flags = start.getFlags()
            randomFlag = random.choice(flags)
            args = {
                "myId": self.start_id,
                "flagsNum": len(flags),
                "randomFlag": randomFlag,
                "hwid": start.getHwid()
            }
            self.update_Chat_thread = GetChatUpdatesThread(args=args)
            self.update_Chat_thread.finished.connect(self.process_chat_updates)
            self.update_Chat_thread.start()
    
    def process_chat_updates(self):
        chats = self.update_Chat_thread.chat_updates
        if chats:
            self.contact_list.clear()
            for chat in chats:
                item = QListWidgetItem(chat) 
                item.setFont(QFont("Roboto", 14))
                self.contact_list.addItem(item)
    
    def display_chat(self, item):
        self.chat_window.clear()
        user_id = item.text()
        self.user_id_input.setText(user_id)
        self.send_button.setEnabled(True)
        self.update_timer.start()
        self.chat_window.insertPlainText(f"Загрузка...")
        self.get_updates()

    
    def topic_contact(self):
        flags = start.getFlags()
        args = {
                "myId": self.start_id,
                "flagsNum": len(flags),
                "randomFlag": random.choice(flags),
                "hwid": start.getHwid(),
                "adrId": self.user_id_input.text()
            }
        rt=API.api(args)
        rt.addContact()
    
    def start_chat(self):
        self.count_update = 0
        user_id = self.user_id_input.text()
        if user_id:
            response = self.check_user(user_id)
            if response == "yes":
                self.lastes_updates.clear()
                self.topic_contact()
                self.user_id = self.user_id_input.text()
                self.send_button.setEnabled(True)
                self.update_timer.start()
                self.chat_window.insertPlainText(f"Загрузка...")
                self.get_updates()
            else:
                QMessageBox.warning(self, "Ошибка", "Пользователь не найден!")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите ID пользователя!")


    
    def check_user(self, user_id):
        asp = API.api(args={"myId": user_id})
        res=asp.checkId()
        if res:
            return "no"
        else:
            return "yes"


    def get_updates(self):
        if self.start_id:  
            flags = start.getFlags()
            args = {
                "myId": self.start_id,
                "flagsNum": len(flags),
                "randomFlag": random.choice(flags),
                "hwid": start.getHwid(),
                "adrId": self.user_id_input.text()
            }
            self.update_thread = GetUpdatesThread(args=args)
            self.update_thread.finished.connect(self.process_updates)
            self.update_thread.start()
    
    def process_updates(self):
            updates = self.update_thread.updates
            if updates:
                if self.count_update != 0:
                    if self.lastes_updates == []:
                        self.chat_window.clear()
                    for update in updates:
                        if update not in self.lastes_updates:
                            message = ""
                            start_id = update["start_id"]
                            messageq = update["message"]
                            cryPtKeyInt = int(self.start_id) + int(self.user_id_input.text())
                            cryptKey = CryptoGraphy.getKey(f"{cryPtKeyInt}{self.CRYPT_KEY}")
                            crypt=CryptoGraphy.crypt(cryptKey)
                            decoded_message = crypt.Decrypt(messageq)
                            if self.start_id != start_id:
                                message += f"{decoded_message}\n"
                                self.chat_window.insertPlainText(message)
                            self.lastes_updates.append(update)
                        self.chat_window.verticalScrollBar().setValue(self.chat_window.verticalScrollBar().maximum())
                else:
                    if self.lastes_updates == []:
                        self.chat_window.clear()
                    for update in updates:
                        if update not in self.lastes_updates:
                            message = ""
                            start_id = update["start_id"]
                            messageq = update["message"]
                            cryPtKeyInt = int(self.start_id) + int(self.user_id_input.text())
                            cryptKey = CryptoGraphy.getKey(f"{cryPtKeyInt}{self.CRYPT_KEY}")
                            crypt=CryptoGraphy.crypt(cryptKey)
                            decoded_message = crypt.Decrypt(messageq)
                            if self.start_id == start_id:
                                message += f"YOU: {decoded_message}\n"
                            else:
                                message += f"{decoded_message}\n"
                            self.chat_window.insertPlainText(message)
                        self.lastes_updates.append(update)
                        self.chat_window.verticalScrollBar().setValue(self.chat_window.verticalScrollBar().maximum())
                self.count_update = self.count_update + 1
            else:
                self.chat_window.clear()
                self.chat_window.insertPlainText("Сообщений не найдено, отправьте первое")

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.chat_window.insertPlainText(f"YOU: {message}\n")
            cryPtKeyInt = int(self.start_id) + int(self.user_id_input.text())
            cryptKey = CryptoGraphy.getKey(f"{cryPtKeyInt}{self.CRYPT_KEY}")
            crypt=CryptoGraphy.crypt(cryptKey)
            encoded_message = crypt.Encrypt(message)
            self.sendMessage(encoded_message)
            self.message_input.clear()
        else:
            print("ok")

    def sendMessage(self, message):
        if self.start_id:
            flags = start.getFlags()
            args = {
                "myId": self.start_id,
                "messageText": message,
                "flagsNum": len(flags),
                "randomFlag": random.choice(flags),
                "hwid": start.getHwid(),
                "adrId": self.user_id_input.text()
            }
            rsp=API.api(args=args)
            res=rsp.sendMessage()
            if res:
                return "ok"
