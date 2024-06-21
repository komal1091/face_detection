import cv2
from mtcnn import MTCNN

cap = cv2.VideoCapture("d:\\language vedio\\Do You Feel Like a Typical Czech_ _ Easy Czech 1.mp4")

detector = MTCNN()

while True:
    ret, frame = cap.read()

    output = detector.detect_faces(frame)
    for i in output:
        x,y,width,height = i["box"]
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+width,y+height),color=(0,255,0),thickness=2)
    cv2.imshow("window", frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cv2.destroyAllWindows()



