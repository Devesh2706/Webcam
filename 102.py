import cv2
import dropbox
import time
import random

start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)

    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")

    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "ZBHMrBImW_kAAAAAAAAAAcRbja2fY0M0F4hx_B66E_3fwgjwUDYO-zjC_MmFL2x3"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()                    

