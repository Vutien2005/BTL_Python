import speech_recognition as sr
import datetime
import pyttsx3
import cv2

# Khởi tạo đối tượng pyttsx3 để phát âm thanh
rb_m = pyttsx3.init()

while True:
    # Khởi tạo đối tượng Recognizer
    recognizer = sr.Recognizer()
    
    # Sử dụng microphone để thu âm
    with sr.Microphone() as mic:
        print("Please say something:")
        audio = recognizer.listen(mic)
    
    # Nhận diện giọng nói
    try:
        you = recognizer.recognize_google(audio)
        print("You said:", you)
    except sr.UnknownValueError:
        you = ""
        print("I couldn't understand. Please repeat.")
    except sr.RequestError:
        you = ""
        print("Request error. Check your internet connection.")

    # Xử lý phản hồi
    if you == "":
        response = "I didn't catch that."
    elif "hello" in you.lower():  # .lower() to handle case-insensitivity
        response = "Hello Tran Anh Tu"
    elif "today" in you.lower():
        response = "Today is " + str(datetime.date.today())
    elif "time" in you.lower():
        now = datetime.datetime.now()
        response = "Current time is " + now.strftime("%H:%M:%S")
    elif "open camera" in you.lower():
        # Mở camera mặc định
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            response = "Cannot open camera"
            print(response)
        else:
            response = "Camera opened. Press 'q' to exit."
            print(response)
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                cv2.imshow('Camera Frame', frame)
                # Nhấn 'q' để thoát
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            response = "Camera closed."
    elif "bye" in you.lower():
        response = "Goodbye Tran Anh Tu"
        print("rb:", response)
        rb_m.say(response)
        rb_m.runAndWait()
        break
    else:
        response = "I'm here to help!"

    # In và phát phản hồi
    print("rb:", response)
    rb_m.say(response)
    rb_m.runAndWait()
