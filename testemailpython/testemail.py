import smtplib
import imaplib
import email
from email.header import decode_header
import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog

ten_dang_nhap = "tpython056@gmail.com"
mat_khau = "ikav ugyg rvgi gwob"

def gui_email(chu_de, nguoi_nhan, noi_dung):
    nguoi_nhan += '@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(ten_dang_nhap, mat_khau)
        server.sendmail(ten_dang_nhap, nguoi_nhan, f"Subject: {chu_de}\n\n{noi_dung}")
        messagebox.showinfo("Thành công", "Email đã được gửi thành công!")
        with open("hop_thu_di.txt", 'a', encoding='utf-8') as f:
            f.write(f"Tiêu đề: {chu_de}\n")
            f.write(f"Người nhận: {nguoi_nhan}\n")
            f.write(f"Nội dung:\n{noi_dung}\n")
            f.write("=" * 50 + "\n")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể gửi email: {str(e)}")
    finally:
        server.quit()

def xem_hop_thu_di():
    try:
        with open("hop_thu_di.txt", 'r', encoding='utf-8') as file:
            content = file.readlines()
            if content:
                emails = "".join(content)
                hien_thi_cua_so_texte("Hộp Thư Đi", emails)
            else:
                messagebox.showinfo("Thông báo", "Hộp thư đi đang trống.")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy hộp thư đi.")

def kiem_tra_hop_thu_den():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(ten_dang_nhap, mat_khau)
        mail.select("inbox")
        status, messages = mail.search(None, 'ALL')
        if status != 'OK':
            messagebox.showerror("Lỗi", "Không thể tìm email.")
            return
        email_ids = messages[0].split()
        email_ids = email_ids[-5:]
        emails = []
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            if status != 'OK':
                continue
            msg = email.message_from_bytes(msg_data[0][1])
            chu_de, encoding = decode_header(msg["Subject"])[0]
            if isinstance(chu_de, bytes):
                chu_de = chu_de.decode(encoding if encoding else 'utf-8')
            tu = msg.get("From")
            if msg.is_multipart():
                body = ""
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
            emails.append(f"Nhận từ: {tu}\nTiêu đề: {chu_de}\nNội dung:\n{body}\n")
        if emails:
            noi_dung_email = "\n".join(emails)
            hien_thi_cua_so_texte("Hộp Thư Đến", noi_dung_email)
            with open("hop_thu_den.txt", 'a', encoding='utf-8') as f:
                f.write(noi_dung_email)
                f.write("=" * 50 + "\n")
        else:
            messagebox.showinfo("Thông báo", "Không có email mới.")
        mail.logout()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể kiểm tra hộp thư đến: {str(e)}")

def hien_thi_cua_so_texte(tieu_de, noi_dung):
    text_window = tk.Toplevel(root)
    text_window.title(tieu_de)
    text_area = scrolledtext.ScrolledText(text_window, width=60, height=20)
    text_area.pack()
    text_area.insert(tk.END, noi_dung if noi_dung else "Không có nội dung.")
    text_area.configure(state='disabled')

def soan_thu():
    soan= tk.Toplevel(root)
    soan.title("Soạn Thư")
    tk.Label(soan, text="Tiêu đề:").pack()
    title_entry = tk.Entry(soan)
    title_entry.pack()
    tk.Label(soan, text="Người nhận:").pack()
    recipient_entry = tk.Entry(soan)
    recipient_entry.pack()
    tk.Label(soan, text="Nội dung:").pack()
    content_text = tk.Text(soan, height=10)
    content_text.pack()
    tk.Button(soan, text="Gửi", command=lambda: gui_email(title_entry.get(), recipient_entry.get(), content_text.get("1.0", tk.END))).pack()

def xoa_tin_nhan():
    loai_xoa = simpledialog.askstring("Xóa Tin Nhắn", "Bạn muốn xóa (1) Hộp Thư Đến hay (2) Hộp Thư Đi? (Nhập 1 hoặc 2)")
    if loai_xoa == "1":
        try:
            open("hop_thu_den.txt", 'w').close()
            messagebox.showinfo("Thành công", "Đã xóa tất cả tin nhắn trong hộp thư đến.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa hộp thư đến: {str(e)}")
    elif loai_xoa == "2":
        try:
            open("hop_thu_di.txt", 'w').close()
            messagebox.showinfo("Thành công", "Đã xóa tất cả tin nhắn trong hộp thư đi.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa hộp thư đi: {str(e)}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập 1 hoặc 2.")

def thoat():
    if messagebox.askokcancel("Thoát", "Bạn có chắc chắn muốn thoát?"):
        root.destroy()

root = tk.Tk()
root.title("Hộp Thư Điện Tử")
tk.Button(root, text="Soạn Thư", command=soan_thu).pack(pady=5)
tk.Button(root, text="Xem Hộp Thư Đi", command=xem_hop_thu_di).pack(pady=5)
tk.Button(root, text="Kiểm Tra Hộp Thư Đến", command=kiem_tra_hop_thu_den).pack(pady=5)
tk.Button(root, text="Xóa Tin Nhắn", command=xoa_tin_nhan).pack(pady=5)
tk.Button(root, text="Thoát", command=thoat).pack(pady=5)

root.mainloop()
