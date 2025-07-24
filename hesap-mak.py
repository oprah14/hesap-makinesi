import os
def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        print("Bir sayi 0'a bölünemez!")
        return 0
    else:
        return x / y    

def exponentiation(x, y):
    return x ** y

x = 0
y = 0
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
        x = float(input("Birinci sayiyi giriniz: "))
        y = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {addition(x, y)}")
    elif (sec == '2'):
        x = float(input("Birinci sayiyi giriniz: "))
        y = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {substraction(x, y)}")
    elif (sec == '3'):
        x = float(input("Birinci sayiyi giriniz: "))
        y = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {multiplication(x, y)}")
    elif (sec == '4'):
        x = float(input("Birinci sayiyi giriniz: "))
        y = float(input("İkinci sayiyi giriniz: "))
        print(f"Sonuç: {division(x, y)}")
    elif (sec == '5'):
        x = float(input("Taban sayiyi giriniz: "))
        y = float(input("Üs sayisini giriniz: "))
        print(f"Sonuç: {exponentiation(x, y)}")
    else:
        print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı giriniz.")
    input("Devam Etmek Istiyorsan ENTER'a Bas...")    
