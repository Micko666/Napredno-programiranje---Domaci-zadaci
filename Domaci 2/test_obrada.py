from obrada import ServisRezervacija


class LazniIzvor:
    def __init__(self, rezervacije: list[dict[str, str]]) -> None:
        self.rezervacije = rezervacije

    def ucitaj(self) -> list[dict[str, str]]:
        return self.rezervacije


class LazniIzvjestaj:
    def __init__(self) -> None:
        self.posljednji_iznos: float | None = None

    def sacuvaj(self, ukupno: float) -> None:
        self.posljednji_iznos = ukupno


def test_vise_rezervacija():
    izvjestaj = LazniIzvjestaj()
    izvor = LazniIzvor([
        {"gost": "Ana", "noci": "3", "cijena_noci": "80"},
        {"gost": "Marko", "noci": "5", "cijena_noci": "65"},
        {"gost": "Ivana", "noci": "2", "cijena_noci": "120"},
    ])
    servis = ServisRezervacija(izvor, izvjestaj)

    assert servis.obradi() == 805.0
    assert izvjestaj.posljednji_iznos == 805.0


def test_prazan_izvor():
    izvjestaj = LazniIzvjestaj()
    servis = ServisRezervacija(LazniIzvor([]), izvjestaj)

    assert servis.obradi() == 0.0
    assert izvjestaj.posljednji_iznos == 0.0


def test_jedna_rezervacija():
    izvjestaj = LazniIzvjestaj()
    izvor = LazniIzvor([{"gost": "Ana", "noci": "2", "cijena_noci": "100"}])
    servis = ServisRezervacija(izvor, izvjestaj)

    assert servis.obradi() == 200.0
    assert izvjestaj.posljednji_iznos == 200.0
