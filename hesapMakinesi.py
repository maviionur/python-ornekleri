sayi1 = int(input("İlk sayiyi girin:"))
sayi2 = int(input("İkinci sayiyi girin:"))
islem = int(input("Bir işlem seçin\n 1-Toplama\n 2-Çıkarma\n 3-Çarpma\n 4-Bölme\n 5-Mod alma\n"))
toplam = 0
if islem == 1:
	toplam =sayi1+sayi2
	print("Sonuç:",toplam)
elif islem == 2:
	toplam = sayi1-sayi2
	print("Sonuç:",toplam)
elif islem ==3:
	toplam = sayi1 * sayi2
	print("Sonuç:",toplam)
elif islem ==4:
	toplam = sayi1/sayi2
	print("Sonuç",toplam)
elif islem ==5:
	toplam = sayi1 % sayi2
	print("Sonuç:",toplam)
else:
	print("Böyle bir işlem yok")


