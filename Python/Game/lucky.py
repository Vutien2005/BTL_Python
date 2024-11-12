import random
import os
import sys
import datetime

# Kiểm tra và tạo thư mục và tệp nếu không tồn tại
def create_directory_and_file():
    if not os.path.exists("Game"):
        os.makedirs("Game")
    if not os.path.exists("Game\\tai_xiu.txt"):
        with open("Game\\tai_xiu.txt", "w") as file:
            file.write("0")
    if not os.path.exists("Game\\lich_su_nap.txt"):
        open("Game\\lich_su_nap.txt", "w").close()
    if not os.path.exists("Game\\lich_su_rut.txt"):
        open("Game\\lich_su_rut.txt", "w").close()

# Hàm nạp thẻ và ghi lịch sử nạp tiền vào tệp
def nap_the():
    create_directory_and_file()
    try:
        money = float(input("Nhập số tiền bạn muốn nạp: "))
        with open("Game\\tai_xiu.txt", "r") as file:
            tk = float(file.read())
        with open("Game\\tai_xiu.txt", "w") as file:
            file.write(str(tk + money))
        with open("Game\\lich_su_nap.txt", "a", encoding="UTF-8") as file:
            file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Đã nạp {money} VND\n')
        print(f'Đã nạp thành công {money} VND')
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ.")

# Hàm kiểm tra tài khoản
def kt_tk():
    create_directory_and_file()
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = file.read()
    print(f'Tài khoản hiện tại của bạn có {tk} VND')

# Hàm quăng xúc xắc
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

# Hàm xác định "Tài" hoặc "Xỉu"
def return_tx(dice):
    diem = sum(dice)
    if 11 <= diem <= 18:
        return "t"  # "Tài"
    elif 3 <= diem <= 10:
        return "x"  # "Xỉu"

# Hàm hiển thị lịch sử nạp tiền từ tệp trực tiếp
def return_lich_su_nap():
    create_directory_and_file()
    try:
        with open("Game\\lich_su_nap.txt", "r", encoding="UTF-8") as file:
            content = file.read()
            if content:
                print("Lịch sử nạp tiền:")
                print(content)  # Hiển thị nội dung lịch sử nạp tiền
            else:
                print("Bạn chưa có lịch sử nạp tiền.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc lịch sử nạp tiền: {e}")


# Hàm hiển thị lịch sử rút tiền từ tệp trực tiếp
def return_lich_su_rut():
    create_directory_and_file()
    try:
        with open("Game\\lich_su_rut.txt", "r", encoding="UTF-8") as file:
            content = file.read()
            if content:
                print("Lịch sử rút tiền:")
                print(content)  # Hiển thị nội dung lịch sử rút tiền
            else:
                print("Bạn chưa có lịch sử rút tiền.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc lịch sử rút tiền: {e}")


# Hàm rút tiền và ghi lịch sử rút tiền vào tệp
def rut_tien():
    create_directory_and_file()
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = float(file.read())
    print(f"Tài khoản của bạn hiện có: {tk} VND")
    
    try:
        tien = float(input("Nhập số tiền bạn muốn rút: "))
        if tk < tien:
            print("Tài khoản của bạn không đủ để rút.")
        else:
            with open("Game\\tai_xiu.txt", "w") as file:
                file.write(str(tk - tien))
            with open("Game\\lich_su_rut.txt", "a", encoding="UTF-8") as file:
                file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Đã rút {tien} VND\n')
            print(f"Bạn đã rút thành công {tien} VND")
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ.")

# Hàm chơi game
def play_game():
    create_directory_and_file()
    print("Chào mừng đến với trò chơi may mắn")
    with open("Game\\tai_xiu.txt", "r") as file:
        tk = float(file.read())
    if tk == 0:
        print("Tài khoản của bạn không đủ để tham gia, bạn cần nạp thêm.")
        ans = input("Bạn có muốn nạp tiền không (Y/N): ")
        if ans.lower() == "y":
            nap_the()
            play_game()
        else:
            print("Cảm ơn bạn đã chơi!")
            return  # Quay lại menu chính
    else:
        print(f"Tài khoản của bạn hiện tại: {tk} VND")
        try:
            cuoc = float(input("Nhập số tiền đặt vào: "))
            while cuoc > tk:
                print("Số tiền bạn đặt vào quá cao. Vui lòng chọn lại.")
                cuoc = float(input("Nhập số tiền đặt vào: "))
            
            choice = input("Nhập lựa chọn của bạn (t/x): ")
            dice = roll_dice()
            check = return_tx(dice)
            print(f"Kết quả xúc xắc: {dice}")
            if choice.lower() == check:
                winnings = cuoc * 1.6
                tk += winnings
                print(f"Bạn đã thắng! Tài khoản của bạn đã được cộng thêm {winnings} VND")
            else:
                tk -= cuoc
                print(f"Bạn đã thua! Tài khoản của bạn đã bị trừ đi {cuoc} VND")

            with open("Game\\tai_xiu.txt", "w") as file:
                file.write(str(tk))

            ans = input("Bạn có muốn tiếp tục chơi không (Y/N): ")
            if ans.lower() == "n":
                print("Cảm ơn bạn đã chơi!")
                return  # Quay lại menu chính
            else:
                play_game()
        except ValueError:
            print("Vui lòng nhập số tiền hợp lệ.")


# Hàm chính
def main():
    while True:
        os.system("cls")
        print("==================CHÀO MỪNG ĐẾN VỚI GAME======================")
        print("1. Chơi game")
        print("2. Nạp tiền")
        print("3. Kiểm tra tài khoản")
        print("4. Lịch sử nạp tiền")
        print("5. Lịch sử rút tiền")
        print("6. Rút tiền")
        print("7. Thoát")
        try:
            choice = int(input("Chọn chức năng: "))
            if choice == 1:
                os.system("cls")
                play_game()
            elif choice == 2:
                os.system("cls")
                nap_the()
                input("Nhấn ENTER để tiếp tục: ")
            elif choice == 3:
                os.system("cls")
                kt_tk()
                input("Nhấn ENTER để tiếp tục: ")
            elif choice == 4:
                os.system("cls")
                return_lich_su_nap()
                input("Nhấn ENTER để tiếp tục: ")
            elif choice == 5:
                os.system("cls")
                return_lich_su_rut()
                input("Nhấn ENTER để tiếp tục: ")
            elif choice == 6:
                os.system("cls")
                rut_tien()
                input("Nhấn ENTER để tiếp tục: ")
            elif choice == 7:
                print("Cảm ơn bạn đã chơi!")
                sys.exit(0)
            else:
                print("Vui lòng chọn một số từ 1 đến 7.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

# Chạy chương trình
main()
