izinli_karakterler = "0123456789+-/*=%. "

print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

while True:
    veri = input("İşleminiz: ")
    if veri == "q":
        print("çıkılıyor...")
        break

    for s in veri:
        if s not in izinli_karakterler:
            print("Neyin peşindesin?!")
            quit()

    hesap = eval(veri)

    print(hesap)
