# Mini projekat 1 – Refaktoring obrade rezervacija

## Opis zadatka

Cilj projekta je refaktorisanje jednostavnog programa za obradu rezervacija. Polazni kod objedinjava učitavanje podataka, obračun ukupnog iznosa i kreiranje izvještaja. Refaktoringom su ove odgovornosti razdvojene u zasebne klase, uz primjenu SOLID principa S i D, kako bi kod bio čitljiviji, jednostavniji za održavanje i testiranje.

## Fajlovi

- `prije_refaktoringa.py` – početna verzija programa koja objedinjava više odgovornosti.
- `obrada.py` – refaktorisani kod sa razdvojenim odgovornostima.
- `pokreni.py` – pokretanje programa i prikaz rezultata.
- `rezervacije.csv` – primjer podataka o rezervacijama.
- `test_obrada.py` – tri pytest testa za provjeru funkcionalnosti.

## Primijenjeni SOLID principi

**S – Single Responsibility Principle**

Odgovornosti su podijeljene između klasa:
- `CSVIzvor` – učitavanje podataka.
- `ServisRezervacija` – obračun ukupnog iznosa i pozivanje izvještavanja.
- `TekstualniIzvjestaj` – čuvanje rezultata.

**D – Dependency Inversion Principle**

`ServisRezervacija` koristi `Protocol` interfejse `IzvorPodataka` i `Izvjestavanje`, umjesto da direktno zavisi od konkretnih implementacija. Time je omogućeno jednostavnije testiranje pomoću zamjenskih objekata.

## Pokretanje i testiranje

Program se pokreće iz foldera `Domaci 2`:

```powershell
python pokreni.py
python -m pytest -q
ruff check .
```

Očekivani rezultat obračuna je `805.0`, a sadržaj generisanog fajla `izvjestaj.txt` je `805.00`. Napisana su tri pytest testa koja provjeravaju obradu više rezervacija, praznog izvora podataka i jedne rezervacije. Prilikom lokalnog testiranja sva tri testa su uspješno prošla.

## Korišćenje AI alata

1. AI asistent je korišćen kao pomoć pri kreiranju primjera CSV fajla, kao i za početne smjernice u organizaciji koda.
2. Koriscenje S principa za refraktorisanje pocetnog koda. Kako uraditi to na efikasan i smislen nacin.
3. Kako ispisati tacne testove za uspjesnu procjenu i testitranje kod?

## Uočeni problemi i ispravke

- U početnoj verziji generisanog rješenja izlazno ponašanje originalnog i refaktorisanog programa nije bilo potpuno usklađeno. To je ispravljeno kako bi oba programa računala i čuvala isti rezultat.
- Prilikom provjere pomoću Ruff alata pojavila se greška `I001`, koja se odnosila na redosljed importovanja u fajlu `pokreni.py`. Za ispravku je korišćena komanda `ruff check . --fix`.
- Prilikom pokretanja testova ustanovljeno je da sistemski Python nije pronalazio `pytest`, pa su testovi pokrenuti pomoću Pythona iz virtuelnog okruženja.
Nakon provjera, program je uspješno izvršen i sva tri pytest testa su prošla.