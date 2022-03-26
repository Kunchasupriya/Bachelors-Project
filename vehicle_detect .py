import cv2
import serial
ser=serial.Serial('COM8',9600);
print(ser)
car_cascade = cv2.CascadeClassifier('vehicles.xml')
cap = cv2.VideoCapture('video3.mp4')

while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    if(type(img)==type(None)):
        break
    
    cars= car_cascade.detectMultiScale(gray, 1.1, 1)
    print(cars)
    

    for (x,y,w,h) in cars:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    ser.write('Y')
    

    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break
    
cv2.NamedWindow('video')
cv2.imshow('video', img)
cv2.destroyAllWindows()

if cars>0:

        ser = serial.Serial('COM8', 9600)
        print(ser)
        ser.write('N')
else:

        ser = serial.Serial('COM8', 9600)
        print(ser)
        ser.write('Y')
        