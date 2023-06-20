# 입출금통장
import sqlite3

class BankAccount:
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
                balance INTEGER,
                account_type TEXT DEFAULT '',
                interest_rate FLOAT DEFAULT 0.0,
                period FLOAT DEFAULT 0.0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                account_number TEXT,
                transaction_type TEXT,
                amount INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db_connection.commit()

    def deposit(self, account_number, amount):
        self.db_cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
        balance = self.db_cursor.fetchone()[0]
        new_balance = balance + amount
        self.db_cursor.execute("UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, account_number))
        self.db_cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)",
                               (account_number, "입금", amount))
        self.db_connection.commit()
        print(f"입금 완료했습니다. 입금 후 잔액은 {new_balance} 원입니다.")
        print("--------------------")

    def withdraw(self, account_number, amount):
        self.db_cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
        balance = self.db_cursor.fetchone()[0]
        if balance >= amount:
            new_balance = balance - amount
            self.db_cursor.execute("UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, account_number))
            self.db_cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)", (account_number, "출금", amount))
            self.db_connection.commit()
            print(f"출금 완료했습니다. 출금 후 잔액은 {new_balance} 원입니다.")
            print("--------------------")
        else:
            print("출금할 잔액이 부족합니다.")
            print("--------------------")

    def check_transactions(self, account_number):
        self.db_cursor.execute("SELECT * FROM transactions WHERE account_number = ?", (account_number,))
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

    def display_balance(self, account_number):
        self.db_cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
        balance = self.db_cursor.fetchone()[0]
        print(f"현재 금액: {balance} 원")
        print("--------------------")


    def create_account(self, username, account_number, initial_balance):
        self.db_cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.db_cursor.fetchone()

        if user:
            self.db_cursor.execute("INSERT INTO users (username, account_number, balance, account_type) VALUES (?, ?, ?, ?)",
                               (username, account_number, initial_balance, "입출금"))
            self.db_cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (?, ?, ?)", (account_number, "신규개설", initial_balance))
            self.db_connection.commit()

        print("입출금 계좌가 개설되었습니다.")
        print("--------------------")
