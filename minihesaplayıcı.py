def islem(islem_adi):


    def toplam(args1,args2):
       toplama=args1+args2
       return toplama

    def cikarim(args1,args2):
        fark=args1-args2
        return fark

    def carpma(args1,args2):
        carpim=args1*args2
        return carpim

    def bolum(args1,args2):
        bolme=args1/args2
        return bolme




    if islem_adi=="toplama":
        return toplam
    elif islem_adi=="çıkartma":
        return cikarim
    elif islem_adi=="bölme":
        return bolum
    elif islem_adi=="çarpma":
        return carpma


bolme=islem("bölme")
print(bolme(8,4))

carpim=islem("çarpma")
print(carpim(2,6))

cıkarma=islem("çıkartma")
print(cıkarma(8,5))

toplam=islem("toplama")
print(toplam(2,6))



