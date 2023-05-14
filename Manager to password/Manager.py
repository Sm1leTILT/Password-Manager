from PyQt5 import QtWidgets, QtGui, QtCore

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle('Password Manager')
        self.resize(800, 600)

    def initUI(self):
        self.btn_add_pwd = QtWidgets.QPushButton('Add Password')
        self.pwd_list = QtWidgets.QListWidget()

        h_layout = QtWidgets.QHBoxLayout()
        v_layout = QtWidgets.QVBoxLayout()

        h_layout.addStretch(6)
        h_layout.addWidget(self.btn_add_pwd, stretch=2)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.pwd_list)

        self.setLayout(v_layout)

class PasswordWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()

        self.initUI()
        self.setWindowTitle('Password Window')
        self.resize(200, 100)

    def initUI(self):
        v_layout = QtWidgets.QVBoxLayout()

        h_1 = QtWidgets.QHBoxLayout()
        h_2 = QtWidgets.QHBoxLayout()
        h_3 = QtWidgets.QHBoxLayout()
        h_4 = QtWidgets.QHBoxLayout()

        self.btn_edit = QtWidgets.QPushButton('Edit Password')
        self.btn_close = QtWidgets.QPushButton('Close')
        self.btn_copy = QtWidgets.QPushButton('Copy')

        self.servise_edit = QtWidgets.QLineEdit()
        self.login_edit = QtWidgets.QLineEdit()
        self.pwd_edit = QtWidgets.QLineEdit()

        self.pwd_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        servise_lbl = QtWidgets.QLabel('Service:')
        login_lbl = QtWidgets.QLabel('Login:')
        pwd_lbl = QtWidgets.QLabel('Password:')

        h_1.addWidget(servise_lbl, stretch=3)
        h_1.addWidget(self.servise_edit, stretch=5)

        h_2.addWidget(login_lbl, stretch=3)
        h_2.addWidget(self.servise_edit, stretch=5)

        h_3.addWidget(pwd_lbl, stretch=3)
        h_3.addWidget(self.servise_edit, stretch=5)

        v_layout.addLayout(h_1)
        v_layout.addLayout(h_2)
        v_layout.addLayout(h_3)

        self.setLayout(v_layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
