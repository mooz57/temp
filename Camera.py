print("test")
import cv2
import threading

class CamThread(threading.Thread):
    def __init__(self, name, id):
        threading.Thread.__init__(self)
        self.name = name
        self.id = id
        self.fps = 10
    def setFps(self, newFps):
        self.fps = newFps
    def run(self):
        print(f"Starting camera : {self.name}")
        self.preview()
    def preview(self):
        ms = 1000 // self.fps
        cam = cv2.VideoCapture(self.id)
        if not cam.isOpened() or cam is None:
            print("Video has ended or failed")
            return None
        status, frame = cam.read()
        counter = 1
        while status:
            print(f"{self.name} : {counter}")
            cv2.imshow(f'Camera : {self.name}', frame)
            status, frame = cam.read()
            key = cv2.waitKey(ms)
            if key == 27:
                break; #esc
            counter += 1   
        cv2.destroyAllWindows()

cam = []
cam.append(CamThread("Webcam", 0))
cam.append(CamThread("Droid Cam", 1))
cam[0].setFps(100)
# cam[0].start()
cam[1].start()