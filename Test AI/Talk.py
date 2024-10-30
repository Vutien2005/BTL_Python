import speech_recognition
import datetime
import pyttsx3

rb_m = pyttsx3.init()

while True:
    rb = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as mic:
        print("Hãy nói gì đó:")
        audio = rb.listen(mic)
        
    try:
        you = rb.recognize_google(audio, language="vi-VN")  # Chỉ định ngôn ngữ là tiếng Việt
        you = you.lower()  # Chuyển thành chữ thường để dễ so sánh
    except:
        you = ""
        rb = "Xin lỗi, tôi không nghe rõ. Bạn có thể nói lại không?"
        rb_m.say(rb)
        rb_m.runAndWait()
        continue
    
    print("Bạn nói: " + you)

    if "xin chào" in you:
        rb = "Xin chào! Tôi có thể giúp gì cho bạn?"
    elif "hôm nay" in you or "ngày" in you:
        rb = "Hôm nay là " + str(datetime.date.today())
    elif "mấy giờ" in you:
        now = datetime.datetime.now()
        rb = "Bây giờ là " + now.strftime("%H:%M:%S")
    elif "tạm biệt" in you or "chào" in you:
        rb = "Tạm biệt! Chúc bạn một ngày tốt lành!"
        print("rb : " + rb)
        rb_m.say(rb)
        rb_m.runAndWait()
        break
    else:
        rb = "Xin lỗi, tôi không hiểu yêu cầu của bạn."

    print("rb : " + rb)
    rb_m.say(rb)
    rb_m.runAndWait()
