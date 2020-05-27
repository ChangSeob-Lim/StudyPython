import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    # 생성자
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 안에 들어가는 항목
        exitAction = QAction(QIcon('./data/exit.png'), 'Exit', self) #리눅스 상에서 아이콘 안나옴
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        # 메뉴바 생성하고 목록 추가
        menubar = self.menuBar() 
        #menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 버튼 추가
        button = QPushButton('Quit', self)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(self.btn_clicked)

        # 윈폼 만들기
        self.setWindowTitle('My Qt App')
        self.setWindowIcon(QIcon('./data/box.png'))
        #self.move(200, 200)
        #self.resize(640, 400)
        self.setGeometry(100, 100, 640, 400)
        self.show()

    def btn_clicked(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    exit(app.exec_())