import datetime
import os
import sys
def print_effect():
    print("Các chức năng chính: ")
    print("1. Thêm liên lạc mới")
    print("2. Xem danh sách liên lạc")
    print("3. Xóa liên lạc")
    print("4. Tìm kiếm liên lạc")
    print("5. Thoát")

def add_contact():
    print("Thêm liên lạc mới")
    name = input("Tên: ")
    phone_number = input("Số điện thoại: ")
    with open("DanhBa\\sdt.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{phone_number}\n")
        print("Liên lạc đã được thêm")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def list_contacts():
    print("Danh sách liên lạc")
    with open("DanhBa\\sdt.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()
        print("Danh sách liên lạc:")
        for contact in contacts:
            name, phone_number = contact.strip().split(",")
            print(f"{name}: {phone_number}")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def delete_contact():
    print("Xóa liên lạc")
    with open("DanhBa\\sdt.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()
        print("Danh sách liên lạc cần xóa:")
        temp = 0
        for contact in contacts:
            temp += 1
            name = contact.strip().split(",")
            print(temp, ". ", name)
    number = int(input("Số liên lạc cần xóa: ")) -1
    with open("DanhBa\\sdt.txt", "w", encoding="utf-8") as file:
        for i in range(len(contacts)):
            if i != number:
                file.write(contacts[i])
        print("Liên lạc đã được xóa")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")

def search_contact():
    print("Tìm kiếm liên lạc")
    name = input("Tên liên lạc cần tìm: ")
    with open("DanhBa\\sdt.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()
        found = False
        for contact in contacts:
            name_in_file, phone_number = contact.strip().split(",")
            if name_in_file == name:
                found = True
                print(f"Tìm thấy liên lạc {name} với số điện thoại: {phone_number}")
        if found == False:
            print(f"Liên lạc {name} không tìm thấy")
    enter = input("Nhấn ENTER để tiếp tục: ")
    os.system("cls")
def main():
    while True:
        print_effect()
        choice = input("Chọn chức năng: ")
        if choice == "1":
            os.system("cls")
            add_contact()
        elif choice == "2":
            os.system("cls")
            list_contacts()
        elif choice == "3":
            os.system("cls")
            delete_contact()
        elif choice == "4":
            os.system("cls")
            search_contact()
        elif choice == "5":
            print("Thoát chương trình")
            os.system("cls")
            os.system("python main.py")
main()