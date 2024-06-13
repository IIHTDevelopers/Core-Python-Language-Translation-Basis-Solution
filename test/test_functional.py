import unittest
from python_lang import *
from TestUtils import TestUtils  # Assuming you have a TestUtils class for Yaksha
import warnings


class TestFunctions(unittest.TestCase):

    def test_count_words(self):
        test_utils_instance = TestUtils()
        sentence = "Hello im out of this world."
        expected_word_count = 6
        actual_word_count = count_words(sentence)
        test_utils_instance.yakshaAssert("TestCountWords", expected_word_count == actual_word_count, "functional")
        if expected_word_count == actual_word_count:
            print("TestCountWords = Passed")
        else:
            print("TestCountWords = Failed")

    def test_capitalize_sentence(self):
        test_utils_instance = TestUtils()
        given_sentence = "this are the words you need"
        expected_capitalized_sentence = "This are the words you need"
        actual_capitalized_sentence = capitalize_sentence(given_sentence)
        test_utils_instance.yakshaAssert("TestCapitalizeSentence", expected_capitalized_sentence == actual_capitalized_sentence, "functional")
        if expected_capitalized_sentence == actual_capitalized_sentence:
            print("TestCapitalizeSentence = Passed")
        else:
            print("TestCapitalizeSentence = Failed")

    def test_count_e_occurrences(self):
        test_utils_instance = TestUtils()
        input_sentence = "If we have the need specify the from-language and the to-language"
        expected_e_count = 10
        actual_e_count = count_e_occurrences(input_sentence)
        test_utils_instance.yakshaAssert("TestCountEOccurrences", expected_e_count == actual_e_count, "functional")
        if expected_e_count == actual_e_count:
            print("TestCountEOccurrences = Passed")
        else:
            print("TestCountEOccurrences = Failed")

    def test_count_vowels(self):
        test_utils_instance = TestUtils()
        example_string = "Hello, World! This is an example string."
        expected_count = 10
        actual_count = count_vowels(example_string)
        test_utils_instance.yakshaAssert("TestCountVowels", expected_count == actual_count, "functional")
        if expected_count == actual_count:
            print("TestCountVowels = Passed")
        else:
            print("TestCountVowels = Failed")


    def test_translate_to_german(self):
        test_utils_instance = TestUtils()
        translated_text = translate_to_german("Good Morning!")
        expected_translation = "Guten Morgen!"
        test_utils_instance.yakshaAssert("TestTranslateToGerman", expected_translation == translated_text, "functional")
        if expected_translation == translated_text:
            print("TestTranslateToGerman = Passed")
        else:
            print("TestTranslateToGerman = Failed")

    def test_translate_text(self):
        test_utils_instance = TestUtils()
        source_text = "Guten Morgen"
        expected_translation = "Buenos días"
        actual_translation = translate_text(source_text, "german", "spanish")
        test_utils_instance.yakshaAssert("TestTranslateText", expected_translation == actual_translation, "functional")
        if expected_translation == actual_translation:
            print("TestTranslateText = Passed")
        else:
            print("TestTranslateText = Failed")

    def test_correct_words(self):
        test_utils_instance = TestUtils()
        words = ["Data Scence", "Mahine Learnin"]
        expected_corrected_words = ["Data Science", "Machine Learning"]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            actual_corrected_words = correct_words(words)
        test_utils_instance.yakshaAssert("TestCorrectWords", expected_corrected_words == actual_corrected_words, "functional")
        if expected_corrected_words == actual_corrected_words:
            print("TestCorrectWords = Passed")
        else:
            print("TestCorrectWords = Failed")

    def test_analyze_sentiment(self):
        test_utils_instance = TestUtils()
        text = "I love this library! It's so easy to use and powerful."
        expected_sentiment = "Positive"
        actual_sentiment = analyze_sentiment(text)
        test_utils_instance.yakshaAssert("TestAnalyzeSentiment", expected_sentiment == actual_sentiment, "functional")
        if expected_sentiment == actual_sentiment:
            print("TestAnalyzeSentiment = Passed")
        else:
            print("TestAnalyzeSentiment = Failed")

if __name__ == '__main__':
    unittest.main()
