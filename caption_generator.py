from transformers import pipeline

def generate_caption(mood, surroundings="car interior"):
    """
    Generates a caption for Instagram using mood + surroundings.
    Returns:
        caption (str)
    """
    try:
        generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
        prompt = f"Generate a creative Instagram caption based on mood '{mood}' and surroundings '{surroundings}'."
        caption = generator(prompt, max_length=50, do_sample=True)[0]["generated_text"]
        print(f"Caption generated: {caption}")
        return caption
    except Exception as e:
        print("Caption generation error:", e)
        return f"My mood today is {mood}."
