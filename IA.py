#Versión 3.12 de python
import cv2 #Acceder a la webcam del pc, pues se necesita hacer reconocimiento de imagen
from cvzone.HandTrackingModule import HandDetector #Rastrea el movimiento de las manos

webcam= cv2.VideoCapture(0) #El 0 indica la cámara propia del pc
rastreador= HandDetector(detectionCon=0.8, maxHands=4)

while True:
    exito, imagen= webcam.read() #Devuelve dos valores, por lo que asignamos 2 variables
    coordenadas, imagenManos = rastreador.findHands(imagen)


    print(coordenadas)

    cv2.imshow("Proyecto4-IA", imagen) #permite poner título y recibe imagen que capturamos
    
    #Espera cada milisegundo que presione una tecla
    if cv2.waitKey(1) != -1:
        break


webcam.release() #Libera imagen capturada

cv2.destroyAllWindows() #Libera la cámara