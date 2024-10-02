import tkinter as tk
from tkinter import messagebox
import os


if not os.path.exists("DanhBa"):
    os.makedirs("DanhBa")


def print_effect():
    response_text.set("Chọn chức năng để thao tác")


def add_contact_ui():
    clear_inputs()
    response_text.set("Nhập tên và số điện thoại để thêm:")
    name_label.pack()
    name_entry.pack(pady=5)
    phone_label.pack()
    phone_entry.pack(pady=5)
    confirm_button.config(text="Xác nhận thêm", command=lambda: add_contact(name_entry.get(), phone_entry.get()))
    confirm_button.pack(pady=5)

def add_contact(name, phone_number):
    if name and phone_number:
        with open("DanhBa/sdt.txt", "a", encoding="utf-8") as file:
            file.write(f"{name},{phone_number}\n")
        response_text.set("Liên lạc đã được thêm!")
    else:
        response_text.set("Vui lòng nhập đầy đủ thông tin.")
    clear_inputs()


def list_contacts():
    clear_inputs()
    try:
        with open("DanhBa/sdt.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()
            if contacts:
                contact_list = "\n".join([f"{name.strip()}: {phone.strip()}" for name, phone in [contact.split(",") for contact in contacts]])
                response_text.set(f"Danh sách liên lạc:\n{contact_list}")
            else:
                response_text.set("Danh sách liên lạc trống.")
    except FileNotFoundError:
        response_text.set("Chưa có liên lạc nào được lưu.")

def delete_contact_ui():
    clear_inputs()
    response_text.set("Nhập tên liên lạc cần xóa:")
    name_label.pack()
    name_entry.pack(pady=5)
    confirm_button.config(text="Xác nhận xóa", command=lambda: delete_contact(name_entry.get()))
    confirm_button.pack(pady=5)

def delete_contact(name):
    try:
        with open("DanhBa/sdt.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()

        with open("DanhBa/sdt.txt", "w", encoding="utf-8") as file:
            found = False
            for contact in contacts:
                name_in_file, phone_number = contact.strip().split(",")
                if name_in_file != name:
                    file.write(contact)
                else:
                    found = True
            if found:
                response_text.set(f"Liên lạc {name} đã được xóa.")
            else:
                response_text.set(f"Liên lạc {name} không tồn tại.")
    except FileNotFoundError:
        response_text.set("Chưa có liên lạc nào để xóa.")
    clear_inputs()

def search_contact_ui():
    clear_inputs()
    response_text.set("Nhập tên liên lạc cần tìm:")
    name_label.pack()
    name_entry.pack(pady=5)
    confirm_button.config(text="Tìm kiếm", command=lambda: search_contact(name_entry.get()))
    confirm_button.pack(pady=5)

def search_contact(name):
    try:
        with open("DanhBa/sdt.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()
            found = False
            for contact in contacts:
                name_in_file, phone_number = contact.strip().split(",")
                if name_in_file == name:
                    response_text.set(f"Tìm thấy liên lạc {name} với số điện thoại: {phone_number}")
                    found = True
                    break
            if not found:
                response_text.set(f"Liên lạc {name} không tìm thấy.")
    except FileNotFoundError:
        response_text.set("Chưa có liên lạc nào được lưu.")
    clear_inputs()


def clear_inputs():
    name_label.pack_forget()
    name_entry.pack_forget()
    phone_label.pack_forget()
    phone_entry.pack_forget()
    confirm_button.pack_forget()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


def exit_program():
    window.quit()


window = tk.Tk()
window.title("Quản lý danh bạ liên lạc")
window.geometry("400x500")

response_text = tk.StringVar()
response_label = tk.Label(window, textvariable=response_text, wraplength=350, justify="left")
response_label.pack(pady=10)


name_label = tk.Label(window, text="Tên liên lạc:")
name_entry = tk.Entry(window)

phone_label = tk.Label(window, text="Số điện thoại:")
phone_entry = tk.Entry(window)


confirm_button = tk.Button(window, text="Xác nhận")


add_button = tk.Button(window, text="Thêm liên lạc", command=add_contact_ui)
add_button.pack(pady=5)

list_button = tk.Button(window, text="Xem danh sách", command=list_contacts)
list_button.pack(pady=5)

delete_button = tk.Button(window, text="Xóa liên lạc", command=delete_contact_ui)
delete_button.pack(pady=5)

search_button = tk.Button(window, text="Tìm liên lạc", command=search_contact_ui)
search_button.pack(pady=5)

exit_button = tk.Button(window, text="Thoát", command=exit_program)
exit_button.pack(pady=5)


print_effect()
window.mainloop()
