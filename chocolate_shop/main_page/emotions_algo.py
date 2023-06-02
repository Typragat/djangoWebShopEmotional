from deepface import DeepFace
import cv2
import json
import time

def face_analize(image):
    backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
    demography = DeepFace.analyze(img_path = image, detector_backend = backends[4], actions=['emotion'])
    return demography

def emotion_analize():


    cap= cv2.VideoCapture(0)

    while True:
        time.sleep(2)
        success,img = cap.read()
        print(face_analize(img))
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    emotion_analize()

