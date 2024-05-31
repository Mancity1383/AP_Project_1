from Database.database import database

from save import ISave
class Transacation(Save):
    def __init__(self,username,type,price,date,source_of_price,description,type_of_price):
        super().__init__()
        self.username:str=username
        self.type:str=type
        self.price:str=price
        self.date:str=date
        self.source_of_price:str=source_of_price
        self.description:str=description
        self.type_of_price:str=type_of_price


        self.db = database()

    def save(self, ui):
        super().save()
        """ Save user informations to database. """
        new_transaction = [self.username, self.type, self.price, self.date,
                           self.source_of_price, self.description, self.type_of_price]
        self.db.save_new_transaction(new_transaction)
