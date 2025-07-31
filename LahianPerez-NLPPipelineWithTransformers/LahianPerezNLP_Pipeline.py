# Import the pipeline function from Hugging Face's transformers library
from transformers import pipeline

# Create a sentiment-analysis pipeline using the DistilBERT model fine-tuned on SST-2 dataset
sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Analyze the sentiment of the first input text
result1 = sentiment_pipeline("I hate this movie! It was terrorific")

# Analyze the sentiment of the second input text
result2 = sentiment_pipeline("it was ok, I mean isn't fantastic")

# Analyze the sentiment of the third input text
result3 = sentiment_pipeline("Was a fantastic expiercence")

# Print the sentiment results for each input text
print("Result1:", result1)
print("Result2:", result2)
print("Result3:", result3)
