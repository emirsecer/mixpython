import os
import urllib.request
from googlesearch import search
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# Arama yapılacak kelime
kelime = "matematik 2 " 

# İndirilecek dosyaların hedef dizini
hedef_dizin = r"C:\Users\EMİR\Desktop\dersle ve yazılımla alakalı\ders notları\fizik2_withbot"

# Google'da arama yap
url_listesi = list(search(kelime ))

# PDF dosyalarını indir
for url in url_listesi:
    try:
        if url.endswith(".pdf"):
            dosya_adi = url.split("/")[-1]
            dosya_yolu = os.path.join(hedef_dizin, dosya_adi)
            urllib.request.urlretrieve(url, dosya_yolu)
            # PDF dosyasını aç
            with open(dosya_yolu, 'rb') as dosya:
                parser = PDFParser(dosya)
                document = PDFDocument(parser)
                # Başlık bilgisini al
                baslik = document.info[0]['Title']
                # Başlıkta arama yap
                if kelime.lower() in baslik.lower():
                    print(f"{dosya_adi} dosyasında {kelime} kelimesi bulundu!")
    except:
        pass
