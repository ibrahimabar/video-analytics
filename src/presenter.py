from datetime import datetime
import cv2
import time

class Presenter:
    def __init__(self, detection_queue, enable_blur, auto_shutdown):
        self.detection_queue = detection_queue
        self.enable_blur = enable_blur
        self.auto_shutdown = auto_shutdown
    
    def run(self):
        try:
            while True:
                data = self.detection_queue.get()
                if data is None:
                    break
                
                frame, detections = data
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                for (x, y, w, h) in detections:
                    if self.enable_blur:
                        roi = frame[y:y + h, x:x + w]
                        blurred = cv2.GaussianBlur(roi, (51, 51), 0)
                        frame[y:y + h, x:x + w] = blurred
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                cv2.imshow("Video Analytics", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()

            if self.auto_shutdown:
                exit()
            else:
                while True:
                    time.sleep(1)  # Keep presenter running if auto_shutdown is False

        except Exception as e:
            print(f"[Presenter Error]: {e}")
        