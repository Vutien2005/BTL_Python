import os
import sys
import datetime


def print_menu():
    print("=========================CHÀO MỪNG ĐẾN VỚI ỨNG DỤNG=========================")
    print("Chọn các chương trình trong danh sách(1-8): ")
    print("1. Danh bạ")
    print("2. Tin nhắn")
    print("3. Trò chơi")
    print("4. Lịch")
    print("5. Tính toán")
    print("6. Chat bot")
    print("7. Thoát")
def main():
    print_menu()
    choice = int(input("Nhập lựa chọn của bạn: "))
    while choice!= 7:
        if choice == 1:
            os.system("cls")
            os.system("python DanhBa\\danhba.py")
        elif choice == 2:
            os.system("cls")
            os.system("python Email\\email.py")
        elif choice == 3:
            os.system("cls")
            os.system("python Game\\game.py")
        elif choice == 4:
            os.system("cls")
            os.system("python Lich\\lich.py")
        elif choice == 5:
            os.system("cls")
            os.system("python TinhToan\\tinhtoan.py")
        elif choice == 6:
            os.system("cls")
            os.system("python ChatBot\\brain.py")
        elif choice == 7:
            print("Thoát chương trình")
            os.system("cls")
            sys.exit()
        print("Bạn đã chọn chức năng:", choice)
main()