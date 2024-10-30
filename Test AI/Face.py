# Import thư viện OpenCV
import cv2

# Mở kết nối với camera (ID=0)
cap = cv2.VideoCapture(0)

# Tạo bộ phân loại để nhận diện khuôn mặt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Vòng lặp chính để xử lý video từ camera
while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Kiểm tra nếu không thể đọc từ camera
    if not ret:
        print("Không thể đọc từ camera")
        break

    # Chuyển đổi frame sang ảnh xám
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt trong frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vẽ hộp xung quanh khuôn mặt và hiển thị tên "Person" trên mỗi khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Person", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Hiển thị frame với khuôn mặt được nhận diện
    cv2.imshow('Face Detection', frame)

    # Thoát vòng lặp nếu nhấn phím cách
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# Giải phóng camera và đóng cửa sổ hiển thị
cap.release()
cv2.destroyAllWindows()