import cv2
import os

# Define the path to the video file and output directory
video_path = r"C:\Users\sanvi\OneDrive\Desktop\TeleICU\surgery and coma.mp4"
output_folder = r"C:\Users\sanvi\OneDrive\Desktop\TeleICU\frames"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS of the video: {fps}")

# Calculate the interval between frames to achieve 30fps
frame_interval = int(fps / 30)

# Initialize frame count
frame_count = 0
saved_frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Save only every nth frame to match 30fps
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1
    
    frame_count += 1

# Release the video capture object
cap.release()

print(f"Extracted {saved_frame_count} frames and saved them in {output_folder}")
