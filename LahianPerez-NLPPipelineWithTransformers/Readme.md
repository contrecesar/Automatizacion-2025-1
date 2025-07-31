# Simple NLP Pipeline with Transformers Apllicated to Sentiment Analysis 

## Company Scenario: Sentilytics Inc.

**Sentilytics Inc.** is a fictional tech startup that specializes in real-time customer sentiment monitoring. The company uses NLP tools to analyze customer opinions on social media, product reviews, and surveys. This small prototype showcases how such a system could work using state-of-the-art machine learning models.

---

## Project Overview

This Python script demonstrates a basic **sentiment analysis pipeline** using a pre-trained **DistilBERT** model from Hugging Face. It determines whether a given English sentence expresses a **positive** or **negative** sentiment.

---

## Model Used

- **Name**: `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Type**: Transformer-based model
- **Trained on**: Stanford Sentiment Treebank (SST-2)
- **Task**: Binary sentiment classification (`POSITIVE` or `NEGATIVE`)
- **Advantages**: Lightweight, fast inference, good performance for real-time applications

---

## Requirements

Install the necessary libraries before running the script:

```bash
pip install transformers torch
