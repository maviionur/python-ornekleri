
print("1-İkilik tabandan onluk tabana çevirme")
print("2-Onluk tabandan ikilik tabana çevirme")
print("3-ikilik tabandan on altılık tabana çevirme")
print("4-On altılık tabandan ikilik tabana çevirme")

islem = int(input("Yapmak istediğiniz işlemi seçin:"))

if islem == 1:
	sonuc = 0
	sayi = int(input("İkilik tabanda bir sayi girin:"))
	dizi = []
	while sayi >= 1:
		artan = sayi % 10
		dizi.append(artan)
		sayi //= 10
	print(dizi)
	sayac = 0
	for i in range(0,len(dizi)):
		sonuc += dizi[i] * (2 ** sayac)
		sayac += 1
	print("Sonuç:",sonuc)

elif islem == 2:
	sayi = int(input("Onluk tabanda bir sayi girin:"))
	dizi = []
	while sayi >= 1:
		artan = sayi % 2
		dizi.append(artan)
		sayi //= 2
	dizi.reverse()
	print(dizi)
	for i in range(0, len(dizi)):
		print(dizi[i],end="")

elif islem == 3:
	sayi = int(input("İkilik tabanda bir sayi girin:"))
	dizi = []
	while sayi >= 1:
		artan = sayi % 10
		dizi.append(artan)
		sayi //= 10
	print(dizi)
	toplam = 0
	sonuc = 0
	dizi2 = []

	sayac = 0
	while len(dizi) > 0:


		if len(dizi) < 4:
			sonuc = 0
			sayac = 0
			while len(dizi) > 0:
				sonuc += dizi[0] * (2 ** (sayac))
				dizi.pop(0)
				sayac += 1
			dizi2.append(sonuc)

		else:
			sonuc += dizi[0] * (2 ** sayac)
			dizi.pop(0)
			sayac += 1


			if sayac != 0 and sayac % 4 == 0:
				dizi2.append(sonuc)
				sonuc = 0
				sayac = 0








	print(dizi2)






