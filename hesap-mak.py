import os
def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        print("Bir sayi 0'a bölünemez!")
        return 0
    else:
        return x / y    

def us_alma(x, y):
    return x ** y
while True:

    os.system('cls')
    print("""
    *** Hesap Makinesi ***
        
        1.TOPLAMA
        2.CIKARMA
        3.CARPMA
        4.BOLME
        5.US ALMA
    """)

    sec= input("Lütfen yapmak istediğiniz işlemi seçiniz (1-5): ")
    if (sec == '1'):
        a = float(input("Birinci sayiyi giriniz: "))
        b = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {toplama(a, b)}")
    elif (sec == '2'):
        a = float(input("Birinci sayiyi giriniz: "))
        b = float(input("İkinci sayiyi giriniz: "))    
        print(f"Sonuç: {cikarma(a, b)}")
    elif (sec == '3'):
        a = float(input("Birinci sayiyi giriniz: "))
        b = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {carpma(a, b)}")
    elif (sec == '4'):
        a = float(input("Birinci sayiyi giriniz: "))
        b = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {bolme(a, b)}")
    elif (sec == '5'):
        a = float(input("Taban sayiyi giriniz: "))
        b = float(input("Üs sayisini giriniz: "))
        print(f"Sonuç: {us_alma(a, b)}")
    else:
        print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı giriniz.")
    input("Devam Etmek Istiyorsan ENTER'a Bas...")    
