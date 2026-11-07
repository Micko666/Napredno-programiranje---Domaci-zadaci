import csv


class UpravljanjeRezervacijama:
    def __init__(self, ulaz: str, izlaz: str) -> None:
        self.ulaz = ulaz
        self.izlaz = izlaz

    def ucitaj(self) -> list[dict[str, str]]:
        with open(self.ulaz, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def izracunaj(self, rezervacije: list[dict[str, str]]) -> float:
        ukupno = 0.0
        for r in rezervacije:
            ukupno += int(r["noci"]) * float(r["cijena_noci"])
        return ukupno

    def sacuvaj(self, ukupno: float) -> None:
        with open(self.izlaz, "w", encoding="utf-8") as f:
            f.write(f"{ukupno:.2f}")

    def obradi(self) -> float:
        ukupno = self.izracunaj(self.ucitaj())
        self.sacuvaj(ukupno)
        return ukupno
