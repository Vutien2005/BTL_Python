import os
import sys
import datetime
from deep_translator import GoogleTranslator    
import random

def print_effect():
    print("Các chức năng mà tôi có thể giúp đỡ bạn: ")
    print("- Hiển thị thời gian thực")
    print("- Trao đổi thông tin")
    print("- Lưu trữ ghi chú")
    print("- Hiển thị ghi chú của bạn")
    print("- Mở ứng dụng")
    print("- Mở các ứng dụng game trên điện thoại giả lập của bạn")
    print("- Hiển thị thông tin thời tiết")
    print("- Tìm kiếm thông tin trên Google")
    print("- Dịch ngôn ngữ")
    print("- Tính toán một biểu thức")
    print("- Nghe nhạc")
    print("- Chơi game")

def get_time():
    print(f'Bot:\nThời gian hiện tại là: {datetime.datetime.now().strftime("%H:%M:%S")}')
def get_info():
    thead = input("Tiêu đề ghi chú: ")
    content = input("Nội dung ghi chú: ")
    with open('Data\\log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} - {thead}: {content}\n')
        print('Ghi chú đã được lưu.')
def show_info():
    with open('Data\\log.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        if content == "":
            print('Bạn chưa có ghi chú nào.')
        else:
            print('Ghi chú của bạn:')
            print(content)
def open_apps():
    print("Tôi có thể mở các ứng dụng như Chrome, File Explorer")

    chosse_app = input("Nhập tên ứng dụng: ")
    if chosse_app.lower() == "chrome":
        os.system("start C:\\Users\\Public\\Desktop\\chrome")
    elif chosse_app.lower() == "file explorer":
        os.system("start file explorer")
def google_search(duong_dan):
    link = '+'.join(duong_dan.split())
    os.system(f"start chrome https://www.google.com/search?q={link}")
    print(f'Bot: Đang tìm kiếm "{duong_dan}" trên Google.')
def show_code_language():
    print("Danh sách mã ngôn ngữ bạn có thể sử dụng") 
    print("Danh sách mã ngôn ngữ:")
    print("af: Tiếng Afrikaans")
    print("ar: Tiếng Ả Rập")
    print("bg: Tiếng Bulgaria")
    print("bn: Tiếng Bengal")
    print("ca: Tiếng Catalan")
    print("cs: Tiếng Séc")
    print("da: Tiếng Đan Mạch")
    print("de: Tiếng Đức")
    print("el: Tiếng Hy Lạp")
    print("en: Tiếng Anh")
    print("es: Tiếng Tây Ban Nha")
    print("et: Tiếng Estonia")
    print("fa: Tiếng Ba Tư")
    print("fi: Tiếng Phần Lan")
    print("fr: Tiếng Pháp")
    print("gu: Tiếng Gujarati")
    print("he: Tiếng Hebrew")
    print("hi: Tiếng Hindi")
    print("hr: Tiếng Croatia")
    print("hu: Tiếng Hungary")
    print("id: Tiếng Indonesia")
    print("it: Tiếng Ý")
    print("ja: Tiếng Nhật")
    print("kn: Tiếng Kannada")
    print("ko: Tiếng Hàn")
    print("lt: Tiếng Lithuania")
    print("lv: Tiếng Latvia")
    print("ml: Tiếng Malayalam")
    print("mr: Tiếng Marathi")
    print("ms: Tiếng Malaysia")
    print("nl: Tiếng Hà Lan")
    print("no: Tiếng Na Uy")
    print("pl: Tiếng Ba Lan")
    print("pt: Tiếng Bồ Đào Nha")
    print("ro: Tiếng Romania")
    print("ru: Tiếng Nga")
    print("sk: Tiếng Slovak")
    print("sl: Tiếng Slovenia")
    print("sr: Tiếng Serbia")
    print("sv: Tiếng Thụy Điển")
    print("ta: Tiếng Tamil")
    print("te: Tiếng Telugu")
    print("th: Tiếng Thái")
    print("tr: Tiếng Thổ Nhĩ Kỳ")
    print("uk: Tiếng Ukraina")
    print("ur: Tiếng Urdu")
    print("vi: Tiếng Việt")
    print("zh-cn: Tiếng Trung Quốc (Giản thể)")
    print("zh-tw: Tiếng Trung Quốc (Phồn thể)")
         

def play_music():
    song = input("Nhập tên bài hát bạn muốn nghe: ")
    os.system(f"start chrome https://www.youtube.com/results?search_query={'+'.join(song.split())}")
    print(f"Bot: Đang tìm kiếm bài hát '{song}' trên YouTube.")


def get_weather():
    print("Bot: Thời tiết hôm nay nắng, nhiệt độ 30°C.")
def translate_text():
    text = input("Nhập văn bản cần dịch: ")
    show_code_language()
    ngon_ngu = input("Nhập mã ngôn ngữ dịch (ví dụ: en cho tiếng Anh, vi cho tiếng Việt): ")
    translation = GoogleTranslator(source='auto', target=ngon_ngu).translate(text)
    print(f"Bot: Bản dịch: {translation}")

def calculator():
    phep_tinh = input("Nhập phép tính (ví dụ: 5 + 3 * 2): ")
    try:
        kq = eval(phep_tinh)
        print(f"Bot: Kết quả phép tính trên:  {kq}")
    except:
        print("Bot: Có vấn đề với phép tính đầu vào của bạn.")
def mini_game():
    print("Chơi game đơn giản!")
    os.system("python Game\\lucky.py")


def get_message(user):
    if "chào" in user.lower().strip():
        print('Bot: Chào mừng đến với chúng tôi!')  
    elif "tạm biệt" in user.lower().strip():
        print('Bot: Tạm biệt!')
        exit(0)
        os.system("python main.py")
    elif ("thời gian") in user.lower().strip(): 
        get_time()
    elif "chức năng" in user.lower().strip():
        print_effect()
    elif "thêm ghi chú" in user.lower().strip():
        get_info()
    elif "hiển thị ghi chú" in user.lower().strip():
        show_info()
    elif "ứng dụng" in user.lower().strip():
        open_apps()
    elif "tìm kiếm" in user.lower().strip():
        duong_dan = input("Bạn muốn tìm kiếm gì: ")
        google_search(duong_dan)
    elif "thời tiết" in user.lower().strip():
        get_weather()
    elif "dịch" in user.lower().strip():
        translate_text()
    elif "tính" in user.lower().strip():
        calculator()
    elif "nhạc" in user.lower().strip():
        play_music()
    elif ("game" or "trò chơi") in user.lower().strip():
        mini_game()
def main():
    print("Bạn đã đến với ChatBot!")
    print_effect()
    while True:
        user_input = input("Bạn: ")
        get_message(user_input)


main()