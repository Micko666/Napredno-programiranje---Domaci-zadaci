# Mini projekat 3 - Testiran i obezbijeđen API

## Opis zadatka

API računa cijenu hotelske rezervacije na osnovu broja noćenja, cijene noćenja i popusta.

- `GET /health` - provjera rada API-ja.
- `POST /cijena` - obračun cijene rezervacije.

Pydantic provjerava da je broj noćenja od 1 do 30, cijena veća od 0 i najviše 1000000 EUR, a popust od 0 do 1. Gornja granica cijene je demonstraciono ograničenje uvedeno radi ekstremnih unosa.

## Fajlovi

- `main.py` - API.
- `test_api.py` - testovi API-ja.
- `.github/workflows/ci.yml` (u korijenu repozitorijuma) - automatske provjere.

## Pokretanje i testiranje

```bash
python -m pip install fastapi pydantic uvicorn httpx pytest ruff mypy bandit pip-audit
python -m uvicorn main:app --reload

python -m pytest -q
ruff check .
mypy main.py
bandit main.py
pip-audit
```

Napisano je 12 testova koji provjeravaju oba endpointa, obračun sa i bez popusta, granične vrijednosti i neispravne unose. TestClient omogućava testiranje bez pokretanja servera. Ispravni zahtjevi vraćaju status 200, a testirani neispravni unosi 422.

## GitHub Actions

Pri push-u ili pull request-u automatski se pokreću Ruff, mypy i pytest za ovaj domaći zadatak.

## Bezbjednosni rizici

| Rizik | Mjera smanjenja |
| --- | --- |
| Neispravni i ekstremni unosi | Pydantic validacija tipova i opsega. |
| Ranjive biblioteke | Provjera pomoću pip-audit i ažuriranje ranjivih paketa. |
| Tajne u kodu | API nema ključeve ni lozinke; ako se uvedu, čuvati ih u varijablama okruženja. |
| Injekcija | API samo računa cijenu i ne izvršava korisnički unos kao kod ili SQL. |

## Rezultati provjera

- pytest: svih 12 testova uspješno prošlo (jedno upozorenje o zastarijevanju httpx podrške u TestClient-u).
- Ruff: prvobitno je prijavio grešku I001 u importima. Nakon dodavanja praznog reda između importa, provjera je prošla.
- mypy: nema grešaka u main.py.
- Bandit: nije pronašao bezbjednosne propuste u main.py.
- pip-audit: prva provjera zajedničkog Python okruženja prijavila je 407 nalaza u 33 paketa, uključujući biblioteke drugih projekata i zastarjele zavisnosti API-ja. Kreirano je zasebno virtuelno okruženje i instalirane potrebne biblioteke. Ponovna provjera: No known vulnerabilities found.
- GitHub Actions: [uspješan CI run](https://github.com/Micko666/Napredno-programiranje---Domaci-zadaci/actions/runs/46137920064).

## Korišćenje AI alata

ChatGPT je korišćen za pomoć pri prilagođavanju postojećeg API-ja, pripremi CI workflow-a i formatiranje README-a.
