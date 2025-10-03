import cv2
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr
import time

def brighten_frame(frame, value=50):
    """
    Brighten the image by increasing the V (value) channel in HSV color space.
    :param frame: input BGR frame
    :param value: brightness increment (0–255)
    :return: brightened frame
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v = cv2.add(v, value)  # Increase brightness
    v = np.clip(v, 0, 255)

    final_hsv = cv2.merge((h, s, v))
    bright_frame = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bright_frame

def capture_video_frame():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)  # Use macOS backend

    if not cap.isOpened():
        print("Error: Cannot open camera")
        return None

    # Warm up camera
    print("Warming up camera...")
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)
    cap.set(cv2.CAP_PROP_AUTO_WB, 1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    for _ in range(30):  # Discard first frames
        ret, frame = cap.read()
        time.sleep(0.05)

    print("Capturing video frame...")
    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        print("Error: Failed to capture frame")
        return None

    bright_frame = brighten_frame(frame, value=50)  # Brighten
    return bright_frame

def capture_audio(duration=5):
    recognizer = sr.Recognizer()
    fs = 44100

    print(f"Recording audio for {duration} seconds...")
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
    except Exception as e:
        print("Microphone error:", e)
        return ""

    try:
        wavio.write("audio.wav", recording, fs, sampwidth=2)
    except Exception as e:
        print("Error writing audio file:", e)
        return ""

    try:
        with sr.AudioFile("audio.wav") as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print(f"Audio captured: {text}")
        return text
    except Exception as e:
        print("Audio recognition error:", e)
        return ""

if __name__ == "__main__":
    # Capture video
    frame = capture_video_frame()
    if frame is not None:
        cv2.imshow("Captured Frame", frame)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")

    # Capture audio
    audio_text = capture_audio(duration=5)
    print(f"Captured audio text: {audio_text}")
