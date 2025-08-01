# use_model.py

from transformers import pipeline

def main():
    # --- Load the Pipeline with the Fine-Tuned Model ---
    
    # The user has already replaced 'your-huggingface-username' with their actual username.
    model_name = "ther04/my_awesome_imdb_model"
    
    print(f"Loading the sentiment analysis pipeline with model: {model_name}")
    try:
        sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
    except Exception as e:
        print(f"\nError loading the model. Make sure the name '{model_name}' is correct and the model is public.")
        print(f"Original error: {e}")
        return

    # --- 1. Inference Example (Positive Review) ---

    positive_review = "This movie was a masterpiece! The acting was incredible and the story was deeply moving."
    
    print("\n--- Analyzing positive review ---")
    result_pos = sentiment_pipeline(positive_review)
    print(f"Review: '{positive_review}'")
    print(f"Result: {result_pos}")

    # --- 2. Inference Example (Negative Review) ---

    negative_review = "I was really disappointed. The plot was predictable and the characters were completely flat."

    print("\n--- Analyzing negative review ---")
    result_neg = sentiment_pipeline(negative_review)
    print(f"Review: '{negative_review}'")
    print(f"Result: {result_neg}")
    
    # --- 3. Inference with User's Review (NEW SECTION) ---
    
    print("\n--- Test with your own review ---")
    # We ask the user to write a review.
    user_review = input("Write a review in English and press Enter: ")

    # We make sure the user wrote something before analyzing.
    if user_review.strip():
        result_user = sentiment_pipeline(user_review)
        print("\n--- Analyzing your review ---")
        print(f"Your review: '{user_review}'")
        print(f"Analysis result: {result_user}")
    else:
        print("No review was entered to analyze.")


if __name__ == "__main__":
    main()