import cv2
import mediapipe as mp
import time
import handdetectModule
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector=handdetectModule.handDetector(detectionCon=0.5)
pTime=0

fingertips=[4,8,12,16,20]


while True:
    success,img1=cap.read()
    
    img=detector.findHands(img1)
    lmlist=detector.findPosition(img)
    if(lmlist):
        if len(lmlist)>=9:
          fingers=[]

          if lmlist[fingertips[0]][1]>lmlist[fingertips[0]-1][1]:
                fingers.append(1)
          else:
              fingers.append(0)
          for id in range(1,5):
             if lmlist[fingertips[id]][2]<lmlist[fingertips[id]-2][2]:
                 fingers.append(1)
             else:
              fingers.append(0)
          

          cv2.rectangle(img,(10,40),(225,100),(10,2,0),thickness=4)
          print(fingers)
          if fingers==[0,0,1,0,0]:
              cv2.putText(img1,"HEHE😳",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[1,0,0,0,0]:
              cv2.putText(img1,"OK GO",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[0,0,0,0,0]:
              cv2.putText(img1,"HOLD ON",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[0,1,0,0,0]:
              cv2.putText(img1,"ONE",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[0,1,1,0,0]:
              cv2.putText(img1,"TWO",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[0,1,1,1,0]:
              cv2.putText(img1,"THREE",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[0,1,1,1,1]:
              cv2.putText(img1,"FOUR",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[1,1,0,0,1]:
              cv2.putText(img1,"ROCK ON",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
          elif fingers==[1,1,1,1,1]:
              cv2.putText(img1,"STOP",(40,80),cv2.FONT_HERSHEY_PLAIN,2,(12,12,255),3)
              
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'Current Fps: {int(fps)}',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    
    cv2.imshow("SIGN DETECTOR",img)
    if cv2.waitKey(1)==ord('x'):
        break

 

















