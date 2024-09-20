import random
import os
import sys
import datetime

def nap_the(money):
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = file.read()
    with open("Game\\tai_xiu.txt", "w") as file:
        file.write(str(float(tk) + money))
    with open("Game\\lich_su_nap.txt", "a") as file:
        file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} - Đã nạp thêm {money}VND\n')


def kt_tk():
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = file.read()
    print(f'Tài khoản hiện tại của bạn có {tk}VND')


def roll_dice():
    dice = []
    for i in range(3):
        dice.append(random.randint(1, 6))
    return dice
def nap_tien():
    tien = float(input("Nhập số tiền bạn muốn nạp: "))
    with open("Game\\tai_xiu.txt", "w") as file:
        file.write(tien)
    with open("Game\\lich_su_nap.txt", "a") as file:
        file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} - Đã nạp thêm {tien}VND\n')
def return_tx(dice):
    diem = sum(dice)
    if 11 <= diem <= 18:
        return "t"
    elif 3 <= diem <= 10:
        return "x"
    

def return_lich_su():
    with open("Game\\lich_su_nap.txt", "r") as file:
        content = file.read()
        if content == "":
            print("Bạn chưa có ghi chú nào.")
        else:
            print("Lịch sử nạp tiền:")
            print(content)
def rut_tien():
    tien = input("Nhập số tiền bạn muốn rút: ")
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = file.read()
    print(f'Tài khoản của bạn hiện có: {tk}VND')
    if float(tk) < float(tien):
        print("Tài khoản của bạn không đủ để rút.")
    else:
        with open("Game\\tai_xiu.txt", "w") as file:
            file.write(str(float(tk) - float(tien)))
        with open("Game\\lich_su_rut.txt", "a") as file:
            file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} - Đã rút {tien}VND\n')
def play_game():
    print("Chào mừng đến với trò chơi may mắn")
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = file.read()
    if float(tk) == 0:
        print("Tài khoản của bạn không đủ để tham gia, bạn cần nạp thêm.")
        ans = input("Bạn có muốn nạp tiền không (Y/N): ")
        if ans.lower() == "y":
            nap_tien()
            os.system("cls")
            play_game()
        else:
            print("Cảm ơn bạn đã chơi!")
            os.system("python main.py")
    else:
        tien_hien_tai = float(tk)
        print(f"Tài khoản của bạn hiện tại: {tien_hien_tai}VND")
        cuoc = int(input("Nhập số tiền đặt vào: "))
        while cuoc > tien_hien_tai:
            print("Số tiền bạn đặt vào quá cao. Vui lòng chọn lại.")
            cuoc = int(input("Nhập số tiền đặt vào: "))

        choice = input("Nhập lựa chọn của bạn (t/x): ")
        dice = roll_dice()
        check = return_tx(dice)
        print(f"Đã xuất hiện: {dice}")
        if choice.lower() == check:
            print("Bạn đã trúng xúc xắc!")
            tien_hien_tai += cuoc
            with open("Game\\tai_xiu.txt", "w") as file:
                file.write(str(tien_hien_tai))
            print(f"Tài khoản của bạn đã được cộng thêm {cuoc}")
        else:
            print("Bạn đã thua!")
            tien_hien_tai -= cuoc
            with open("Game\\tai_xiu.txt", "w") as file:
                file.write(str(tien_hien_tai))
            print(f"Tài khoản của bạn đã bị trừ đi {cuoc}")
        ans = input("Bạn có muốn tiếp tục chơi hay không (Y/N): ")
        if ans.lower() == "n":
            print("Cảm ơn bạn đã chơi!")
            os.system("python main.py")
        else:
            os.system("cls")
            play_game()

def main():
    while True:
        os.system("cls")
        print("==================CHÀO MỪNG ĐẾN VỚI GAME======================")
        print("1. Chơi game")
        print("2. Nạp tiền")
        print("3. Kiểm tra tài khoản")
        print("4. Lịch sử nạp tiền")
        print("5. Rút tiền")
        print("6. Thoát")
        choice = int(input("Chọn chức năng: "))
        if choice == 1:
            os.system("cls")
            print("TRANG CHỦ CHƠI GAME")
            play_game()
        elif choice == 2:
            os.system("cls")
            print("TRANG CHỦ NẠP THẺ")
            money = int(input("Nhập số tiền bạn muốn nạp: "))
            nap_the(money)
            print(f'Đã nạp thành công {money}VND')
            enter = input("Nhấn ENTER để tiếp tục: ")
        elif choice == 3:
            os.system("cls")
            print("TRANG CHỦ KIỂM TRA TÀI KHOẢN")
            kt_tk()
            enter = input("Nhấn ENTER để tiếp tục: ")
        elif choice == 4:
            os.system("cls")
            print("TRANG CHỦ LỊCH SỬ NẠP TIỀN")
            return_lich_su()
            enter = input("Nhấn ENTER để tiếp tục: ")
        elif choice == 5:
            os.system("cls")
            print("TRANG CHỦ RÚT TIỀN") 
            rut_tien()
            enter = input("Nhấn ENTER để tiếp tục: ")
        elif choice == 6:
            print("Cảm ơn bạn đã chơi!")
            sys.exit(0)

main()