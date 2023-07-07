import cv2 as cv
import queue

# Create a queue
image_queue = queue.Queue()

# Create a video capture object
vid_capture = cv.VideoCapture(r'C:\Users\vinoo\OneDrive\Documents\Video\test_video.mp4')

# Check if the video opened successfully
if not vid_capture.isOpened():
    print("Video opening is unsuccessful")
    exit()

# Frame rate info
fps = int(vid_capture.get(cv.CAP_PROP_FPS))
print("Frame Rate: ", fps, "frames per second")

# Frame count info
frame_count = int(vid_capture.get(cv.CAP_PROP_FRAME_COUNT))
print("Frame Count: ", frame_count)

# Determine the desired window size
window_width = 1024
window_height = 720

# Set the window size
cv.namedWindow('Video', cv.WINDOW_NORMAL)
cv.resizeWindow('Video', window_width, window_height)

# Read each frame from the file
while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret:
        # Resize the frame to fit the window size (optional)
        frame = cv.resize(frame, (window_width, window_height))
        cv.imshow('Video', frame)
        k = cv.waitKey(30)
        if k == ord('q'):  # Check for 'q' key press
            break

        # Add the frame to the image queue
        image_queue.put(frame)
        print("Queue length:", image_queue.qsize())
    else:
        break

# Release the objects
vid_capture.release()
cv.destroyAllWindows()
