import cv2
import numpy as np
import qrcode
from pyzbar.pyzbar import decode
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT
from PyQt5 import QtGui
from playsound import playsound



def scan (self):
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    with open('myDataFile.text') as f:
        myDataList = f.read().splitlines()

    while True:

        success, img = cap.read()
        a=len(decode(img))
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            myColor = (0, 255, 0)
            
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,myColor,1)
            pts2 = barcode.rect
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_TRIPLEX,
                        0.9,myColor,2)
            print (myData)
            break

        if a>0:
            break



        cv2.imshow('Scan QR Code',img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()

    _user32 = ctypes.WinDLL('user32', use_last_error=True)
    _MessageBoxW = _user32.MessageBoxW
    def MessageBoxW(hwnd, text, caption, utype):
        playsound("sound_effects/done.mp3")
        result = _MessageBoxW(hwnd, text, caption, utype)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        if result==10:
            scan(self)

        elif result==11:
            print(myData)
            self.worker_id_2.setText(myData)
            qr = qrcode.make(myData)

            qr.save("current_e/photo.png")


            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("current_e/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.bar_code.setIcon(icon18)

    MessageBoxW(None, "You have scanned ( {} )".format(myData), "caption", 6)

    #def Mbox(title, text, style):
    #    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    #Mbox('Scanning Done', 'you have scanned ( {} )'.format(myData), 6)

    

