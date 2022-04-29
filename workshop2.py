import cv2
cap=cv2.VideoCapture(0) #ตัวเลขคือค่าของการเลือกกล้องว่าจะใช้ตัวไหน 0=กล้องภายในคอม,1=กล้องจากภายนอก

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter(r"D:\Destop\kmitl_opencv\output.avi",fourcc,20.0,(640,480))
while (True):
    check , frame = cap.read() #อ่านค่าจากกล้องเอาไว้ใน Frame,check
    result.write(frame)
    cv2.imshow("output title",frame) #ภาพเคลื่อนไหว
    if cv2.waitKey(1) & 0xFF == ord("q"): #กด q เพื่อหยุดโปรเเกรม
        break
cap.release() #เมื่อปิดการทำงานคืนค่าทรัพยากรให้กับเครื่องเพื่อประหยัด mem
cv2.destroyAllWindows() #ต่อจากกด q เพื่อปิดการทำงานของโปรเเกรม