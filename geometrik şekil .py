def geometri(şekil) :
    if len(şekil)==3:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]

        if (a+b)>c and (a+c)>b and (b+c)>a :
            if(a==b) and (a==c) and (b==c):
               print("bu eşkenar üçgendir.")
            elif (a==b) and (a==c) :
                print ("ikizkenar üçgendir ")
            else :
                 print("çeşikenar üçgendir.")

        else :
            print("üçgen belirtmiyor. ")






    elif len(şekil)==4:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]
        d=şekil[3]
        if(a==b ) and (a==c ) and (a==d):
           print("karedir .")
        elif (a==c) and (b==d):
            print("dikdörtgendir.")
        else:
            print("herhangi bir dörtgen ")




    else :
         print("bu bir şekil verileri hatalı görünüyor !")


while (True):
    elemansayısı=int(input("eleman sayısını giriniz"))
    if (elemansayısı==3):
        a= int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri([a,b,c])


    elif (elemansayısı==4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d =int(input("d"))
        geometri([a,b,c,d])


    else:
        print("lütfen tekrar giriniz ")