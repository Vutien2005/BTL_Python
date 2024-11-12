import tkinter as tk
import random

def play_game(user_choice):
    options = {1: "Búa", 2: "Giấy", 3: "Kéo"}
    
    # Máy tính chọn ngẫu nhiên
    computer_choice = random.randint(1, 3)
    computer_move = options[computer_choice]
    
    # Hiển thị lựa chọn của máy tính
    label_computer_choice.config(text=f"Máy tính đã chọn: {computer_move}")
    
    # Kiểm tra kết quả trò chơi
    if user_choice == computer_move:
        result = "Hòa! Hãy thử lại."
    elif (user_choice == "Búa" and computer_move == "Kéo") or \
         (user_choice == "Kéo" and computer_move == "Giấy") or \
         (user_choice == "Giấy" and computer_move == "Búa"):
        result = "Bạn thắng!"
    else:
        result = "Bạn thua, máy tính thắng!"
    
    # Hiển thị kết quả trò chơi
    label_result.config(text=result)

# Cấu hình cửa sổ chính
root = tk.Tk()
root.title("Trò Chơi Kéo Búa Bao")

# Thay đổi kích thước cửa sổ (chiều rộng x chiều cao)
root.geometry("400x400")  # Bạn có thể thay đổi số 400x400 thành kích thước mong muốn

# Các nút cho lựa chọn của người chơi
button_rock = tk.Button(root, text="Búa", width=20, height=2, command=lambda: play_game("Búa"))
button_rock.pack(pady=20)

button_paper = tk.Button(root, text="Giấy", width=20, height=2, command=lambda: play_game("Giấy"))
button_paper.pack(pady=20)

button_scissors = tk.Button(root, text="Kéo", width=20, height=2, command=lambda: play_game("Kéo"))
button_scissors.pack(pady=20)

# Nhãn hiển thị lựa chọn của máy tính
label_computer_choice = tk.Label(root, text="Máy tính đã chọn: ", font=("Helvetica", 14))
label_computer_choice.pack(pady=10)

# Nhãn hiển thị kết quả trò chơi
label_result = tk.Label(root, text="Kết quả: ", font=("Helvetica", 14))
label_result.pack(pady=20)

# Chạy ứng dụng Tkinter
root.mainloop()
