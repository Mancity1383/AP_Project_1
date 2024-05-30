import sqlite3


class database:
    """ This class is for coonecting to database.db. """
    def __init__(self) -> None:
        self.conn = sqlite3.connect("Database/database.db")
        self.cur = self.conn.cursor()

    def save_new_user(self, user_data: list[str], ui) -> None:
        """ Save user information in db file. """
        # create table if it's not already created.
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, first_name TEXT NOT NULL,last_name TEXT NOT NULL,email TEXT NOT NULL,password TEXT NOT NULL,phone TEXT NOT NULL,city TEXT NOT NULL,birthday TEXT NOT NULL,security_q TEXT NOT NULL,PRIMARY KEY(username));")
        try:
            self.cur.execute(
            "INSERT INTO user(first_name, last_name, username, phone, password, email, city, birthday, security_q) VALUES (?,?,?,?,?,?,?,?,?);", user_data,)
        except sqlite3.IntegrityError:
            # show error message because username is our PRIMARY KEY and should be unique.
            ui.show_error("This username is already chosen.")
        self.conn.commit()
        # self.conn.close()
    def save_new_transaction(self, transaction_data: list[str]) -> None:
        """ Save user information in db file. """
        # create table if it's not already created.
        self.cur.execute("CREATE TABLE IF NOT EXISTS transaction(username TEXT NOT NULL,type TEXT NOT NULL, price TEXT NOT NULL,date TEXT NOT NULL,source_of_price TEXT NOT NULL,description TEXT NOT NULL,type_of_price TEXT NOT NULL,FOREIGN KEY('username') REFERENCES 'user'('username'));")
        self.cur.execute(
        "INSERT INTO transaction(username, type, price, date, source_of_price, description, type_of_price) VALUES (?,?,?,?,?,?,?);", transaction_data,)
        self.conn.commit()
        # self.conn.close()
    def check_user(self, username: str, password: str) -> bool:
        self.cur.execute("SELECT * From user WHERE username=? AND password=?;", (username, password))
        result = self.cur.fetchone()

        return True if result else False
    
    def check_security_question(self,username:str,security_q:str) -> bool:
        self.cur.execute("SELECT * From user WHERE username=? AND security_q=?;", (username, security_q))
        result = self.cur.fetchone()
    
        return True if result else False

    def find_user_email(self,username):
        self.cur.execute("SELECT * From user WHERE username=?;", (username,))
        result = self.cur.fetchone()
        user_email=result[3]
        return user_email
    def find_user_password(self,username):
        self.cur.execute("SELECT * From user WHERE username=?;", (username,))
        result = self.cur.fetchone()
        password=result[4]
        return password
        
    
    

