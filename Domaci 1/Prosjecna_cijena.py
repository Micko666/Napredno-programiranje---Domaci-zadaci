import csv


def prosjecna_cijena(p: str) -> float:
    """Racuna prosjecnu cijenu nocenja ponderisanu brojem noci."""
    ukupno = 0
    iznos = 0.0
    with open(p, newline="", encoding="utf-8") as k:
        for n in csv.DictReader(k):
            try:
                noci = int(n["noci"])
                cijena = float(n["cijena_noci"])
            except (ValueError, TypeError, KeyError):
                raise ValueError("Neispravni podaci u CSV fajlu")

            if noci <= 0 or cijena < 0:
                raise ValueError("Neispravan broj noci ili cijena")

            ukupno += noci
            iznos += noci * cijena
    if ukupno == 0:
        raise ValueError("Nema rezervacija")
    return iznos / ukupno
