<<<<<<< HEAD
import sys

bank_pln = 0


def konwersja_waluty():
    global bank_pln
    print("Aktualnie dostępne waluty do konwersji: EUR, GBP, USD")
    wybrana_waluta = input("Wybierz walutę, na którą chcesz dokonać konwersji: ").upper()
    kwota_pln = int(input("Podaj kwotę PLN do konwersji: "))

    kursy_walut = {
        "EUR": 0.23,
        "GBP": 0.20,
        "USD": 0.25
    }

    if wybrana_waluta in kursy_walut:
        kwota_po_konwersji = kwota_pln * kursy_walut[wybrana_waluta]
        if bank_pln >= kwota_pln:
            bank_pln -= kwota_pln
            print(f"{kwota_pln} PLN zostało skonwertowane na {kwota_po_konwersji} {wybrana_waluta}")
            print(f"Aktualny stan konta PLN: {bank_pln} PLN")
            kolejny_krok()
        else:
            print("Nie masz wystarczającej ilości PLN do konwersji.")
            kolejny_krok()
    else:
        print("Wybrana waluta nie jest dostępna do konwersji.")
        kolejny_krok()
def rejestracja():
    global login
    global haslo
    login = input("Podaj login : ")
    haslo = input("Podaj haslo : ")
    zapis = input("Zarejestrować nowe konto w bazie?")
    if zapis == "tak":
        zapis_danych()
    zaczynamy_dwa = input("Czy po rejestracji chcesz się zalogować?")
    while zaczynamy_dwa == "tak":
        if zaczynamy_dwa == "tak":
            weryfikacja_logowanie()
        elif wejscie == "nie":
            sys.exit()
=======

def password():
   global haslo
   haslo = str(input("Podaj swoje haslo."))
   global haslo_potwierdzenie
   haslo_potwierdzenie = str(input("Podaj haslo raz jeszcze."))
>>>>>>> origin/aplikacja_bankowa

def zapis_danych():
    f = open("data.txt",mode='w')
    f.write(haslo)
    f.write(",")
    f.write(login)
    f.close()

<<<<<<< HEAD
def wplata_waluty_innej_niz_PLN():
    print("Jaka walute chcesz wplacic?")
    waluta = input("EUR/GBP/PLN/USD").lower
    if waluta == "eur":
        kwota_EUR()
    elif waluta == "gbp":
        kwota_GBP()
    elif waluta == "usd":
        kwota_USD()


def kwota_EUR():
    eur = int(input("Ile EUR wpłacic?"))
    global bank_eur
    bank_eur = 0
    bank_eur += bank_eur + eur


def kwota_GBP():
    gbp = int(input("Ile GBP wpłacic?"))
    global bank_gbp
    bank_gbp = 0
    bank_gbp += bank_gbp + gbp


def kwota_USD():
    usd = int(input("Ile USD wpłacic?"))
    global bank_usd
    bank_usd = 0
    bank_usd += bank_usd + usd


def kolejny_krok():
    print("Co chcesz dalej wykonac?")
    while True:
        wybor = input("wplacic[PLN]/wymienic/zakonczyc?")
        if wybor == "wplacic":
            portfel_PLN()
        elif wybor == "wymienic":
            konwersja_waluty()
        elif wybor == "zakonczyc":
            sys.exit()


def portfel_PLN():
    pln = int(input("Ile PLN wpłacic?"))
    global bank_pln
    bank_pln += pln
    print(f"Ilość wpłacona to {bank_pln} PLN")
    if bank_pln > 0:
        kolejny_krok()

def weryfikacja_logowanie():
    login_logowanie = input("Podaj login do logowania: ")
    haslo_logowanie = input("Podaj haslo do logowania: ")

    with open("data.txt", mode='r') as f:
        dane = f.readline().strip().split(',')
        saved_haslo = dane[0]
        saved_login = dane[1]

    if haslo_logowanie == saved_haslo and login_logowanie == saved_login:
        print("Zalogowano pomyslnie")
        kolejny_krok()
    else:
        print("Błędny login lub hasło")

    while haslo_logowanie != saved_haslo:
        print("Hasła nie są zgodne")
        weryfikacja_logowanie()



print("Zaczynamy?")
zaczynamy = input("Rejestracja czy Logowanie?").lower()
if zaczynamy == "rejestracja":
    rejestracja()
while zaczynamy == "logowanie":
    print("Nastąpi proces do logowania.")
    wejscie = input("Wpisz 'tak' aby przejśc dalej,wpisz 'nie' aby zakonczyc działanie programu").lower()
    if wejscie == "tak":
        weryfikacja_logowanie()
    elif wejscie == "nie":
        sys.exit()







=======
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
>>>>>>> origin/aplikacja_bankowa
