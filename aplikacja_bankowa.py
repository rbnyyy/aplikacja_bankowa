
def password():
   global haslo
   haslo = str(input("Podaj swoje haslo."))
   global haslo_potwierdzenie
   haslo_potwierdzenie = str(input("Podaj haslo raz jeszcze."))

def zapis_danych():
    f = open("data.txt",mode='w')
    f.write(haslo)
    f.write(",")
    f.write(login)
    f.close()

def check():
    while haslo_potwierdzenie != haslo:
        print("Hasla nie są zgodne")
        password()


print("CZEŚĆ :)\nWitamy Cię w aplikacji do zarządzania walutami Currverter")

rozpoczecie = str(input("Czy chcesz założyć nowe konto walutowe? TAK/NIE")).lower()


if rozpoczecie == "tak":
    login = str(input("Podaj swoj login do rejestracji."))
else:
    print("Niepoprawny login")

if len(login) > 0:
    password()
    check()
    zapis_danych()
