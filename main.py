import sqlite3
import datetime
import sys
import os  # <--- NOWOŚĆ: Do sprawdzania czy plik istnieje

# --- KONFIGURACJA BAZY DANYCH ---
DB_NAME = "magazyn.db"

def polacz_z_baza():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS odczynniki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa TEXT NOT NULL,
            data_waznosci TEXT,
            ilosc INTEGER
        )
    ''')
    conn.commit()
    return conn

# --- FUNKCJE LOGICZNE ---

def dodaj_odczynnik(conn):
    print("\n➕ DODAWANIE ODCZYNNIKA (RĘCZNE)")
    nazwa = input("Podaj nazwę (np. Glukoza R1): ")
    data = input("Data ważności (RRRR-MM-DD): ")
    try:
        ilosc = int(input("Ilość opakowań: "))
    except ValueError:
        print("❌ Błąd: Ilość musi być liczbą!")
        return

    cursor = conn.cursor()
    cursor.execute("INSERT INTO odczynniki (nazwa, data_waznosci, ilosc) VALUES (?, ?, ?)", 
                   (nazwa, data, ilosc))
    conn.commit()
    print("✅ Dodano do bazy!")

def pokaz_magazyn(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM odczynniki")
    wyniki = cursor.fetchall()
    
    print("\n📦 STAN MAGAZYNU:")
    print(f"{'ID':<4} | {'NAZWA':<20} | {'DATA WAŻN.':<12} | {'ILOŚĆ'}")
    print("-" * 50)
    
    for wiersz in wyniki:
        print(f"{wiersz[0]:<4} | {wiersz[1]:<20} | {wiersz[2]:<12} | {wiersz[3]}")

def sprawdz_terminy(conn):
    print("\n⏳ ANALIZA TERMINÓW WAŻNOŚCI...")
    dzisiaj = datetime.date.today().strftime("%Y-%m-%d")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM odczynniki WHERE data_waznosci < ?", (dzisiaj,))
    przeterminowane = cursor.fetchall()
    
    if przeterminowane:
        print(f"🚨 ALARM! Znaleziono {len(przeterminowane)} przeterminowanych odczynników:")
        for p in przeterminowane:
            print(f"   ❌ (ID: {p[0]}) {p[1]} -> Ważność: {p[2]}")
    else:
        print("✅ Wszystkie odczynniki są ważne.")

def usun_odczynnik(conn):
    print("\n🗑️ USUWANIE ODCZYNNIKA")
    pokaz_magazyn(conn)
    
    try:
        id_do_usuniecia = int(input("\nPodaj ID odczynnika do usunięcia: "))
    except ValueError:
        print("❌ Błąd: ID musi być liczbą!")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM odczynniki WHERE id=?", (id_do_usuniecia,))
    if not cursor.fetchone():
        print("❌ Nie ma takiego ID w bazie!")
        return

    cursor.execute("DELETE FROM odczynniki WHERE id=?", (id_do_usuniecia,))
    conn.commit()
    print(f"✅ Odczynnik o ID {id_do_usuniecia} został usunięty.")

def import_dostawy(conn):
    print("\n🚚 INTELIGENTNY IMPORT DOSTAWY...")
    
    # 1. SPRAWDZANIE JAKI PLIK ISTNIEJE
    if os.path.exists("dostawa.csv"):
        nazwa_pliku = "dostawa.csv"
        print("📂 Wykryto plik: dostawa.csv")
    elif os.path.exists("dostawa.txt"):
        nazwa_pliku = "dostawa.txt"
        print("📂 Wykryto plik: dostawa.txt")
    else:
        print("❌ Błąd: Nie znaleziono pliku 'dostawa.csv' ani 'dostawa.txt'!")
        return

    try:
        with open(nazwa_pliku, "r", encoding='utf-8') as plik:
            linie = plik.readlines()
            
        cursor = conn.cursor()
        licznik = 0
        
        for linia in linie:
            linia = linia.strip() # Usuń spacje/entery z końców
            if not linia: continue # Pomiń puste linie
            
            # 2. WYKRYWANIE SEPARATORA (Przecinek vs Średnik)
            if ";" in linia:
                dane = linia.split(";") # Tryb Polski Excel
            else:
                dane = linia.split(",") # Tryb Standardowy
            
            # Walidacja danych
            if len(dane) == 3:
                nazwa = dane[0].strip()
                data = dane[1].strip()
                try:
                    ilosc = int(dane[2].strip())
                    
                    cursor.execute("INSERT INTO odczynniki (nazwa, data_waznosci, ilosc) VALUES (?, ?, ?)", 
                                   (nazwa, data, ilosc))
                    licznik += 1
                    print(f"   ➕ Wczytano: {nazwa}")
                except ValueError:
                    print(f"   ⚠️ Błąd ilości w linii: {linia}")
            else:
                print(f"   ⚠️ Zły format linii: {linia}")
                
        conn.commit()
        print(f"✅ Sukces! Dodano {licznik} nowych pozycji.")
        
    except Exception as e:
        print(f"❌ Wystąpił niespodziewany błąd: {e}")

# --- MENU GŁÓWNE ---
def main():
    conn = polacz_z_baza()
    
    while True:
        print("\n=== 🧪 SMART REAGENT MANAGER v1.3 ===") # Wersja 1.3
        print("1. 📦 Pokaż stan magazynu")
        print("2. ➕ Dodaj nowy odczynnik")
        print("3. ⏳ Sprawdź terminy ważności")
        print("4. 🗑️ Usuń odczynnik (Zużycie)")
        print("5. 🚚 Importuj dostawę (Auto-Detect CSV/TXT)")
        print("6. 🚪 Wyjście")
        
        wybor = input("WYBIERZ OPCJĘ (1-6): ")
        
        if wybor == '1':
            pokaz_magazyn(conn)
        elif wybor == '2':
            dodaj_odczynnik(conn)
        elif wybor == '3':
            sprawdz_terminy(conn)
        elif wybor == '4':
            usun_odczynnik(conn)
        elif wybor == '5':
            import_dostawy(conn)
        elif wybor == '6':
            print("Zamykam system...")
            conn.close()
            sys.exit()
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()
