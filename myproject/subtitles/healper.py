from googletrans import Translator

def translate_subtitles(subtitles):
    translator = Translator()
    for sub in subtitles:
        translated_text = translator.translate(sub.text, src='zh-cn', dest='en')
        sub.text = translated_text.text
    return subtitles
