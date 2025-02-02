from PyQt6 import QtCore, QtGui, QtWidgets
from Controlers.transaction_controllet import TransactionController
from Utils.show import Show
from Views.font import Font_detail
class Ui_Category(object):
    def __init__(self):
        self.username="username"
        self.style="style"
        self.font=Font_detail()

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.resize(316, 146)
        font = QtGui.QFont()
        font.setPointSize(14 * self.font.font_size)
        font.setBold(True)
        font.setItalic(True)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)


        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.category_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.category_lbl.setFont(font)
        self.category_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.category_lbl)
        
        self.le_category = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.verticalLayout.addWidget(self.le_category)
        
        self.add_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.verticalLayout.addWidget(self.add_btn)
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 22))

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)

        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)

        self.MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtGui.QAction(parent=self.MainWindow)
        self.actionhelp = QtGui.QAction(parent=self.MainWindow)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        
        self.controller = TransactionController(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add category"))
        self.category_lbl.setText(_translate("MainWindow", "Add Category"))
        self.le_category.setPlaceholderText(
            _translate("MainWindow", "Enter category name"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
    
    def add_btn_clicked(self) -> None:
        check=""
        if self.le_category.text():
            check=self.controller.add_category(self.le_category.text())
            if not check:
                Show(QtWidgets.QMessageBox.Icon.Information,"This category alredy exist","Category Exist")
        else:
            Show(QtWidgets.QMessageBox.Icon.Critical,"Please write your category name","Error")
        if check:
            QtCore.QTimer.singleShot(2000,self.hide)
            Show(QtWidgets.QMessageBox.Icon.Information,"Your Category Added","Category Added")