# 예금통장
import sqlite3

class DepositAccount:
    def __init__(self):
        self.db_connection = sqlite3.connect('bank.db')
        self.db_cursor = self.db_connection.cursor()
        self.create_table()

    def create_table(self):
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password TEXT DEFAULT '',
                account_number TEXT,
                balance INTEGER DEFAULT 0,
                account_type TEXT DEFAULT '',
                interest_rate FLOAT DEFAULT 0.0,
                period FLOAT DEFAULT 0.0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS deposit (
                account_number TEXT,
                transaction_type TEXT,
                amount INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db_connection.commit()

    def check_transactions(self, account_number):
        self.db_cursor.execute("SELECT * FROM deposit WHERE account_number = ?", (account_number,))
        transactions = self.db_cursor.fetchall()
        if transactions:
            print("----------거래내역----------")
            for transaction in transactions:
                account_number, transaction_type, amount, timestamp = transaction
                
                print(f"계좌 번호: {account_number}")
                print(f"거래 유형: {transaction_type}")
                print(f"거래 금액: {amount} 원")
                print(f"거래 일시: {timestamp}")
                print("--------------------")
        else:
            print("거래 내역이 없습니다.")
            print("--------------------")

    def withdraw(self, account_number):
        self.db_cursor.execute("SELECT balance, interest_rate, period FROM users WHERE account_number = ?", (account_number,))
        balance, interest_rate, period = self.db_cursor.fetchone()
        

        interest = balance * interest_rate * period
        new_balance = int(balance + interest)

        print(f"예금 해지 시 받는 금액은 {new_balance} 원입니다.")
        print("--------------------")

    def display_balance(self, account_number):
        self.db_cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
        balance = self.db_cursor.fetchone()[0]
        print(f"현재 금액: {balance} 원")
        print("--------------------")


    def create_account(self, username, account_number, initial_balance, interest_rate, period):
        self.db_cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.db_cursor.fetchone()

        if user:
            self.db_cursor.execute("INSERT INTO users (username, account_number, balance, account_type, interest_rate, period) VALUES (?, ?, ?, ?, ?, ?)",
                               (username, account_number, initial_balance, "예금", interest_rate, period))
            self.db_cursor.execute("INSERT INTO deposit (account_number, transaction_type, amount) VALUES (?, ?, ?)", (account_number, "신규가입", initial_balance))
            self.db_connection.commit()

        print("예금 계좌가 개설되었습니다.")
        print("--------------------")