import cv2
import os

def video_to_images(video_path, output_folder, frame_interval=10):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    print(f"Converting every {frame_interval}th frame from the video to images. Total frames: {frame_count}, FPS: {fps}")

    # Read and save every nth frame as an image
    for frame_num in range(0, frame_count, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame as an image
        image_path = os.path.join(output_folder, f"frame_{frame_num:04d}.jpg")
        cv2.imwrite(image_path, frame)

        print(f"Saved frame {frame_num}")

    # Release the video capture object
    cap.release()

    print("Video to images conversion completed.")

# Example usage
video_path = '1.mp4'
output_folder = 'images'

video_to_images(video_path, output_folder, frame_interval=100)
