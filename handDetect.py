import cv2 
import mediapipe as mp
import time

video=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hand=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
ptime=0
while True:
    _,img=video.read()
    imgRBG=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hand.process(imgRBG)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                if id==4 or id==8 or id==12 or id==16 or id==20:
                    cv2.circle(img,(cx,cy),10,(123,33,8),cv2.FILLED)
            mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
    '''
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    f=f"Current FPS: {int(fps)}"
    print(f)
    cv2.putText(img,f,(8,70),cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(200,155,100),thickness=2)
   '''

    cv2.imshow("IMG",img)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break


