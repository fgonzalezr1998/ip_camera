import threading
import time
import cv2

class CameraServer(threading.Thread):
    def __init__(self, name="CameraServer"):
        self.__is_active = False
        self.__camera = None
        self.__failure = True
        self.__last_frame = None
        threading.Thread.__init__(self, name=name)
        threading.Thread.start(self)
    
    def __del__(self):
        self.__camera.release()
        cv2.destroyAllWindows()

    def run(self):
        self.__camera = cv2.VideoCapture(0)
        while (True):
            if (not self.__is_active):
                cv2.destroyAllWindows()
                continue

            ret, frame = self.__camera.read()
            if not ret:
                self.__failure = True
                print("[ERROR] Error capturing frame!")
                self.stop()
                break
            else:
                self.__failure = False

            self.__last_frame = frame

        self.__camera.release()

    def start(self):
        print("Running Camera...")
        self.__is_active = True
        # Wait if failure
        t0 = time.time()
        while ((time.time() - t0 < 2) and self.__failure):
            pass

        # Return true if not failure, and false if failure
        return not self.__failure

    def stop(self):
        self.__is_active = False

    def getFrame(self):
        return self.__last_frame