import cv2
class Detector:
    def __init__(self, frame_queue, detection_queue):
        self.frame_queue = frame_queue
        self.detection_queue = detection_queue
        self.first_frame = None
    
    def run(self):       
        try:
            while True:
                frame = self.frame_queue.get()
                if frame is None:
                    self.detection_queue.put(None)
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)

                if self.first_frame is None:
                    self.first_frame = gray
                    continue

                frame_delta = cv2.absdiff(self.first_frame, gray)
                thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=2)
                contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                detections = [cv2.boundingRect(contour) for contour in contours if cv2.contourArea(contour) > 500]
                self.detection_queue.put((frame, detections))
        except Exception as e:
            print(f"[Detector Error]: {e}")
            self.detection_queue.put(None)