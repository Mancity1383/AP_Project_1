from Models.transacation import Transacation
from Utils.validation import Validation
from Database.database import database
from PyQt6 import QtCore, QtGui, QtWidgets
from Utils.show import Show


class Record:
    def __init__(self, type, ui):
        self.type = type
        self.ui = ui

    
    def record(self, username, le_date, le_price, le_description, combo_price_type, combo_price_source):
        username = username
        record_validation = Validation()
        price = le_price.text()
        date = le_date.text()
        description = le_description.text()
        type_of_price = combo_price_type.currentText()
        source_of_price = combo_price_source.currentText()

        if not record_validation.validate_price(price):
            le_price.setStyleSheet("border: 1px solid red")
            le_price.textChanged.connect(
                lambda: self.change_styles_price(le_price))
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid cost . It should be Postive Number.","invalid cost")
            return

        if not record_validation.validate_description(description):
            le_description.setStyleSheet("border: 1px solid red")
            le_description.textChanged.connect(self.change_styles_description)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid income . It should be lesser than 100.","invalid income")
            return
        if not record_validation.validate_type_of_price(type_of_price):
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid income . Choose one of the type of income","invalid income")
            return
        if not record_validation.validate_source_of_price(source_of_price):
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid income . Choose one of the source of income","invalid income")
            return
        record = Transacation(username, self.type,price, date,
                              source_of_price, description, type_of_price)
        record.save(self.ui)
        return True

    def change_styles_price(self, le_price):
        le_price.setStyleSheet("")


class TransactionController:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.validation = Validation()
        self.db = database()

    def record_income(self) -> None:
        result=Record("income", self.ui).record(self.ui.username, self.ui.dateEdit, self.ui.le_Income,
                                         self.ui.le_discription, self.ui.combo_incom_type, self.ui.combo_source)
        if result == True:
            return result
        else:
            return None

    def record_cost(self) -> None:
        result=Record("cost", self.ui).record(self.ui.username, self.ui.dateEdit, self.ui.le_cost,
                                       self.ui.le_discription, self.ui.combo_cost_type, self.ui.combo_source)
        if result == True:
            return result
        else:
            return None
    
    def add_category(self, category: str):
        if self.validation.validate_category(category):
            return self.db.add_category(self.ui.username, category)

    def get_source_of_price(self,username):
        source_of_price=self.db.get_source_of_price(username)
        return source_of_price
    
    def search(self, query: str, filter_search: dict, username: str):
        return self.db.search(query, filter_search, username)
    
    def reporting(self,filter_search: dict,username: str):
        return self.db.reporting(filter_search,username)