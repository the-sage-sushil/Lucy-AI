import cv2
import time
import numpy as np
import handtracking as htm
import math
import pyautogui as pygui
import pyttsx3
import datetime
import speech_recognition as sr

#################################################
wcam, hCam = pygui.position()
Swidth, Shight = pygui.size()
CurrentX, CurrentY = pygui.position()

#################################################

cap = cv2.VideoCapture(0)
cap.set(3, Swidth)
cap.set(4, Shight)

pTime = 0

detector = htm.handDetector(detectionCon=0.7)

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volumeRangr = volume.GetVolumeRange()
pygui.FAILSAFE = False

minVol = volumeRangr[0]
maxVol = volumeRangr[1]


class handgrsture:
        while True:

            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            if len(lmList) != 0:

                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.circle(img, (cx, cy), 8, (255, 0, 0), cv2.FILLED)

                length = math.hypot(x2 - x1, y2 - y1)
                print(length)

                # hand range 30 -  180
                # volume Range -20 -0

                pygui.moveTo((x1 + x2), (y1 + y2))

                if length < 30:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                    pygui.click()

                    print(x1 + x2, y1 + y2)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.imshow("Img", img)
            cv2.waitKey(1)
