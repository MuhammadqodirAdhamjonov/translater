from googletrans import Translator

translator = Translator()


def my_translator(text, dest, src):
    tarjima = translator.translate(text, dest=dest, src=src)
    return tarjima.text
