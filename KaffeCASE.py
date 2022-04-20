import random



print('Hej, og velkommen til den virtuelle kaffebar. Før du kan bestille skal du logge ind.\n')
class Login():
    def __init__(self):
        self.brugernavn = input('Kea-Email : ')
        self.adgangskode = input('Adgangskode : ')

    def login_check(self):
        file = open("Login.txt","r")
        if '@' not in self.brugernavn:
            print('Kea-Email skal indeholde @')
            print('Log venligst ind igen')
            login = Login()
            login.login_check()
        elif self.brugernavn and self.adgangskode in file:
            print('\nVelkommen', self.brugernavn)
        else:
            print("\nlogin mislykkedes")
            spørgsmål = input("\nEr det første gang du logger ind på denne kaffemaskine med din Kea-Email? ja/nej : ")

            if spørgsmål == "ja":
                print('Du skal skrive din Kea-Email og adgangskode første gang du logger ind.')
                print('Dette skal du gøre for at opdatere dine oplysingner i vores system.')
                self.opdater_system()

            if spørgsmål == 'nej':
                print('Prøv at logge ind igen.')
                login = Login()
                login.login_check()
            file.close()
    def opdater_system(self):
        file = open("Login.txt", "a")
        file.write("\n" + input('Kea-Email : '))
        file.write("\n" + input('Adgangskode : '))
        print('Login opdateret i vores system. Prøv venligst at logge ind igen.')
        file.close()
        login = Login()
        login.login_check()


login = Login()
login.login_check()

#her spørges der om kunde vil svare på spg. Derudover kører den videre til betaling, så den rigtige procent bliver trukket fra
#først ses uden rabat
class rabat():
    def __init__(self):
        self.procent= input("Vil du svare på et spørgsmål fra en tidligere kunde, og stille et til den næste, for at spare 20% på din kaffe? Hvis du vil, indtast 'ja', hvis ikke indtast 'nej' \n")
        if self.procent == 'nej':
            print("En lille kop koster 20kr, og en stor kop koster 30kr, hvilken størrelse ønsker du?")
            self.size()
        if self.procent == 'ja':
            self.question()
        else:
            print("Valg eksisterer ikke, prøv igen")
            self.__init__()

    def size(self):
        self.size = input("Skriv stor for stor kop, lille for en lille kop.\n")
        if self.size == 'stor':
            print("Perfekt, det bliver en stor kop til dig")
            print("Du skal vælge en stor kop når du kommer til menuen, betal nu de 30kr'\n")
        if self.size == 'lille':
            print("Perfekt, det bliver en lille kop til dig")
            print("Du skal vælge en lille kop når du kommer til menuen, betal nu de 20kr'\n")

    def size_rabat(self):
        self.size_rabat = input("Skriv stor for stor kop, lille for en lille kop.\n")
        if self.size_rabat == 'stor':
            print("Perfekt, det bliver en stor kop til dig")
            print("Du skal vælge en stor kop når du kommer til menuen, betal nu de 24kr'\n")
        if self.size_rabat == 'lille':
            print("Perfekt, det bliver en lille kop til dig")
            print("Du skal vælge en lille kop når du kommer til menuen, betal nu de 16kr'\n")

    def question(self):
        self.question_list = ['Spørgsmålet før dig, blev spurgt af Rebecca. Hvad er din yndlings film?','Spørgsmålet før dig, blev spurgt af Karsten. Hvad er din hårfarve?', 'Spørgsmålet før dig, blev spurgt af Morten. Hvad er din livret?']
        self.choose = random.choice(self.question_list)
        print(self.choose)
        input()
        input("Hvilket spørgsmål, vil du stille til personen efter dig?\n")
        print("Tak for at være social! Du sparer nu 20% på din kaffe, te eller kakao.")
        print("En lille kop koster normalt 20kr, nu 16kr, og en stor kop koster normalt 30kr, men nu 24kr, hvilken størrelse ønsker du?\n ")
        self.size_rabat()

rabat()

class betaling():
    def __init__(self):
        self.godkend = input("Betal nu ved at skrive 'godkend'\n")
        if self.godkend == 'godkend':
            print("Betaling gennemført")
        else:
            print("Betaling kunne ikke gennemføres, prøv igen")
            self.__init__()
betaling()

#nu skal kunde vælge hvilken form for drikkelse de ønsker
class Drik():
    def __init__(self, vand):
        self.vand = vand

    def info(self):
        return "Vand: "+ self.vand
#stor café latte
class Cafe_latte(Drik):
    def __init__(self, vand, maelk, kaffepulver):
        Drik.__init__(self, vand)
        self.maelk = maelk
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand:" + self.vand + "Mælk: " + self.maelk + "Kaffepulver:" + self.kaffepulver

#lille cafe latte
class cafe_latte(Drik):
    def __init__(self, vand, maelk, kaffepulver):
        Drik.__init__(self, vand)
        self.maelk = maelk
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand:" + self.vand + "Mælk: " + self.maelk + "Kaffepulver:" + self.kaffepulver

#Stor Kakao
class Kakao(Drik):
    def __init__(self, vand , kakaopulver):
        Drik.__init__(self, vand)
        self.kakaopulver = kakaopulver

    def info(self):
        return "Vand: " + self.vand + "Kakaopulver:" + self.kakaopulver

#lille kakao
class kakao(Drik):
    def __init__(self, vand , kakaopulver):
        Drik.__init__(self, vand)
        self.kakaopulver = kakaopulver

    def info(self):
        return "Vand: " + self.vand + "Kakaopulver:" + self.kakaopulver

#Stor americano
class Americano(Drik):
    def __init__(self, vand, kaffepulver):
        Drik.__init__(self, vand)
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand: " + self.vand + "kaffepulver: " + self.kaffepulver

#Lille americano'@' not in self.brugernavn:'@' not in self.brugernavn:
class americano(Drik):
    def __init__(self, vand, kaffepulver):
        Drik.__init__(self, vand)
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand: " + self.vand + "kaffepulver: " + self.kaffepulver

#Stor espresso
class Espresso(Drik):
    def __init__(self, vand, kaffepulver):
        Drik.__init__(self, vand)
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand: " + self.vand + "kaffepulver: " + self.kaffepulver

#Lille espresso
class espresso(Drik):
    def __init__(self, vand, kaffepulver):
        Drik.__init__(self, vand)
        self.kaffepulver = kaffepulver

    def info(self):
        return "Vand: " + self.vand + "kaffepulver: " + self.kaffepulver

#stor te
class Te(Drik):
    def __init__(self, vand, tebrev):
        Drik.__init__(self, vand)
        self.tebrev = tebrev

    def info(self):
        return "Vand: " + self.vand + "Te smag: " + self.tebrev

#Lille te
class te(Drik):
    def __init__(self, vand, tebrev):
        Drik.__init__(self, vand)
        self.tebrev = tebrev

    def info(self):
        return "Vand: " + self.vand + "Te smag: " + self.tebrev


Cafe_latte1 = Cafe_latte(" 75 ml. ", "280 ml. ", " 21 g.")
Cafe_latte2 = cafe_latte(" 55 ml. ", "250 ml. ", " 14 g.")
Kakao1 = Kakao("350 ml. ", " 52 g.")
Kakao2 = kakao("250 ml. ", " 39 g.")
Espresso1 = Espresso("75 ml. ", " 21 g.")
Espresso2 = espresso("55 ml. ", " 14 g.")
Te1 = Te("450 ml. ", " Mint")
Te2 = te("300 ml. ", " Mint")
Americano1 = Americano(" 355 ml. ", " 21 g.")
Americano2 = americano(" 305 ml. ", " 14 g.")


class size_choose():
    def __init__(self):
        self.size11 = input("Vil du se menuen for en stor eller lille drik? \n")
        if self.size11 == "stor":
            print("cafe latte")
            print(Cafe_latte1.info())
            print("kakao")
            print(Kakao1.info())
            print("espresso")
            print(Espresso1.info())
            print("te")
            print(Te1.info())
            print("americano")
            print(Americano1.info())
        elif self.size11 == "lille":
            print("cafe latte")
            print(Cafe_latte2.info())
            print("kakao")
            print(Kakao2.info())
            print("espresso")
            print(Espresso2.info())
            print("te")
            print(Te2.info())
            print("americano")
            print(Americano2.info())
        else:
            print("Valg eksisterer ikke, prøv igen")
            self.__init__()
size_choose()


#her tælles der ned, og kaffen laves
class Choose():
    def __init__(self):
        self.liste = ["cafe latte", "kakao", "espresso", "te", "americano"]
        self.drik = input("Hvilken drik ønsker du ud af menukortet?\n")
        if self.drik in self.liste:
            n = 5
            while n > 0 :
                print(n)
                n = n - 1
            print("Din", self.drik, "er nu klar!")
        if self.drik not in self.liste:
            print("Du skal vælge en drik fra menukortet?")
            self.__init__()
Choose()
print("Tak fordi du valgte at bruge vores sociale kaffemaskine\n")
print("Hav en god dag!!")
