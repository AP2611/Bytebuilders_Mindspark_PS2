from deepface import DeepFace
from textblob import TextBlob

def analyze_face_mood(frame):
    """
    Uses DeepFace to detect emotion from a video frame.
    Returns:
        mood (str)
    """
    try:
        analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
        mood = analysis["dominant_emotion"]
        print(f"Detected face mood: {mood}")
        return mood
    except Exception as e:
        print("Face mood detection error:", e)
        return "neutral"

def analyze_audio_mood(text):
    """
    Analyzes text sentiment to detect mood.
    Returns:
        mood (str)
    """
    try:
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0.1:
            return "happy"
        elif sentiment < -0.1:
            return "sad"
        else:
            return "neutral"
    except Exception as e:
        print("Audio mood detection error:", e)
        return "neutral"

def combine_moods(face_mood, audio_mood):
    """
    Combines face and audio moods.
    Returns:
        final_mood (str)
    """
    if face_mood != "neutral":
        return face_mood
    return audio_mood
