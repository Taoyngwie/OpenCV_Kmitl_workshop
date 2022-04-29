import cv2

#imread คำสั่งในการอ่านภาพ
#ใส่ r เพื่อบอกคอมว่า \ คือเครื่องหมาย /
img = cv2.imread(r"D:\Destop\kmitl_opencv\kmutt.jpg") #ชื่อภาพว่า kmutt โดยท่ขนาดภาพตามจริง
img_resize = cv2.resize(img,(500,200)) #นำภาพมา resize โดยที่มีการปรับขนาดภาพใหม่
cv2.rectangle(img,(0,0),(100,100),(255,0,0),5)#image,จุดมุมบนซ้าย,จุดมุมล่างขวา,สี rgb,ความหนา
cv2.rectangle(img,(100,100),(200,200),(255,0,255),-1) #ใส่ -1 เพื่อให้สีภาพมันเต็ม

cv2.imwrite("D:\Destop\kmitl_opencv\kmutt2.jpg",img) #การเซฟภาพ โดยที่จะเปลี่ยนชื่อใหม่ใส่ลงไป
print(img) #เเสดงค่า matrix ของรูปภาพ
cv2.imshow("kmutt",img) #ใช้ในการเปิดภาพ โดยที่ใส่ค่า parameter เป็นชื่อของภาพลงไป
cv2.waitKey() #หน่วงข้อมูลรอจาก keyboard โดยนับถอยหลังปิดภาพ


