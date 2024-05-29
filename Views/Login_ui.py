from PyQt6 import QtCore, QtGui, QtWidgets
from Views.forgetpassword import *
from Controlers.user_controller import UserController

class Ui_Login(object):

    def open_window_forgetpage(self):

        class Forgetpage(QtWidgets.QMainWindow, ForgetPassword):

            def __init__(self):
                super().__init__()

                self.setupUi(self)
        self.ui = Forgetpage()
        self.ui.show()
        self.ui.setWindowTitle("Forget Password Page")
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.check_count = 0
        self.ban=False
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(parent=self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(30, 0, 501, 561))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(r"pictures\730_generated.jpg"))
        self.picture.setObjectName("picture")
        self.loginpage_l = QtWidgets.QLabel(parent=self.centralwidget)
        self.loginpage_l.setGeometry(QtCore.QRect(680, 40, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Lalezar")
        font.setPointSize(30)
        self.loginpage_l.setFont(font)
        self.loginpage_l.setObjectName("loginpage_l")
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(590, 200, 361, 31))
        self.username.setText("")
        self.error_l=QtWidgets.QLabel("You are banned for 60 seconds".title(),parent=self.centralwidget)
        self.error_l.setGeometry(QtCore.QRect(590, 170, 361, 31))
        self.error_l.setStyleSheet("color:red")
        self.error_l.setObjectName("error")
        self.error_l.hide()
        self.username.setObjectName("username")
        self.username.textChanged.connect(self.username_changed)
        self.time = QtCore.QTime.currentTime()
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(590, 260, 361, 31))
        self.password.setObjectName("password")
        self.password.textChanged.connect(self.password_changed)
        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(590, 354, 361, 31))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0763e5;
                        color: #000000;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color:#1AA7EC ;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }
                """)
        self.login_btn.clicked.connect(self.pressed_login_btn)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(570, 420, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.forget_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.forget_btn.setGeometry(QtCore.QRect(590, 470, 361, 31))
        self.forget_btn.setObjectName("forget_btn")
        self.forget_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0763e5;
                        color: #000000;
                        border-radius: 15px;
                        border: 2px #1AA7EC;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color:#1AA7EC ;
                    }
                    QPushButton:pressed {
                        background-color: #1AA7EC;
                    }
                """)
        self.forget_btn.clicked.connect(self.forget_password_clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginpage_l.setText(_translate("MainWindow", "Login Page"))
        self.username.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.forget_btn.setText(_translate("MainWindow", "Forgot Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def pressed_login_btn(self):

        if self.ban:
            self.check_count = 0
            second=QtCore.QTime.currentTime().second() == self.time.second()
            minutes=QtCore.QTime.currentTime().minute() == self.time.minute()
            hour=QtCore.QTime.currentTime().hour() == self.time.hour()
            self.error_l.show()
            if hour and minutes and second:
                self.ban=False
        if self.ban == False:
            self.username.setStyleSheet(" ")
            self.password.setStyleSheet(" ")
            if self.check_count == 3:
                self.ban=True
                self.time=QtCore.QTime.currentTime().addSecs(60)
            login_check = UserController(self)
            if login_check.login(self.username,self.password):
                pass
            else:
                self.username.setStyleSheet("border: 1px solid red")
                self.password.setStyleSheet("border: 1px solid red")
                self.check_count += 1

    def forget_password_clicked(self):
        self.open_window_forgetpage()

    def username_changed(self):
        self.username.setStyleSheet("")

    def password_changed(self):
        self.password.setStyleSheet("")







