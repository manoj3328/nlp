import nltk
from googletrans import Translator

nltk.download('punkt_tab')

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    return " ".join(tokens)

def translate_text(text, target_language):
    translator = Translator()
    
    translation = translator.translate(text, dest=target_language)
    return translation.text

english_text = "who are you?"
processed_text = preprocess_text(english_text)
languages = ['es', 'fr', 'de','te','hi']

for lang in languages:
    translated_text = translate_text(processed_text, lang)
    print(f"Translated to {lang}: {translated_text}")
