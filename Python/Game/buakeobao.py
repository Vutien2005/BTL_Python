import random

def rock_paper_scissors():
    options = {1: "Búa", 2: "Giấy", 3: "Kéo"}
    
    while True:
        # Máy tính chọn ngẫu nhiên
        computer_choice = random.randint(1, 3)
        computer_move = options[computer_choice]
        
        # Hiển thị lựa chọn của máy tính ngay lập tức
        print(f"Máy tính đã chọn ngẫu nhiên: {computer_move}")
        
        # Người dùng nhập lựa chọn
        user_move = input("Hãy chọn (Búa, Giấy, Kéo): ").capitalize()
        
        # Xác định người chiến thắng
        if user_move == computer_move:
            print("Hòa! Hãy thử lại.")
        elif (user_move == "Búa" and computer_move == "Kéo") or \
             (user_move == "Kéo" and computer_move == "Giấy") or \
             (user_move == "Giấy" and computer_move == "Búa"):
            print("Bạn thắng!")
        else:
            print("Bạn thua, máy tính thắng!")
        
        # Hỏi người chơi có muốn chơi lại không
        play_again = input("Bạn có muốn chơi lại không? (c/k): ").lower()
        if play_again != 'c':
            print("Cảm ơn bạn đã chơi!")
            break

rock_paper_scissors()
