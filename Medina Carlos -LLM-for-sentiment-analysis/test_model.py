from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="./sentiment-model", tokenizer="./sentiment-model")


id2label = {0: "negative", 1: "positive"}


examples = [
    "What a fantastic movie. I loved it!",
    "This was the worst film I’ve ever seen.",
    "It was okay, not great but not terrible.",
    "Absolutely boring and poorly acted.",
    "Beautiful cinematography and amazing story."
]

print("Label 1: Positive")
print("Label 0: Negative")
print("Score: Nivel de confianza")

for text in examples:
    result = classifier(text)[0]
    label = id2label[int(result["label"].split("_")[-1])]
    print(f"{label.upper()} ({result['score']:.2f}) → {text}")

