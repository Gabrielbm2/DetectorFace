import cv2 #opencv
import mediapipe as mp


# inicializa o opencv e o mediapipe
webcan = cv2.VideoCapture(0)
solucao_captura_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_captura_rosto.FaceDetection()
desenho_contorno = mp.solutions.drawing_utils

while True:
    #le as informações da webcan
    verificador, frame = webcan.read()
    if not verificador:
        break
    #reconhece os rostos
    lista_rostos = reconhecedor_rostos.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #contorna os rostos com o desenho
            desenho_contorno.draw_detection(frame, rosto)
            
    cv2.imshow("Rostos webcan", frame)
    
    #quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27:
        break
    
webcan.release()