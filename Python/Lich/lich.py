import datetime
import os
import calendar

def print_effect():
    print("Các chức năng chính: ")
    print("1. Hiển thị lịch của tháng")
    print("2. Khởi tạo lịch hẹn")
    print("3. Ghi chú lịch")
    print("4. Thoát")

def display_calendar():
    print("XEM LỊCH")
    year = int(input("Năm: "))
    month = int(input("Tháng: "))
    calendar.setfirstweekday(calendar.MONDAY)
    print(calendar.month(year, month))
    enter = input("Nhấn ENTER để tiếp tục")
    os.system("cls")


def create_schedule():
    print("TẠO SỰ KIỆN THÔNG BÁO")
    event_name = input("Tên sự kiện: ")
    event_date = input("Ngày (dd/mm/yyyy): ")
    event_time = input("Giờ (hh:mm): ")
    with open("Lich\\date.txt", "a", encoding="utf-8") as file:
        file.write(f"{event_date} {event_time}: {event_name}\n")
        print("Lịch hẹn đã được tạo.")
    enter = input("Nhấn ENTER để tiếp tục")
    os.system("cls")

def write_note():
    print("GHI CHÚ LỊCH")
    event_date = input("Ngày (dd/mm/yyyy): ")
    note_content = input("Nội dung ghi chú: ")
    with open("Lich\\note.txt", "a", encoding="utf-8") as file:
        file.write(f"{event_date}: {note_content}\n")
        print("Ghi chú đã được ghi.")
    enter = input("Nhấn ENTER để tiếp tục")
    os.system("cls")

def main():
    while True:
        print_effect()
        choice = int(input("Chọn chức năng (1-4): "))
        if choice == 1:
            os.system("cls")
            display_calendar()
        elif choice == 2:
            os.system("cls")
            create_schedule()
        elif choice == 3:
            os.system("cls")
            write_note()
        elif choice == 4:
            os.system("cls")
            print("Chương trình đã thoát.")
            os.system("python main.py")
            break
        else:
            print("Chọn sai chức năng. Vui lòng chọn lại.")
main()