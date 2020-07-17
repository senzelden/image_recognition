"""extracts frames from video"""
import cv2


IN_PATH = "input"
OUT_PATH = "frames/frame"


def get_frames(input, output):
    """extract frames from input video"""
    vidcap = cv2.VideoCapture(f"{input}.mp4")
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"{output}{count}.jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1


if __name__ == "__main__":
    get_frames(IN_PATH, OUT_PATH)
