import urllib.request
url1="https://avatars.mds.yandex.net/i?id=87867ac0b29423139f498254a94c5e1f_l-5220647-images-thumbs&ref=rim&n=13&w=640&h=640 "
url2="https://i.pinimg.com/236x/b6/56/e7/b656e7172dcd0f986d7bc05e8b5ec74e.jpg"
url3=  "https://img1.fonwall.ru/o/w5/zakat-pole-prud-ozero.jpg"
urllistesi=[url1,url2,url3]
say=4
for url in urllistesi :
    urllib.request.urlretrieve(url,"resim"+str(say)+".jpg")
    say+=1
