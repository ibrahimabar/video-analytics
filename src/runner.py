import multiprocessing as mp
import argparse
from streamer import Streamer
from presenter import Presenter
from detector import Detector

def main(video_path, enable_blur, auto_shutdown):
    try:
        frame_queue = mp.Queue()
        detection_queue = mp.Queue()

        streamer = Streamer(video_path, frame_queue)
        detector = Detector(frame_queue, detection_queue)
        presenter = Presenter(detection_queue, enable_blur, auto_shutdown)

        p1 = mp.Process(target=streamer.run)
        p2 = mp.Process(target=detector.run)
        p3 = mp.Process(target=presenter.run)

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        if auto_shutdown:
            p3.terminate()  # Ensure Presenter stops if auto_shutdown is enabled
    
    
    except Exception as e:
        print(f"[Main Process Error]: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Real-Time Video Analytics System")
    parser.add_argument("--video", type=str, required=True, help="Path to input video")
    parser.add_argument("--enable_blur", action="store_true", help="Enable blurring of detected motion areas")
    parser.add_argument("--auto_shutdown", action="store_true", help="Automatically shut down when the video ends")
    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_arguments()
    main(args.video, args.enable_blur, args.auto_shutdown)
