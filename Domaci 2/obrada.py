import csv
from typing import Protocol


class IzvorPodataka(Protocol):
    def ucitaj(self) -> list[dict[str, str]]: ...


class Izvjestavanje(Protocol):
    def sacuvaj(self, ukupno: float) -> None: ...


class CSVIzvor:
    def __init__(self, putanja: str) -> None:
        self.putanja = putanja

    def ucitaj(self) -> list[dict[str, str]]:
        with open(self.putanja, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))


class TekstualniIzvjestaj:
    def __init__(self, putanja: str) -> None:
        self.putanja = putanja

    def sacuvaj(self, ukupno: float) -> None:
        with open(self.putanja, "w", encoding="utf-8") as f:
            f.write(f"{ukupno:.2f}")


class ServisRezervacija:
    def __init__(self, izvor: IzvorPodataka, izvjestaj: Izvjestavanje) -> None:
        self.izvor = izvor
        self.izvjestaj = izvjestaj

    def izracunaj(self, rezervacije: list[dict[str, str]]) -> float:
        ukupno = 0.0
        for r in rezervacije:
            ukupno += int(r["noci"]) * float(r["cijena_noci"])
        return ukupno

    def obradi(self) -> float:
        ukupno = self.izracunaj(self.izvor.ucitaj())
        self.izvjestaj.sacuvaj(ukupno)
        return ukupno
