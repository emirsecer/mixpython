try:
    import random


    def greeting() :
        responses = ["Merhaba! Nasıl yardımcı olabilirim?",
                     "Merhaba, ne yapabilirim?",
                     "Selam! Nasıl yardımcı olabilirim?"]
        print (random.choice (responses))


    def goodbye() :
        responses = ["Görüşürüz!",
                     "Hoşça kalın!",
                     "Tekrar görüşmek üzere!"]
        print (random.choice (responses))


    def remindme() :
        print ("Ne zaman hatırlatmamı istersiniz? (Örnek: '10 dakika sonra')")
        time = input ()
        print (f"Tamam, size {time} hatırlatacağım.")


    def calculate() :
        print ("Lütfen bir işlem girin. (Örnek: '2 + 3')")
        problem = input ()
        print (f"Sonuç: {eval (problem)}")


    def main() :
        greeting ()
        while True :
            command = input ().lower ()
            if "görüşürüz" in command :
                goodbye ()
                break
            if "güle güle" in command:
                goodbye()
                break
            elif "hatırlat" in command :
                remindme ()
            elif "hesapla" in command :
                calculate ()
            elif "kaç eder " in command :
                calculate()
            else :
                print ("Anlamadım, tekrar söyler misiniz?")


    if __name__ == "__main__" :
        main ()
except ZeroDivisionError:
    print("0 ile bölünemiyor")
