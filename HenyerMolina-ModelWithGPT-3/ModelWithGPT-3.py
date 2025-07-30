import openai
import os

# --- Initial Configuration ---
# Paste your new OpenAI API key here.
# Remember to keep this key private and don't share it!
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

def improve_professional_text(draft: str) -> str:
    """
    Uses an OpenAI model to improve a text draft.
    Args:
        draft: The original text that needs to be improved.
    Returns:
        The AI-improved text or an error message.
    """
    # This is the "prompt" or instruction we give to the model.
    # It's crucial to be clear and specific about what we want.
    system_prompt = """
    You are an expert writing assistant. Your task is to take the user's text,
    which is a draft, and rewrite it to be more professional, clear and concise.
    Correct grammatical errors, improve sentence structure and ensure the tone
    is appropriate for a business environment. Don't add new information, just improve the existing text.
    Return only the improved text.
    """
    
    try:
        # Make the call to the OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # One of the most capable and cost-effective models
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": draft}
            ],
            temperature=0.5,  # Low value to get more predictable responses
            max_tokens=500    # Length limit for the response
        )
        
        # Extract the content from the response
        improved_text = response.choices[0].message.content.strip()
        return improved_text
        
    except openai.APIError as e:
        # Handle API errors
        return f"An error occurred with the OpenAI API: {e}"
    except Exception as e:
        # Handle other possible errors
        return f"An unexpected error occurred: {e}"

# --- Usage Example ---
if __name__ == "__main__":
    original_text = """
    Well, I wanted to say that the sales report for this month is ready.
    I reviewed it and it seems things are going well, we went up 10%.
    I think it's because of the new marketing campaign we did.
    I'm sending it to you so you can take a look.
    """
    
    print("--- Original Text ---")
    print(original_text)
    print("\n" + "="*30 + "\n")
    
    print("--- Requesting improvement from AI... ---")
    final_text = improve_professional_text(original_text)
    
    print("\n--- AI-Improved Text ---")
    print(final_text)