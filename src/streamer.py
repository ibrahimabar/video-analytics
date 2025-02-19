import cv2, time

class Streamer:
    def __init__(self, video_path, frame_queue):
        self.video_path = video_path
        self.frame_queue = frame_queue
    
    def run(self):
        try:
            cap = cv2.VideoCapture(self.video_path)
            if not cap.isOpened():
                raise ValueError(f"Error: Unable to open video file {self.video_path}")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                self.frame_queue.put(frame)
                time.sleep(1 / 30)  # Approximate video FPS control
            cap.release()
            self.frame_queue.put(None)  # Signal end of video
        except Exception as e:
            print(f"[Streamer Error]: {e}")
            self.frame_queue.put(None)