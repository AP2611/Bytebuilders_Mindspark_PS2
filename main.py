from data_capture import capture_face_frame, capture_audio
from mood_analysis import analyze_face_mood, analyze_audio_mood, combine_moods
from caption_generation import generate_caption
from interaction import user_approval, post_to_instagram

if __name__ == "__main__":
    # Step 1 — Capture data
    frame = capture_face_frame()
    audio_text = capture_audio()

    # Step 2 — Analyze mood
    face_mood = analyze_face_mood(frame)
    audio_mood = analyze_audio_mood(audio_text)
    final_mood = combine_moods(face_mood, audio_mood)
    print(f"Final Mood: {final_mood}")

    # Step 3 — Generate caption
    surroundings = "car interior"
    caption = generate_caption(final_mood, surroundings)

    # Step 4 — Approval & Posting
    if user_approval(caption):
        image_path = input("Enter the path to the image to post: ")
        post_to_instagram(image_path, caption)
    else:
        print("Post cancelled.")
