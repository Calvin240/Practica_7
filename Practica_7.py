import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    kernel = np.ones((7,7),np.uint8)
    if ret == True:
            cv2.imshow('frame',frame)
            erosion = cv2.erode(frame,kernel,iterations = 1)
            cv2.imshow('Erosion',erosion)
            dilatacion = cv2.dilate(frame,kernel,iterations = 1)
            cv2.imshow('Dilatacion',dilatacion)
            apertura = cv2.morphologyEx(frame,cv2.MORPH_OPEN,kernel)
            cv2.imshow('Apertura',apertura)
            cierre = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,kernel)
            cv2.imshow('Cierre',cierre)
            gradiente = cv2.morphologyEx(frame,cv2.MORPH_GRADIENT,kernel)
            cv2.imshow('Gradiente',gradiente)
            if cv2.waitKey(1) & 0xFF == ord('k'):
                break
cap.release()
cv2.destroyAllWindows()
