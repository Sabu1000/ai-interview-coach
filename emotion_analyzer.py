import os
from deepface import DeepFace

def analyze_emotions_in_frames(frames_dir):
    emotion_results = {} # dict to store emotions
    for filename in sorted(os.listdir(frames_dir)): # go through each file in the frames_dir and and try and analyze each face
        if filename.endswith(".jpg"):
            image_path = os.path.join(frames_dir, filename)
            try:
                result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False) # get emotion only
                # store emotion in dict
                dominant_emotion = result[0]['dominant_emotion']
                emotion_results[filename] = dominant_emotion

                print(f"{filename}: {dominant_emotion}")

            except Exception as e:
                print(f"[ERROR] Could not process {filename}: {str(e)}")

    return emotion_results

# Test the function when run as a script
if __name__ == "__main__":
    frames_directory = "frames"  # Change this to your frames directory
    if os.path.exists(frames_directory):
        print(f"Analyzing emotions in frames from: {frames_directory}")
        results = analyze_emotions_in_frames(frames_directory)
        print(f"\nAnalysis complete! Found {len(results)} frames with emotions.")
        print("Results:", results)
    else:
        print(f"Directory '{frames_directory}' not found. Please check the path.")