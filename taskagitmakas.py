import random
oyun = ['Tas', 'Kagit', 'Makas']
a = (random.choice(oyun))
b = input('Deger giriniz: ')
print('Bilgisayarın Sectigi: ',a)
if (a == b):
    print('Berabere')
elif(b == 'Tas'):
    if(a == 'Kagit'):
        print('Kaybettiniz!')
    else:
        print('Kazandiniz!')
elif(b == 'Kagit'):
    if(a == 'Tas'):
        print('Kazandiniz!')
    else:
        print('Kaybettiniz!')
elif(b == 'Makas'):
    if(a == 'Kagit'):
        print('Kazandiniz!')
    else:
        print('Kaybettiniz!')
else:
    print('Hatali deger girdiniz')







