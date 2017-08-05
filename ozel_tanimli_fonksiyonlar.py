#-*-coding:utf-8-*-
from math import sqrt
from math import pow

print("Fonkiyonları En Geniş Tanım Kümesi")

islem = input("Tanım kümesini bulmak istediğiniz fonksiyonu \n"
            "Dikkali bir şekilde belirtiniz.\n"
            "En fazla 2.dereceden ifadeler için kulanılır.\n"
            "Not : kökleri/Dereceli ifadeler için 'x' karakterini\n"
             "Kullanınız. :")



parcali = list()#Kullanıcıdan aldığımız fonksiyonu parçalıyoruz.
                #ve gerekli olan parçaları sakladığımız liste

carp = 0# '*' karakterinden kaç tane olduğunu saklar.
topla =0 # '+' karakterinden kaç tane olduğunu saklar.
kök = 0 # 'x' karakterinden kaç tane olduğunu saklar.
cık = 0
for i in islem: # '*' karakterinden kaç tane olduğunu sayar.
    if '*' in i:
        carp +=1
for i in islem:# '+' karakterinden kaç tane olduğunu sayar.
    if '+' in i:
        topla +=1
for i in islem:# '-' karakterinden kaç tane olduğunu sayar.
    if '-' in i:
        cık -=1
for i in islem:# 'x' karakterinden kaç tane olduğunu sayar.
    if 'x' in i:
        kök +=1

# '*' ve '+' karakterleri hariç
#  diğer bütün karakterleri parcali listesine ekler
for i in islem:
    if '*' not in i and '+' not in i and '-' not in i:
        parcali.append(i)


#?????????????????????????????????????????????????????????????????????????????????????????????????

#girilen değerin sabit bir fonksiyon mu olduğunu kontrol eder.
if carp == 0 & topla == 0:
    global sayilar
    sayilar = '1234567890'
    if str(parcali) in str(sayilar):
        print("Tanım kümesi : Reel sayılar\n"
              "Girdiğiniz fonksiyon: Sabit bir fonksiyon.\n")
    else:
        print("hatalı değer girişi yaptınız")


 #?????????????????????????????????????????????????????????????????????????????????????????????????????
#girilen değerin doğrusal bir fonksiyon(mx+c) mu olduğunu kontrol eder.
#Girilen değer doğrusal bir fonksiyon ise köklerin değerini bulur.
elif carp == 1 and (topla == 1 or topla ==0) and kök == 1:
    k = "" #x li terimin katsayılarını bulur
    r = ""# sabit terimin değerini bulur.
    sıra = 0
    for i in parcali:
        if 'x' not in i:
            k +=i
            sıra +=1
        else:
            break
    for i in parcali[sıra+1::1]:
        r +=i
    kök = -(int(r)/int(k))
    print("X in kat sayısı ve Başkat sayı:{}\n"
          "Sabit terim : {}\n "
          "Çözüm kümesi X: {}".format(k,r,kök))


#????????????????????????????????????????????????????????????????????????????????????????????????????

#Girilen değerin 2.derecen bir fonksiyon mu oldğunu kontrol eder.
#Eger 2.dereceden ise köklerini bulur.
elif (carp == 4 or carp == 3) and \
    (topla ==0 or topla == 1 or topla ==2)\
    and (cık == 0 or cık == 1 or cık ==2)\
    and (kök == 2 or kök == 1):
    print("2.dereceden denklem")

    # 4*x**2+4*x+1 Benzeri kökler için
    if(kök == 2 and (topla ==2 or topla == 1 or topla == 0)
    and (cık == 1 or cık == 2 or cık == 0)):
        diskriminant =0
        a,b,c = "","",""
        say = list()
        say.append(0)
        k=0
        for i in parcali:
            if 'x' not in i:
                a += i
                say[0] = int(say[0]) + 1
            else:
                break

        k = int(say[0]) + 2
        for i in parcali[k::1]:
            if 'x' not in i:
                b += i
                say[0] = int(say[0]) + 1
            else:
                break

        k = int(say[0]) + 3
        for i in parcali[k::1]:
            if 'x' not in i:
                c += i
                say[0] = int(say[0]) + 1
            else:
                break
        # diskriminant değerini bulacak.
        # diskriminant 2.dereceden denklemin reel kökü olduğunu
        # kontrol etmek amacı ve köklerin değerlerini bulurken
        # kullacağımız bir değişkenimiz.Matematik 2'de(lise) öğrenebilirsiniz.
        diskriminant = pow(float(b), 2) - (4 * float(a) * float(c))
        print("Disriminant değeri:{}".format(diskriminant))


        if (diskriminant >0):
            print("2.derecen denklim kökleri:")
            x1 = (-int(b) - sqrt(diskriminant)) / 2 * int(a)
            x2 = (-int(b) + sqrt(diskriminant)) / 2 * int(a)
        elif(diskriminant == 0):
            x1 = -float(b)/(2*float(a))
            x2 = x1
        else:
            print("girdiğiniz 2. dereceden denklemin reel kök yok.")

        print("x1 kökün değeri: {}\nx2 kökün değeri :{}"
              .format(x1, x2))
        print(say[0])
        print("değerler ", a, b, c)
    # 4*x**2+4*x  Benzeri kökler için
    elif(kök == 2 and (topla == 1 or cık == 1)):
        a, b, c = "", "", ""
        say = list()
        say.append(0)
        k = 0 # say  dizisine(liste) sıra belirtmek için

        # 'x**2' terim kat sayısı
        for i in parcali:
            if 'x' not in i:
                a += i
                say[0] = int(say[0]) + 1
            else:
                break
        # 'x' li terim kat sayısı
        k = int(say[0]) + 2
        for i in parcali[k::1]:
            if 'x' not in i:
                b += i
                say[0] = int(say[0]) + 1
            else:
                break
        #sabit terim
        c += '0'

        #Kökleri bulacağız
        x1 = 0
        x2 = -float(a)/float(b)

        print("kok degerleri",x1,x2)
        print(say[0])
        print("değerler ", a, b, c)
    # x**2 + 1 türü denklemlerin çözümü
    elif(kök == 1 and ( topla == 1 or cık == 1)):
        a, b, c = "", "", ""
        diskriminant=0
        say = list()
        say.append(0)
        k = 0  # say  dizisine(liste) sıra belirtmek için

        # 'x**2' terim kat sayısı
        for i in parcali:
            if 'x' not in i:
                a += i
                say[0] = int(say[0]) + 1
            else:
                break
        # 'x' li terim kat sayısı
        b = '0'
        #sabit terim
        k = int(say[0]) + 2
        for i in parcali[k::1]:
            if 'x' not in i:
                c += i
                say[0] = int(say[0]) + 1
            else:
                break


        # diskriminant değerini bulacak.
        # diskriminant 2.dereceden denklemin reel kökü olduğunu
        # kontrol etmek amacı ve köklerin değerlerini bulurken
        # kullacağımız bir değişkenimiz.Matematik 2'de(lise) öğrenebilirsiniz.
        diskriminant = pow(float(b), 2) - (4 * float(a) * float(c))
        print("Disriminant değeri:{}".format(diskriminant))

        if (diskriminant > 0):
            print("2.derecen denklim kökleri:")
            x1 = sqrt(float(a) / float(b))
        else:
            print("girdiğiniz 2. dereceden denklemin reel kök yok.")

        print("x1 kökün değeri: {}".format(x1,))
        print(say[0])
        print("değerler ", a, b, c)



print("Parcalı listesinin içindekiler:",parcali)

"""
   
        #diskriminant değerini bulacak.
        #diskriminant 2.dereceden denklemin reel kökü olduğunu
        #kontrol etmek amacı ve köklerin değerlerini bulurken
        #kullacağımız bir değişkenimiz.Matematik 2'de(lise) öğrenebilirsiniz.
        print(a,b,c)
        diskriminant = pow(int(b),2)-(4*int(a)*int(c))
        print("Disriminant değeri:{}".format(diskriminant))
        if(diskriminant >=1):
            print("2.derecen denklim kökleri:")
            x1 = (-int(b)-sqrt(diskriminant))/2*int(a)
            x2 = (-int(b)+sqrt(diskriminant))/2*int(a)
        else:
            print("girdiğiniz 2. dereceden denklemin reel kök yok.")

        print("x1 kökün değeri: {}\nx2 kökün değeri :{}"
              .format(x1,x2))
    # x**2+2*x gibi 2.dereceden denklem için
    elif(kök ==2 and topla ==1):
        # En büyük dereceli (x**2) terimin kat sayısını bulacak
        for i in parcali:
            if 'x' not in i:
                a += i
                say += 1
            else:
                break
                # 'x**1'terimin kat sayısını bulacak
        for i in parcali[say + 2::1]:
            if 'x' not in i:
                b += i
                say += 1
            else:
                break
        # sabit terimi bulacak.
        c +='0'

        # diskriminant değerini bulacak.
        # diskriminant 2.dereceden denklemin reel kökü olduğunu
        # kontrol etmek amacı ve köklerin değerlerini bulurken
        # kullacağımız bir değişkenimiz.Matematik 2'de(lise) öğrenebilirsiniz.
        diskriminant = pow(int(b),2)- 4 * int(a) * int(c)
        print("Disriminant değeri:{}".format(diskriminant))
        if (diskriminant >=1):
            print("2.derecen denklim kökleri:")
            x1 = (-int(b) - sqrt(diskriminant)) / 2 * int(a)
            x2 = (-int(b) + sqrt(diskriminant)) / 2 * int(a)
        else:
            print("girdiğiniz 2. dereceden denklemin reel kök yok.")

        print("x1 kökün değeri: {}\nx2 kökün değeri :{}"
              .format(x1, x2))


"""

print(*parcali)
print(parcali)
