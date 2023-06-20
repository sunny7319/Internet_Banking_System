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


if __name__ == "__main__":
    main = Main()