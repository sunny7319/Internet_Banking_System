import sqlite3
import sys

class LoginSystem:
    def __init__(self):
        self.db_connection = sqlite3.connect('bank.db')
        self.db_cursor = self.db_connection.cursor()
        self.create_table()

    def create_table(self):
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password TEXT,
                account_number TEXT DEFAULT '',
                balance INTEGER DEFAULT 0,
                account_type TEXT DEFAULT '',
                interest_rate FLOAT DEFAULT 0.0,
                period FLOAT DEFAULT 0.0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db_connection.commit()

    def login(self):
        print("-----------로그인----------")
        username = input("이름을 입력하세요 : ")
        password = input("비밀번호를 입력하세요 : ")

        self.db_cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.db_cursor.fetchone()

        if user:
            print("로그인 되었습니다.")
            print("--------------------")
        else:
            print("일치하는 이름 또는 비밀번호가 없습니다.")
            print("--------------------")
            print("회원가입 하시겠습니까?")
            choice = int(input("1. 예\t 2. 아니요 다시 로그인 하겠습니다.\n"))

            if choice == 1:
                self.signup()
            else:
                self.login()

    def signup(self):
        print("-----------회원가입----------")
        username = input("이름을 입력하세요 : ")
        password = input("비밀번호를 입력하세요 : ")

        self.db_cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        exist_user = self.db_cursor.fetchone()

        if exist_user:
            print("회원정보가 있습니다. 다시 로그인 해주세요.")
            self.login()
        else:
            self.db_cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.db_connection.commit()

            print("회원가입 되었습니다.")
            print("--------------------")
            print("로그인 하시겠습니까?")
            choice = int(input("1. 예\t 2. 아니요 종료하겠습니다.\n"))

            if choice == 1:
                self.login()
            else:
                print("--------------------")
                print("오픈뱅킹 서비스를 종료합니다.")
                sys.exit()

    def close(self):
        self.db_cursor.close()
        self.db_connection.close()


    # def login_menu(self):
    #     print("다음 중 하나를 선택해 주세요.")
    #     choice = int(input("1. 로그인\t 2. 회원가입\t 3. 종료\n"))

    #     if choice == 1:
    #         self.login()
    #     elif choice == 2:
    #         self.signup()
    #     else:
    #         print("--------------------")
    #         print("오픈뱅킹 서비스를 종료합니다.")


# if __name__ == "__main__":
#     login_system = LoginSystem()
#     try:
#         login_system.create_table()
#         login_system.login_menu()
#     finally:
#         login_system.close()
