import os
import sys
import math

def print_menu():
    print("=========================CHÀO MỪNG ĐẾN VỚI MÁY TÍNH THÔNG MINH============= ============")
    print("Chọn các chương trình trong danh sách(1-9): ")
    print("1. Phuong trinh bậc hai")
    print("2. Phuong trinh bậc một")
    print("3. Tính toán")
    print("4. Hệ phương trình bậc nhất")
    print("5. Tính lũy thừa")
    print("6. Thoát")

def pt_b2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem.")
        return None
    elif delta == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return [x1, x2]
def pt_b1(a, b):
    if a == 0:
        if b == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
        return None
    else:
        x = -b / a
        return [x]
def tinh_toan():
    bieu_thuc = input("Nhập biểu thức muốn tính: ")
    kq = eval(bieu_thuc)
    print(f"Kết quả tính toán: {kq}")
def he_pt_b1(a, b, c, d, e, f):
    dem=a/d
    y=(f*dem-c)/(e*dem-b)
    x=(f*(b/e)-c)/(d*(b/e)-a)
    return [x, y]

def luy_thua():
    so = int(input("Nhập số cơ số: "))
    mu = int(input("Nhập số mũ: "))
    result = math.pow(so, mu)
    print(f"{so} mũ {mu} bằng: {result}")
    enter = input("Nhấn ENTER để tiếp tục.")


def main():
    while True:
        os.system("cls")
        print_menu()
        choice = int(input("Chọn chức năng: "))
        if choice == 1:
            os.system("cls")
            print("GIẢI PHƯƠNG TRÌNH BẬC 2")
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            c = float(input("Nhập c: "))
            result = pt_b2(a, b, c)
            if result is not None:
                print("Nghiệm(s) của phuong trình bậc hai:", result)
            enter = input("Nhấn ENTER để tiếp tục.")
        elif choice == 2:
            os.system("cls")
            print("GIẢI PHƯƠNG TRÌNH BẬC 1")
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            result = pt_b1(a, b)
            if result is not None:
                print("Nghiệm của phuong trình bậc nhất:", result)
            enter = input("Nhấn ENTER để tiếp tục.")
        elif choice == 3:
            os.system("cls")
            print("TÍNH TOÁN BIỂU THỨC")
            tinh_toan()
            enter = input("Nhấn ENTER để tiếp tục.")
        elif choice == 4:
            os.system("cls")
            print("GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN")
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            c = float(input("Nhập c: "))
            d = float(input("Nhập d: "))
            e = float(input("Nhập e: "))
            f = float(input("Nhập f: "))
            result = he_pt_b1(a, b, c, d, e, f)
            if result is not None:
                print("Nghiệm của hệ phương trình bậc nhất:", result)
            enter = input("Nhấn ENTER để tiếp tục.")
        elif choice == 5:
            os.system("cls")
            print("TÍNH LŨY THỪA")
            luy_thua()
        elif choice == 6:
            os.system("cls")
            os.system("python main.py")

main()