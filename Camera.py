import cv2

def takesnapshot():
    videocaptureobject = cv2.VideoCapture(0)
    Result = True
    while (Result):
        ret,frame = videocaptureobject.read()

        cv2.imwrite("pick1.jpg",frame)
        Result = False

    videocaptureobject.release()
    cv2.destroyAllWindows()    

takesnapshot()
