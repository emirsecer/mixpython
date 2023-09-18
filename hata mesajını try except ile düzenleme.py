sayı1=input("sayı1:")
sayı2=input("sayı2:")


try:
    sayı1=int(sayı1)
    sayı2=int(sayı2)
    print( sayı1/sayı2)

except ValueError:
    print("lütfen bir sayı girdiğinizden emin olun.")

except ZeroDivisionError:
    print("sayı sıfır ile bölünemiyor.")