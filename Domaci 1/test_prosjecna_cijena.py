from Prosjecna_cijena import prosjecna_cijena


def test_prosjecna_cijena():
    rezultat = prosjecna_cijena("rezervacije.csv")
    assert rezultat == 80.5
