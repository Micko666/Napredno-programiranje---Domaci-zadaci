
# Napredno programiranje - Domaci zadaci

## Domaci 1

### Korisceni alati
- Python 3.12
- VS Code
- Git i GitHub
- Ruff
- pytest

### Opis
Implementirana je funkcija prosjecna_cijena koja cita rezervacije iz CSV fajla i racuna ponderisanu prosjecnu cijenu nocenja.

### Korisceni AI upiti
1. Koristeci ruff, objasni mi kako da provjerim kod.
2. formiraj mi 3 podatka za rezervacije koristeci sledeci format gost,noci,cijena_noci u csv obliku.
3. Formiraj mi test tako da provjeri da li se vrijednost dobijena funkciom poklapa sa ponderisanom vrijednoscu.

### Uoceni problemi i ispravke
- Python nije pronalazio modul zbog pogresnog radnog direktorijuma.
- CSV fajl je imao prazan prvi red, sto je izazvalo KeyError.
- Ispravljen je csv fajl i funkcija je uspjesno izvrsena.

### Testiranje
python -m pytest -q

### Provjera kvaliteta
ruff check .
ruff format .
