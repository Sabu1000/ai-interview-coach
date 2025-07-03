import cv2
import os

def extract_frames(video_path, output_dir, interval_seconds=1):
    # open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return
    
   
    fps = cap.get(cv2.CAP_PROP_FPS) # determines how many fps the video is in
    frame_interval = int(fps * interval_seconds) # if fps is 30 and interval is 1, a frame is captured every second
    frame_count = 0
    saved_count = 0

    # create output directory where frames are saved
    os.makedirs(output_dir, exist_ok=True)

    while True:
        ret, frame = cap.read() # ret tells if there are any more frames in video and frame is the image data
        if not ret: # if no more frames, break
            break
    
        if frame_count % frame_interval == 0: # check if current frame should be saved (saves one frame per second)
            frame_filename = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
        frame_count += 1 # always increase frame counter
 
    cap.release() # close file
    print(f"Saved {saved_count} frames to '{output_dir}'.")
