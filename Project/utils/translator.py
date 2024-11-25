from googletrans import Translator

def translate_text(text, dest_language="ko"):
    translator = Translator()
    result = translator.translate(text, dest=dest_language)
    return result.text
