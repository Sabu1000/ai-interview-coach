import nltk 
from textblob import TextBlob

FILTER_WORDS = {"um", "uh", "like", "you know", "so", "basically", "actually", "right", "I mean"}

def analyze_transcript(text):
    print("Starting NLP analysis...")

    # this gets every word from text and puts inside of dict
    words = nltk.word_tokenize(text.lower())
    
    filter_counts = {}
    for word in FILTER_WORDS: # for every word in filter words check if the word is in transcriped check, if so add to dict and increase the count by one
        if word in words:
            filter_counts[word] = words.count(word)

    blob = TextBlob(text) # create a textblob object
    sentiment = blob.sentiment # analyze the emotional tone of the text (from -1 (most negative tone) to 1 (most positive tone))
    

    print("Filter words used")
    for word, count in filter_counts.items():
        print(f" - '{word}': {count} times")
    
    print("\nSentiment Analysis:")
    print(f" - Polarity (emotion): {sentiment.polarity:.2f} (−1=negative, +1=positive)")
    print(f" - Subjectivity (opinion): {sentiment.subjectivity:.2f} (0=objective, 1=subjective)")

    return {
        "filter_counts": filter_counts,
        "sentiment": {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }

    }


