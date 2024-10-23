import os
import datetime
from deep_translator import GoogleTranslator    
import tkinter as tk
from tkinter import simpledialog, messagebox
import webbrowser

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        
        self.chat_box = tk.Text(root, state='disabled', wrap='word')
        self.chat_box.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.bind('<Return>', self.send_message)

        self.print_effect()

    def print_effect(self):
        self.display_message("Các chức năng mà tôi có thể giúp đỡ bạn: \n"
                             "- Hiển thị thời gian thực\n"
                             "- Trao đổi thông tin\n"
                             "- Lưu trữ ghi chú\n"
                             "- Hiển thị ghi chú của bạn\n"
                             "- Mở ứng dụng\n"
                             "- Hiển thị thông tin thời tiết\n"
                             "- Tìm kiếm thông tin trên Google\n"
                             "- Dịch ngôn ngữ\n"
                             "- Tính toán một biểu thức\n"
                             "- Nghe nhạc\n"
                             "- Chơi game\n")
        

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, "Bot: " + message + "\n")
        self.chat_box.config(state='disabled')
        self.chat_box.see(tk.END)

    def send_message(self, event):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.display_message("Bạn: " + user_input)
        self.get_message(user_input)

    def get_time(self):
        now = datetime.datetime.now()
        self.display_message(f'Thời gian hiện tại là: {now.strftime("%H:%M:%S")}')

    def get_info(self):
        title = simpledialog.askstring("Ghi chú", "Tiêu đề ghi chú:")
        content = simpledialog.askstring("Ghi chú", "Nội dung ghi chú:")
        if title and content:
            with open('Data/log.txt', 'a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} - {title}: {content}\n')
                self.display_message('Ghi chú đã được lưu.')

    def show_info(self):
        try:
            with open('Data/log.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                if content == "":
                    self.display_message('Bạn chưa có ghi chú nào.')
                else:
                    self.display_message('Ghi chú của bạn:\n' + content)
        except FileNotFoundError:
            self.display_message('Không tìm thấy file ghi chú.')

    def open_apps(self):
        app = simpledialog.askstring("Mở ứng dụng", "Nhập tên ứng dụng (ví dụ: Chrome):")
        if app.lower() == "valorant":
            os.system("start C:\\Users\\Public\\Desktop\\VALORANT.lnk")
        elif app.lower() == "chrome":
            webbrowser.open("chrome")
        else:
            self.display_message("Ứng dụng không hỗ trợ.")

    def google_search(self, query):
        link = '+'.join(query.split())
        webbrowser.open(f"https://www.google.com/search?q={link}")
        self.display_message(f'Đang tìm kiếm "{query}" trên Google.')

    def get_weather(self):
        self.display_message("Thời tiết hôm nay nắng, nhiệt độ 29°C.")

    def translate_text(self):
        text = simpledialog.askstring("Dịch văn bản", "Nhập văn bản cần dịch:")
        if text:
            code = simpledialog.askstring("Chọn ngôn ngữ", "Nhập tên ngôn ngữ (ví dụ: Anh, Việt Nam, Pháp):")
            language_codes = {
                "anh": 'en',
                "việt nam": 'vi',
                "pháp": 'fr',
                "hà lan": 'nl',
                "đức": 'de',
                "tây ban nha": 'es',  # Sửa mã ngôn ngữ từ "nz" thành "es"
                "trung quốc": 'zh-cn',  # Sửa mã ngôn ngữ thành mã cho tiếng Trung Quốc (Giản thể)
                "hungary": 'hu',
                "thái lan": 'th',
                "israel": 'he',  # Sửa mã ngôn ngữ cho tiếng Hebrew
                "islandia": 'is',
                "nhật bản": 'ja',  # Sửa mã ngôn ngữ cho tiếng Nhật
                "hàn quốc": 'ko'  # Sửa mã ngôn ngữ cho tiếng Hàn
            }

            code = language_codes.get(code.lower().strip(" "), code)

            try:    
                translation = GoogleTranslator(source='auto', target=code).translate(text)
                self.display_message(f"Bạn: {text}")
                self.display_message(f"Bản dịch: {translation}")
            except Exception as e:
                self.display_message(f"Lỗi dịch: {str(e)}")

    def play_music(self):
        song = simpledialog.askstring("Nghe nhạc", "Nhập tên bài hát bạn muốn nghe:")
        if song:
            webbrowser.open(f"https://www.youtube.com/results?search_query={'+'.join(song.split())}")
            self.display_message(f"Đang tìm kiếm bài hát '{song}' trên YouTube.")

    def get_message(self, user):
        if "chào" in user.lower().strip():
            self.display_message('Chào mừng đến với chúng tôi!')
        elif "tạm biệt" in user.lower().strip():
            self.display_message('Tạm biệt!')
            self.root.quit()
        elif "thời gian" in user.lower().strip(): 
            self.get_time()
        elif "thêm ghi chú" in user.lower().strip():
            self.get_info()
        elif "hiển thị ghi chú" in user.lower().strip():
            self.show_info()
        elif "mở ứng dụng" in user.lower().strip():
            self.open_apps()
        elif "tìm kiếm" in user.lower().strip():
            query = simpledialog.askstring("Tìm kiếm", "Bạn muốn tìm kiếm gì:")
            if query:
                self.google_search(query)
        elif "thời tiết" in user.lower().strip():
            self.get_weather()
        elif "dịch" in user.lower().strip():
            self.translate_text()
        elif "nhạc" in user.lower().strip():
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = ChatBot(root)
    root.mainloop()
