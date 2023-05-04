import PokerHandFunction
from ultralytics import YOLO
import cv2
import cvzone
import math

# video
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
# model
model = YOLO('playingCards.pt')

class_names = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']

while True:
    hand = []


    success , img = cap.read()
    results = model(img,stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            w,h = x2-x1,y2-y1

            conf = math.ceil((box.conf[0])*100)/100

            classes = int(box.cls[0])
            currentClass = class_names[classes]

            cvzone.cornerRect(img,(x1,y1,w,h),l=10,t=1,rt=1,)
            cvzone.putTextRect(img,f"{currentClass}",(max(0,x1),max(40,y1)),scale=1,thickness=1)

            if conf>0.5:
                hand.append(currentClass)

    hand = list(set(hand))
    if len(hand) == 5:
        results , hand_dict = PokerHandFunction.findPokerHand(hand)

        for key,value in hand_dict.items():
            if value == results:
                score = key
        cvzone.putTextRect(img, f'Your Hand: {results} | Your Score: {score}', (20, 75), scale=2, thickness=2)


    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
