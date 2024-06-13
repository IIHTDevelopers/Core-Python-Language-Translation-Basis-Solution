import textblob
import translate
from translate import Translator
def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Return the number of words
    return len(words)

# Test the function
sentence = "Hello im out of this world."
print("Number of words:", count_words(sentence))

def capitalize_sentence(sentence):
    return sentence.capitalize()

given_sentence = "this are the words you need"
capitalized_sentence = capitalize_sentence(given_sentence)
print("Capitalized Sentence:", capitalized_sentence)
def count_e_occurrences(sentence):
    count = 0
    for char in sentence:
        if char.lower() == 'e':
            count += 1
    return count

# Example usage:
input_sentence = "If we have the need specify the from-language and the to-language"
e_count = count_e_occurrences(input_sentence)
print("Number of 'e' occurrences:", e_count)


def count_vowels(string):
    # Define a list of vowels
    vowels = "aeiouAEIOU"

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the vowel count
            vowel_count += 1

    # Return the total count of vowels
    return vowel_count


# Example input
example_string = "Hello, World! This is an example string."

# Output the number of vowels in the example string
print("Number of vowels in the string:", count_vowels(example_string))


def translate_to_german(text):
    translator = Translator(to_lang="German")
    translation = translator.translate(text)
    return translation

# Example usage:
translated_text = translate_to_german("Good Morning!")
print("Translation:", translated_text)

from translate import Translator

def translate_text(source_text, from_lang, to_lang):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(source_text)
    return translation

# Example usage:
def translate_german_to_spanish(source_text):
    return translate_text(source_text, "german", "spanish")

source_text = "Guten Morgen"
translation = translate_german_to_spanish(source_text)
print("Translation:", translation)

from textblob import TextBlob


def correct_words(words):
    corrected_words = []
    for word in words:
        corrected_words.append(TextBlob(word).correct())
    return corrected_words
if __name__ == "__main__":
    words = ["Data Scence", "Mahine Learnin"]
    corrected_words = correct_words(words)
    print("Wrong words:", words)
    print("Corrected Words are:")
    for word in corrected_words:
        print(word, end=" ")


import textblob

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text string.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The sentiment classification ('Positive', 'Neutral', or 'Negative').
    """

    blob = textblob.TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Execute the function and print the result (ensure this block is executed)
text = "I love this library! It's so easy to use and powerful."
sentiment = analyze_sentiment(text)
print("Sentiment:", sentiment)
