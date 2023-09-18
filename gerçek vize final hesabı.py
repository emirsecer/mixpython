vize=int(input("vizenizi giriniz"))
final=int(input("finalinizi giriniz "))
ortalama=(((vize*40)/100)+((final*60)/100))

if ortalama >50 :
    print ("geçtiniz -> :{}".format(ortalama))

else:
    print("geçemediniz ->:{}".format(ortalama))



if final<50 :
    print("finalden en az 50 alırsanız dersi geçmeye hak kazanırsınız !")