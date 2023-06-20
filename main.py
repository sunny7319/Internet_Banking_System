from login import LoginSystem
from bank_account import BankAccount
from saving_account import SavingAccount
from deposit_account import DepositAccount
import sys


class Main:
    name = "써니뱅크"

    def __init__(self):
        while True:
            print(f"{self.name}입니다.")
            self.login_menu()



    def login_menu(self):
        login_system = LoginSystem()
        print("다음 중 하나를 선택해 주세요.")
        choice = int(input("1. 로그인\t 2. 회원가입\t 3. 종료\n"))

        if choice == 1:
            login_system.login()
            self.account_menu()
        elif choice == 2:
            login_system.signup()
        else:
            print("--------------------")
            print("오픈뱅킹 서비스를 종료합니다.")
            sys.exit()



    def account_menu(self):
        print("다음 중 하나를 선택해 주세요.")
        choice = int(input("1. 입출금통장\t 2. 적금통장\t 3. 예금통장\t 4. 종료\n"))
        print("--------------------")

        if choice == 1:
            self.bank_account_menu()
        elif choice == 2:
            self.saving_account_menu()
        elif choice == 3:
            self.deposit_account_menu()
        else:
            print("오픈뱅킹 서비스를 종료합니다.")
            sys.exit()



    def bank_account_menu(self):
        bank_account = BankAccount()
        print("입출금 화면입니다. 무엇을 도와드릴까요?")
        choice = int(input("1. 거래내역 보기\t 2. 입금\t 3. 출금\t 4. 현재 금액 보기\n5. 신규계좌 개설하기\t 6. 뒤로가기\t 7. 종료\n"))
        
        if choice == 1:
            account_number = input("계좌번호를 입력하세요: ")
            bank_account.check_transactions(account_number)
            self.bank_account_menu()

        elif choice == 2:
            print("----------입금----------")
            account_number = input("계좌번호를 입력하세요: ")
            amount = int(input("입금할 금액을 입력하세요: "))
            bank_account.deposit(account_number, amount)
            self.bank_account_menu()

        elif choice == 3:
            print("----------출금----------")
            account_number = input("계좌번호를 입력하세요: ")
            amount = int(input("출금할 금액을 입력하세요: "))
            bank_account.withdraw(account_number, amount)
            self.bank_account_menu()
        
        elif choice == 4:
            account_number = input("계좌번호를 입력하세요: ")
            bank_account.display_balance(account_number)
            self.bank_account_menu()
        
        elif choice == 5:
            print("----------신규계좌 개설----------")
            username = input("이름을 입력하세요: ")
            account_number = input("계좌번호를 입력하세요: ")
            initial_deposit = 0   # 초기금액
            bank_account.create_account(username, account_number, initial_deposit)
            self.bank_account_menu()
        
        elif choice == 6:
            self.account_menu()
        
        else:
            print("--------------------")
            print("오픈뱅킹 서비스를 종료합니다.")
            sys.exit()



    def saving_account_menu(self):
        saving_account = SavingAccount()
        print("자유적금 화면입니다. 무엇을 도와드릴까요?")
        choice = int(input("1. 거래내역 보기\t 2. 적금\t 3. 만기해지 시 받는 금액 계산\t 4. 현재 금액\n5. 신규계좌 개설\t 6. 뒤로가기\t 7. 종료\n"))

        if choice == 1:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            saving_account.check_transactions(account_number)
            self.saving_account_menu()

        elif choice == 2:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            amount = int(input("적금할 금액을 입력하세요: "))
            saving_account.deposit(account_number, amount)
            self.saving_account_menu()

        elif choice == 3:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            saving_account.withdraw(account_number)
            self.saving_account_menu()

        elif choice == 4:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            saving_account.display_balance(account_number)
            self.saving_account_menu()

        elif choice == 5:
            print("----------신규계좌 개설----------")
            print("가입하고 싶은 상품을 선택하세요.")
            choice_i = int(input("1. 이자율: 3%, 기간: 6개월\t 2. 이자율: 5%, 기간: 12개월\n"))
            
            if choice_i == 1:
                i = 0.03
                period = 0.5
            else:
                i = 0.05
                period = 1
            
            username = input("이름을 입력하세요: ")
            account_number = input("계좌번호를 입력하세요: ")
            initial_deposit = int(input("초기 입금할 금액을 입력하세요: "))

            saving_account.create_account(username, account_number, initial_deposit, i, period)
            self.saving_account_menu()

        elif choice == 6:
            print("--------------------")
            self.account_menu()

        else:
            print("--------------------")
            print("오픈뱅킹 서비스를 종료합니다.")
            sys.exit()



    def deposit_account_menu(self):
        deposit_account = DepositAccount()
        print("예금 화면입니다. 무엇을 도와드릴까요?")
        choice = int(input("1. 거래내역 보기\t 2. 만기해지 시 받는 금액 계산\t 3. 현재 금액\n4. 신규계좌 개설\t 5. 뒤로가기\t 6. 종료\n"))

        if choice == 1:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            deposit_account.check_transactions(account_number)
            self.deposit_account_menu()

        elif choice == 2:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            deposit_account.withdraw(account_number)
            self.deposit_account_menu()

        elif choice == 3:
            print("--------------------")
            account_number = input("계좌번호를 입력하세요: ")
            deposit_account.display_balance(account_number)
            self.deposit_account_menu()

        elif choice == 4:
            print("----------신규계좌 개설----------")
            print("가입하고 싶은 상품을 선택하세요.")
            choice_i = int(input("1. 이자율: 3.5%, 기간: 6개월\t 2. 이자율: 6%, 기간: 12개월\n"))
            
            if choice_i == 1:
                i = 0.035
                period = 0.5
            else:
                i = 0.06
                period = 1
            
            username = input("이름을 입력하세요: ")
            account_number = input("계좌번호를 입력하세요: ")
            initial_deposit = int(input("초기 입금할 금액을 입력하세요: "))

            deposit_account.create_account(username, account_number, initial_deposit, i, period)
            self.deposit_account_menu()

        elif choice == 5:
            print("--------------------")
            self.account_menu()

        else:
            print("--------------------")
            print("오픈뱅킹 서비스를 종료합니다.")
            sys.exit()





# class Main:
#     name = "써니뱅크"

#     def __init__(self):
#         self.db_connection = sqlite3.connect('bank.db')
#         self.db_cursor = self.db_connection.cursor()
#         self.create_table()
#         self.login_menu()

#     def create_table(self):
#         self.db_cursor.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT,
#                 password TEXT,
#                 account_number TEXT,
#                 balance INTEGER,
#                 transaction_type TEXT,
#                 amount INTEGER,
#                 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
        
#         self.db_connection.commit()

if __name__ == "__main__":
    main = Main()
    # main.login_menu()



#     def open_account(self):
#         print("계좌 개설 화면으로 이동합니다.")
#         print("다음 중 하나를 선택해 주세요.")
#         print("1. 입출금통장\t2. 적금통장\t3. 예금통장")
        
#         choice = int(input())

#         if choice == 1:
#             self.new_bank_account()
#         elif choice == 2:
#             self.new_savings_account()
#         elif choice == 3:
#             self.new_deposit_account()
#         else:
#             print("잘못된 선택입니다.")

#     # 신규 입출금통장
#     def new_bank_account(self):
#         account_name = input("이름을 입력하세요: ")
#         account_number = input("계좌번호를 입력하세요: ")
#         initial_deposit = 0

#         account = BankAccount(initial_deposit)
#         account.display_balance()

#         self.accounts.append((account_name, account_number, account))

#         print("입출금통장 개설이 완료되었습니다.")

#         print("로그아웃 하시겠습니까?\t 1. 예\t 2. 아니요")
#         chioce = int(input())
#         if chioce == 1:
#             self.logout
#         else:


#     # 신규 적금통장
#     def new_savings_account(self):
#         account_name = input("이름을 입력하세요: ")
#         account_number = input("계좌번호를 입력하세요: ")
#         initial_deposit = int(input("초기 입금액을 입력하세요: "))

#         account = SavingsProgram(initial_deposit)

#         self.accounts.append((account_number, account_name, account))

#         print("적금통장 개설이 완료되었습니다.")
#         account.display_balance()

#     # 신규 예금통장
#     def new_deposit_account(self):
#         account_name = input("이름을 입력하세요: ")
#         account_number = input("계좌번호를 입력하세요: ")
#         initial_deposit = int(input("초기 입금액을 입력하세요: "))

#         account = DepositProgram(initial_deposit)
        
#         self.accounts.append((account_number, account_name, account))

#         print("예금통장 개설이 완료되었습니다.")
#         account.display_balance()

    

#     def logout(self):
#         self.logged_in = False
#         print("로그아웃 되었습니다.")
#         while 1:
#             break