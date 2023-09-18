from ynn6d64d4 import bakiye

defkullanıcı = "yazılımcıbebe"
defparola = "1234bebe"
while (True) :
    kullanıcı = input ("kulanıcı adını giriniz :")
    parola = input ("şifrenizi giriniz :")
    if ((kullanıcı == defkullanıcı) and (parola == defparola)) :
        print ("hoşgeldiniz giriş yapılan hesap ", kullanıcı)
        print ("yapmak istediginiz işlemi seçiniz :")
        print ("1-para çekme\n 2-para yatırma ")
        seçim = int (input ("seçiminiz :"))
        if (seçim == 1) :
            print ("çekmek istediğiniz tutarı giriniz :")
            değer = input ("tl")
            print ("işlem gerçekleştiriliyor...")
            int  (bakiye,değer )
            int (bakiye,değer)
            bakiye2 = bakiye - değer
        if (seçim == 2) :
            print ("yatırmak istediğiniz tutarı giriniz :")
        break
    elif ((kullanıcı != defkullanıcı) and (parola == defparola)) :
        print ("kullanıcı adınızı kontrol ediniz!")
    elif (kullanıcı == defkullanıcı) and (parola != defparola) :
        print ("şifrenizi kontrol ediniz!")
        print ("yardım mı gerekiyor ? (E/H)")
        cevap = input (" cevap nedir ")
        if (cevap == "E") :
            yeniparola = input ("yeni parola")
            print ("lütfen bekleyin, işlem gerçekleştiriliyor")
            defparola = yeniparola
            print ("şifreniz değiştirildi")
    else :
        print ("bilgileri kontrol edin !")
