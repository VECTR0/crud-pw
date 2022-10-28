### Opis projektu

Prototyp systemu dla serwisu komputerowego. Umożliwia stworzenie zgłoszenia, wylistowanie wszystkich zgłoszeń, ewentulną edycję lub anulowanie oraz wyszukiwanie wybranych zgłoszeń.

### Instalacja

## Linux

Uruchom skrypt `install.sh`

## Windows

Uruchom skrypt `install.bat`

### Uruchamianie

W pliku `.env` znajduje się konfiguracja systemu. Standardowa konfiguracja to `:3000` frontend oraz `:5000` backend.

## Linux

Uruchom `run.sh`

## Windows

Uruchom `run.bat`

### Użytkowanie

Po uruchomieniu otworzy się okno przeglądarki `http://localhost:3000/`. Do adresu URL dodajemy `v1-4`, które są widokami: klienta, dwa zarządcy, oraz technika. Klient może dodać zgłoszenie, zarządca może sprawdzić wszystkie zgłoszenia danego klienta, zmodyfikować zgłoszenie klienta lub ewentualnie usunąć zgłoszenie, a technik wyszukać zgłoszenie po jego identyfikatorze.
