import random

# Rastgele selamlama mesajları listesi
greetings = ["Merhaba! Benimle ne yapabilirim?",
             "Selam, nasıl yardımcı olabilirim?",
             "Merhaba! Ne yapabilirim?"]

# Rastgele elveda mesajları listesi
goodbyes = ["Güle güle!",
            "Hoşça kal!",
            "Görüşürüz!"]

# Kullanıcının sorduğu sorulara verilebilecek cevaplar
responses = {"nasılsın": "İyiyim, teşekkür ederim. Sen nasılsın?",
             "bugün hava nasıl": "Sanırım dışarı çıkmak için güzel bir gün.",
             "yapabileceğin şeyler neler": "Size hatırlatma yapabilirim veya sizi eğlendirebilirim.",
             "teşekkürler": "Rica ederim, her zaman buradayım."}

def chat():
    # Asistanın kullanıcıya rastgele bir selamlama mesajı göndermesi
    print(random.choice(greetings))

    while True:
        # Kullanıcının girdiği mesajın alınması
        message = input().lower()

        # Kullanıcı asistanı kapatmak istiyorsa
        if message == "görüşürüz":
            # Rastgele bir elveda mesajı gönderilir ve döngü sonlandırılır
            print(random.choice(goodbyes))
            break

        # Kullanıcının sorusuna verilebilecek bir cevap varsa
        elif message in responses:
            # İlgili cevap yazdırılır
            print(responses[message])

        # Bilinmeyen bir mesaj alındıysa
        else:
            # Kullanıcı anlaşılmadı mesajı alır
            print("Anlamadım, tekrar söyler misiniz?")

if __name__ == "__main__":
    chat()
