#Code một chương trình tin nhắn bao gồm các chương trình nhỏ : Nhập tin nhắn, xem hộp thư đến, hộp thư đi, xóa tin nhắn trong các hôp

import os
import datetime
def print_menu():
    print("\n========================= CHÀO MỪNG ĐẾN VỚI HỘP THOẠI TIN NHẮN ==========================")
    print("Chọn chức năng của bạn: ")
    print("1. Nhập tin nhắn")
    print("2. Xem hộp thư đến")
    print("3. Xem hộp thư đi")
    print("4. Xóa tin nhắn")
    print("5. Thoát")

def create_mess():
    print("Nhập tin nhắn")
    nguoi_nhan = input("Nhập tên người nhận: ")
    with open("DanhBa\\sdt.txt", 'r', encoding='utf-8') as file:
        for i in file:
            ten, sdt = i.strip().split(',')
            if ten == nguoi_nhan:
                with open("Email\\hop_thu_di.txt", 'a', encoding='utf-8') as file:
                    file.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {input('Nhập nội dung tin nhắn: ')} - Tới {nguoi_nhan} \n")
                    print("Đã gửi tin nhắn")
                    enter = input("Nhấn ENTER để tiếp tục: ")
                    os.system("cls")
                    return
        print("Tên người nhận không tồn tại trong danh bạ.")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def view_inbox():
    print("Hộp thư đến")
    with open("Email\\hop_thu_den.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        if content == "":
            print("Hộp thư đến đang trống.")
        else:
            print(content)
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def view_outbox():
    print("Hộp thư đi")
    with open("Email\\hop_thu_di.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        if content == "":
            print("Hộp thư đi đang trống.")
        else:
            print(content)
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def delete_mess():
    print("Xóa tin nhắn")
    print("1. Hộp thư đến")
    print("2. Hộp thư đi")
    choice = int(input("Chọn hộp thư cần xóa tin nhắn: "))
    if choice == 1:
        with open("Email\\hop_thu_den.txt", 'r', encoding='utf-8') as file:
            content = file.read()
            if content == "":
                print("Hộp thư đến đang trống.")
                return
            else:
                print(content)
                stt_xoa = int(input("Chọn stt tin nhắn cần xóa: "))
                lines = content.split('\n')
                del lines[stt_xoa - 1]
                with open("Email\\hop_thu_den.txt", 'w', encoding='utf-8') as file:
                    file.write('\n'.join(lines))
                    print("Tin nhắn đã xóa.")
    elif choice == 2:
        with open("Email\\hop_thu_di.txt", 'r', encoding='utf-8') as file:
            content = file.read()
            if content == "":
                print("Hộp thư đi đang trống.")
                return
            else:
                print(content)
                stt_xoa = int(input("Chọn stt tin nhắn cần xóa: "))
                lines = content.split('\n')
                del lines[stt_xoa - 1]
                with open("Email\\hop_thu_di.txt", 'w', encoding='utf-8') as file:
                    file.write('\n'.join(lines))
                    print("Tin nhắn đã xóa.")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def main():
    while True:
        print_menu()
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
            os.system("cls")
            create_mess()
        elif choice == 2:
            os.system("cls")
            view_inbox()
        elif choice == 3:
            os.system("cls")
            view_outbox()
        elif choice == 4:
            os.system("cls")
            delete_mess()
        elif choice == 5:
            os.system("cls")
            print("Đã thoát chương trình.")
            os.system("python main.py")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

main()
 