import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(r"D:\Destop\kmitl_opencv\facedetection\haarcascade_frontalface_default.xml")

while (True):
    check,frame=cap.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #เเปลงภาพจาก bgr ไปเป็น Gray scale
    face_detect=face_cascade.detectMultiScale(gray_img,1.1,5)
    for (x,y,w,h) in face_detect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5) #เมื่อdetec ใบหน้าจะวาดรูปสี่เหลี่ยม
        cv2.imshow("detec face camera",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
