try:
     dosya =open("yazılımbilimi.txt","r")
except IOError:
    print("dosya bulunamadı.")

finally:
    dosya.close()



