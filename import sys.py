import sys
from PyQt5.QtWidgets import QApplication, Qlabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt")
        self.setGeometry(100, 100, 600, 400)
        self.label = Qlabel("Hello, PyQt!", self)
        self.label.setGeometry(50, 50, 200, 50)

app = QApplication(sys.angry)
window = MainWindow()
window.show()
sys.exit(app.exec_())