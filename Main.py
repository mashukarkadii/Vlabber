import start
from vlabber import Vlabber
from PyQt5.QtWidgets import QApplication
import sys

start.start_messager()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Vlabber()
    window.show()
    sys.exit(app.exec_())