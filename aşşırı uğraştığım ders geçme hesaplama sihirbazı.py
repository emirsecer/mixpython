

while True :
 try :
  note1 = int(input("bir not giriniz"))
  note2 = int(input("bir not giriniz"))
  note3 = int(input("bir not giriniz"))
  topla = note1 + note2 + note3
  ortalama = topla / 3
  canegrisi = int(input(" size bildirilen çan eğrisi değerini giriniz"))

  if (ortalama > 50):
      print("ortalama:{}".format(ortalama))
      print("geçtiniz")
      break

  elif note1 == 0 or note2 == 0 or note3 == 0:
      print("sınavdan 0 alan öğrenci geçemez.")
      break


  elif ortalama >= canegrisi:
      print("çan eğrisinin üzerinde kalarak geçmeye hak kazandınız :")
      break


  else:
      print("ortalama:{}".format(ortalama))
      print("maalesef bu dersten geçemediniz")
      break

 except ValueError :
       print("lütfen sayı olacak  şekilde notları tekrar giriniz ")