import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout

class DraggablePopup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.initUI()
        self.header_mouse_pos = None

    def initUI(self):
        self.setFixedSize(300, 200)
        self.setWindowTitle('Draggable Popup')
        self.layout = QVBoxLayout()

        self.header = QWidget(self, Qt.Widget)
        self.header_layout = QHBoxLayout()
        self.header_label = QLabel("Popup Header", self.header)
        self.close_button = QPushButton("X", self.header)
        self.close_button.clicked.connect(self.hide)
        self.close_button.setFixedSize(20, 20)

        self.header_layout.addWidget(self.header_label)
        self.header_layout.addWidget(self.close_button)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header.setLayout(self.header_layout)
        self.header.setFixedHeight(30)
        self.header.setStyleSheet("background: lightgrey;")
        
        self.layout.addWidget(self.header)
        self.content = QLabel("This is the popup content.", self)
        self.layout.addWidget(self.content)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: white;")

        self.header.mousePressEvent = self.headerMousePressEvent
        self.header.mouseMoveEvent = self.headerMouseMoveEvent

    def headerMousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.header_mouse_pos = event.pos()

    def headerMouseMoveEvent(self, event):
        if self.header_mouse_pos is not None:
            self.move(self.pos() + event.pos() - self.header_mouse_pos)

    def mouseReleaseEvent(self, event):
        self.header_mouse_pos = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 600, 400)
        
        self.button = QPushButton('Open Popup', self)
        self.button.clicked.connect(self.openPopup)
        self.button.move(250, 180)

        self.popup = DraggablePopup(self)

    def openPopup(self):
        self.popup.show()
        self.popup.move(150, 100)  # Adjust as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
