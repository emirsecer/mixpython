def çeviri ():
    from googletrans import Translator

    # Çevrilecek metni kullanıcıdan alın
    text = input ("Çevirmek istediğiniz metni girin: ")

    # Kaynak ve hedef dilleri kullanıcıdan alın
    src_lang = input ("Kaynak dil: ")
    dest_lang = input ("Hedef dil: ")

    # Google Translate API'sine bağlanın
    translator = Translator ()

    # Metni çevirin
    result = translator.translate (text, src=src_lang, dest=dest_lang)

    # Çeviri sonuçlarını kullanıcıya gösterin
    print (f"{result.origin} ({src_lang}) -> {result.text} ({dest_lang})")

